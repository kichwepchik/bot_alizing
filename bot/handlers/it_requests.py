from aiogram import types
from bot.keyboards.inline import get_it_request_buttons, get_back_button, get_attachment_buttons

async def handle_it_requests(message: types.Message):
    await message.answer("Вы выбрали IT-заявки.", reply_markup=get_it_request_buttons())

async def handle_create_request(message: types.Message, state):
    async with state.proxy() as data:
        if 'subject' not in data:
            if len(message.text) <= 50:
                data['subject'] = message.text
                await message.answer("Предоставьте описание проблемы.")
            else:
                await message.answer("Тема обращения слишком длинная. Максимум 50 символов.")
        elif 'description' not in data:
            data['description'] = message.text
            await message.answer("Описание получено.", reply_markup=get_attachment_buttons())
