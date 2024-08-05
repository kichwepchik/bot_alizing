from aiogram import Bot, Dispatcher
import logging
import asyncio
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import CommandStart
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from dotenv import load_dotenv
from bot.settings import settings
from bot.utils.commands import set_commands
from bot.keyboards.callback import process_callback_query
from bot.keyboards.reply import reply_keyboard
from handlers.registration import handle_start_command, handle_contact
from handlers.menu import handle_it_requests, handle_agreement, handle_delivery, handle_hr_assistant
from handlers.it_requests import handle_create_request

load_dotenv()

class ITRequestForm(StatesGroup):
    subject = State()
    description = State()
    attachment = State()

async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text='Bot ON!')

async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Bot OFF!')

async def start():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    bot = Bot(token=settings.bots.bot_token, default=DefaultBotProperties(parse_mode='HTML'))
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(handle_start_command, CommandStart())
    dp.message.register(handle_contact, lambda message: message.contact is not None)
    dp.message.register(handle_it_requests, lambda message: message.text == 'IT-заявки')
    dp.message.register(handle_agreement, lambda message: message.text == 'Согласование')
    dp.message.register(handle_delivery, lambda message: message.text == 'Отгрузка(водители)')
    dp.message.register(handle_hr_assistant, lambda message: message.text == 'HR-помощник')
    dp.message.register(handle_create_request, state=ITRequestForm.subject)
    dp.message.register(handle_create_request, state=ITRequestForm.description)
    dp.callback_query.register(process_callback_query)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())
