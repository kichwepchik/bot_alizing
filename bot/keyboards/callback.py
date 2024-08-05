from aiogram import types
from aiogram.dispatcher import FSMContext
from bot.keyboards.inline import get_it_request_buttons, get_back_button, get_attachment_buttons
from bot.main import ITRequestForm

async def process_callback_query(callback_query: types.CallbackQuery, state: FSMContext):
    if callback_query.data == "provide_contact":
        await callback_query.message.answer(
            "Пожалуйста, отправьте свой контакт.",
            reply_markup=types.ReplyKeyboardMarkup(
                keyboard=[
                    [types.KeyboardButton(text="Отправить контакт", request_contact=True)]
                ], resize_keyboard=True, one_time_keyboard=True
            )
        )
        await callback_query.answer()
    elif callback_query.data == "create_request":
        await ITRequestForm.subject.set()
        await callback_query.message.answer("Тема обращения макс. 50 символов", reply_markup=get_back_button())
    elif callback_query.data == "back_to_menu":
        await state.finish()
        await callback_query.message.answer("Выберите одну из опций:", reply_markup=reply_keyboard)
    elif callback_query.data == "back_to_it_requests":
        await callback_query.message.answer("Вы выбрали IT-заявки.", reply_markup=get_it_request_buttons())
    elif callback_query.data == "add_attachment":
        await ITRequestForm.attachment.set()
        await callback_query.message.answer("Отправьте вложение (фото или документ).")
    elif callback_query.data == "skip_attachment":
        await state.finish()
        await callback_query.message.answer("Вложение пропущено.", reply_markup=reply_keyboard)
