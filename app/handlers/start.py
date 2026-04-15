from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import CallbackQuery
from handlers.callbacks import generated_inline_keyboard
from database.db import search_user_and_add
from services.music_services import search_music_ytdlp, clip_music


router = Router()


@router.message(Command("start"))
async def start(message: types.Message):
    user = search_user_and_add(message.from_user.id, message.from_user.username)
    await message.answer(
        f"Привіт {message.from_user.full_name}! Я, бот по пошуку музики, напиши назву пісні або виконавця, а я знайду його пісні! Якщо щось забудеш використовуй команду /help"
    )


@router.message(Command("help"))
async def help(message: types.Message):
    await message.answer(
        f"Ой лялечко, забув як користуватись? Я, бот по пошуку музики, напиши назву пісні або виконавця, а я знайду його пісні!"
    )


@router.message(F.text.startswith("/"))
async def help(message: types.Message):
    await message.answer(
        f"Ой лялечко, забув як користуватись? Я, бот по пошуку музики, напиши назву пісні або виконавця, а я знайду його пісні!"
    )


@router.message()
async def start_search_music(message: types.Message):
    try:
        src_music = search_music_ytdlp(message.text)
        list_music = clip_music(src_music)

        if len(list_music) > 0:
                 
            await message.answer("Обирай пісню:", reply_markup=generated_inline_keyboard())
    except:
        print("Проблема! Щось пішло не так з пошуком музики!")
        await message.answer("Пробач, щось пішло не так, ми вже працюємо над цим.")


@router.callback_query()
async def handle_button_music(callback: CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=None)
    await callback.message.delete()
