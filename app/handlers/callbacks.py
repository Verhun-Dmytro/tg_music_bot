#from handlers.start import router
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def generated_inline_keyboard(musiclist):

    try:
        
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text=title, callback_data=f'{vid}')
                ]
                for title, vid in musiclist.items()
            ]
        )
        return keyboard
    except Exception as e:
        print(e)
        return None
