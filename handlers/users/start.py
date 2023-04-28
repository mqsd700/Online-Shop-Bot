from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, Command
import logging

from keyboards.default.Mainbuttons import menuStart
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
     #logging.info(message)
     #logging.info(f"{message.from_user.id=}")
     #logging.info(f"{message.from_user.full_name=}")
     await message.answer(f"Привет {message.from_user.full_name} 🖐 Оформим ваш заказ вместе?🤓")
     await message.answer(f"Выберите Технику👇", reply_markup=menuStart)

@dp.message_handler(Command('menu'))
async def bot_menu(message: types.Message):
     await message.answer( f"Вебырите Технику👇",reply_markup=menuStart)