from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                               keyboard = [
                                   [
                                       KeyboardButton(text="📞Мой Контакт",
                                                      request_contact=True)
                                   ]
                               ])