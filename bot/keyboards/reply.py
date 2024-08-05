from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

# Основная клавиатура
reply_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='IT-заявки')
        ],
        [
            KeyboardButton(text='Согласование')
        ],
        [
            KeyboardButton(text='Отгрузка(водители)')
        ],
        [
            KeyboardButton(text='HR-помощник')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    selective=True
)
