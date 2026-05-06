from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import CallbackQuery, FSInputFile
from aiogram.exceptions import TelegramBadRequest, TelegramForbiddenError
from .callbacks import generated_inline_keyboard
from database.db import search_user_and_add, add_music_list
from services.music_services import search_music_ytdlp, clip_music
from services.dowloader import dowload_music, delete_music, convert_video_to_audio


router = Router()


@router.message(Command("start"))
async def start(message: types.Message):
    user = search_user_and_add(message.from_user.id, message.from_user.username)
    await message.answer(
        f"Привіт {message.from_user.full_name}! Я бот по пошуку музики, напиши назву пісні або виконавця, а я знайду його пісні! Якщо щось забудеш використовуй команду /help"
    )


@router.message(Command("help"))
async def help(message: types.Message):
    await message.answer(
        f"Ой лялечко, забув як користуватись? Я бот по пошуку музики, напиши назву пісні або виконавця, а я знайду його пісні!"
    )


@router.message(F.text.startswith("/"))
async def help(message: types.Message):
    await message.answer(
        f"Ой лялечко, забув як користуватись? Я бот по пошуку музики, напиши назву пісні або виконавця, а я знайду його пісні!"
    )


@router.message()
async def start_search_music(message: types.Message):
    try:
        src_music = search_music_ytdlp(message.text)
        list_music = clip_music(src_music)

        if len(list_music) > 0:
                 
            await message.answer("Обирай пісню:", reply_markup=generated_inline_keyboard(list_music))
    except Exception as e:
        print(f"Error! {e}")
        await message.answer("Пробач, щось пішло не так, ми вже працюємо над цим.")


@router.callback_query()
async def handle_button_music(callback: CallbackQuery):
    try:
        await callback.message.edit_reply_markup(reply_markup=None)
        await callback.message.delete()

        music_pl = dowload_music(callback.data)
        audio = convert_video_to_audio(music_pl)

        if not audio:
            raise ValueError("Audio not created")

        audio_send = FSInputFile(audio)

        await callback.message.answer_audio(audio=audio_send)

        add_music_list(callback.from_user.id, music_pl["filename"])

        delete_music(music_pl["output"])
        delete_music(audio)

    except (TelegramBadRequest, TelegramForbiddenError) as e:
        print(f"Telegram error: {e}")
        await callback.answer("Проблема з Telegram повідомленням")

    except Exception as e:
        print(f"General error: {e}")
        await callback.answer("Не вдалося обробити аудіо. Спробуйте ще раз.")
