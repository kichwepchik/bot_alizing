from aiogram import types

async def handle_it_requests(message: types.Message):
    await message.answer("Вы выбрали IT-заявки.")

async def handle_agreement(message: types.Message):
    await message.answer("Вы выбрали Согласование.")

async def handle_delivery(message: types.Message):
    await message.answer("Вы выбрали Отгрузка(водители).")

async def handle_hr_assistant(message: types.Message):
    await message.answer("Вы выбрали HR-помощник.")
