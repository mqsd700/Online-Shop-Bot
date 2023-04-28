from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuStart = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Смартфоны📱'),
            KeyboardButton(text='Ноутбуки💻'),
            KeyboardButton(text='Бытовые Техники📺'),
        ],
    ],
     resize_keyboard=True
    )