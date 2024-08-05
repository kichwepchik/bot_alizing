from aiogram import types
from aiogram.exceptions import TelegramForbiddenError
from bot.keyboards.inline import get_contact_button
from bot.keyboards.reply import reply_keyboard

async def handle_start_command(message: types.Message):
    try:
        keyboard = get_contact_button()
        await message.answer("Пожалуйста, предоставьте ваш номер телефона", reply_markup=keyboard)
    except TelegramForbiddenError:
        print(f"Не удалось отправить сообщение пользователю {message.from_user.id}: бот был заблокирован пользователем.")

async def handle_contact(message: types.Message):
    if message.contact:
        await message.answer(f"Спасибо, {message.contact.first_name}! Ваш номер {message.contact.phone_number} получен.")
        await message.answer("Выберите одну из опций:", reply_markup=reply_keyboard)
