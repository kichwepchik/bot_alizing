from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_contact_button():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Предоставить номер", callback_data="provide_contact")]
    ])

def get_it_request_buttons():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Создать заявку", callback_data="create_request")],
        [InlineKeyboardButton(text="Назад", callback_data="back_to_menu")]
    ])

def get_back_button():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад", callback_data="back_to_it_requests")]
    ])

def get_attachment_buttons():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Добавить вложение", callback_data="add_attachment")],
        [InlineKeyboardButton(text="Пропустить", callback_data="skip_attachment")]
    ])
