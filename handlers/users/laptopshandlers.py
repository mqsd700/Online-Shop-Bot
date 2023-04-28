import logging
from aiogram.types import Message, CallbackQuery
from keyboards.inline.laptopskeyboard import laptopsMenu, hpmenu, acermenu, lenovomenu
from keyboards.inline.phoneskeyboard import cancelmenu
from loader import dp
import PHOTOS




@dp.message_handler(text_contains= "Ноутбуки")
async def select_category(message: Message):
 await message.answer(f"Выберите марку ноутбука:", reply_markup=laptopsMenu)


@dp.callback_query_handler(text="hp")
async def buy_samsung(call: CallbackQuery):
  await call.message.answer("Выберите модель ноутбука👇", reply_markup=hpmenu)
  await call.message.delete()
  await call.answer(cache_time=60)

@dp. callback_query_handler(text="omen")
async def omen(call: CallbackQuery):
  global photo
  photo = open('PHOTOS/HPOMEN.png', 'rb')
  await call.bot.send_photo(call.message.chat.id, photo, caption='Характеристики:\nПроцессор: 4HM, 2,8ГГЦ\nОперативная память: 12GB\nВстроенная память: 256/512GB\nБатарея: 5000 MA-Ч\nЭкран: 6,8 дюма, AMOLED, 120ГГЦ\nКамера: 108Mn + 13 Mn\nФронтальная камера: 40МП\n\nЦена: 2.000$.',reply_markup=cancelmenu)

  await call.answer(cache_time=60)


@dp. callback_query_handler(text="pavilion")
async def omen(call: CallbackQuery):
  global photo
  photo = open('PHOTOS/HPPAVILION.png', 'rb')
  await call.bot.send_photo(call.message.chat.id, photo, caption='Характеристики:\nПроцессор: 4HM, 2,8ГГЦ\nОперативная память: 12GB\nВстроенная память: 256/512GB\nБатарея: 5000 MA-Ч\nЭкран: 6,8 дюма, AMOLED, 120ГГЦ\nКамера: 108Mn + 13 Mn\nФронтальная камера: 40МП\n\nЦена: 2.000$.',reply_markup=cancelmenu)

  await call.answer(cache_time=60)


@dp. callback_query_handler(text="probook")
async def omen(call: CallbackQuery):
  global photo
  photo = open('PHOTOS/HPPROBOOK.png', 'rb')
  await call.bot.send_photo(call.message.chat.id, photo, caption='Характеристики:\nПроцессор: 4HM, 2,8ГГЦ\nОперативная память: 12GB\nВстроенная память: 256/512GB\nБатарея: 5000 MA-Ч\nЭкран: 6,8 дюма, AMOLED, 120ГГЦ\nКамера: 108Mn + 13 Mn\nФронтальная камера: 40МП\n\nЦена: 2.000$.',reply_markup=cancelmenu)

  await call.answer(cache_time=60)


@dp.callback_query_handler(text="cancel1")
async def cancel_buying(call: CallbackQuery):
 await call.message.edit_reply_markup(reply_markup=laptopsMenu)
 await call.answer()



                   #FOR ACER LAPTOPS!

@dp.callback_query_handler(text="acer")
async def buy_ACER(call: CallbackQuery):
  await call.message.answer("Выберите модель ноутбука👇", reply_markup=acermenu)
  await call.message.delete()
  await call.answer(cache_time=60)


@dp. callback_query_handler(text="nitro")
async def nitro(call: CallbackQuery):
  global photo
  photo = open('PHOTOS/ACRNITRO.png', 'rb')
  await call.bot.send_photo(call.message.chat.id, photo, caption='Характеристики:\nПроцессор: 4HM, 2,8ГГЦ\nОперативная память: 12GB\nВстроенная память: 256/512GB\nБатарея: 5000 MA-Ч\nЭкран: 6,8 дюма, AMOLED, 120ГГЦ\nКамера: 108Mn + 13 Mn\nФронтальная камера: 40МП\n\nЦена: 2.000$.',reply_markup=cancelmenu)

  await call.answer(cache_time=60)


@dp. callback_query_handler(text="predator")
async def RGRGR(call: CallbackQuery):
  global photo
  photo = open('PHOTOS/ACRPREDATOR.png', 'rb')
  await call.bot.send_photo(call.message.chat.id, photo, caption='Характеристики:\nПроцессор: 4HM, 2,8ГГЦ\nОперативная память: 12GB\nВстроенная память: 256/512GB\nБатарея: 5000 MA-Ч\nЭкран: 6,8 дюма, AMOLED, 120ГГЦ\nКамера: 108Mn + 13 Mn\nФронтальная камера: 40МП\n\nЦена: 2.000$.',reply_markup=cancelmenu)

  await call.answer(cache_time=60)


@dp. callback_query_handler(text="aspire")
async def ASPIRE(call: CallbackQuery):
  global photo
  photo = open('PHOTOS/ACRASPIRE.png', 'rb')
  await call.bot.send_photo(call.message.chat.id, photo, caption='Характеристики:\nПроцессор: 4HM, 2,8ГГЦ\nОперативная память: 12GB\nВстроенная память: 256/512GB\nБатарея: 5000 MA-Ч\nЭкран: 6,8 дюма, AMOLED, 120ГГЦ\nКамера: 108Mn + 13 Mn\nФронтальная камера: 40МП\n\nЦена: 2.000$.',reply_markup=cancelmenu)

  await call.answer(cache_time=60)


@dp.callback_query_handler(text="cancel1")
async def cancel_buying(call: CallbackQuery):
 await call.message.edit_reply_markup(reply_markup=laptopsMenu)
 await call.answer()


                          #FOR LENOVO LAPTOPS!

@dp.callback_query_handler(text="lenovo")
async def buy_lenovo(call: CallbackQuery):
  await call.message.answer("Выберите модель ноутбука👇", reply_markup=lenovomenu)
  await call.message.delete()
  await call.answer(cache_time=60)


@dp. callback_query_handler(text="legion")
async def legion(call: CallbackQuery):
  global photo
  photo = open('PHOTOS/LNVLEGION.png', 'rb')
  await call.bot.send_photo(call.message.chat.id, photo, caption='Характеристики:\nПроцессор: 4HM, 2,8ГГЦ\nОперативная память: 12GB\nВстроенная память: 256/512GB\nБатарея: 5000 MA-Ч\nЭкран: 6,8 дюма, AMOLED, 120ГГЦ\nКамера: 108Mn + 13 Mn\nФронтальная камера: 40МП\n\nЦена: 2.000$.',reply_markup=cancelmenu)

  await call.answer(cache_time=60)


@dp. callback_query_handler(text="ideapad")
async def ideapad(call: CallbackQuery):
  global photo
  photo = open('PHOTOS/LNVIDEAPAD.png', 'rb')
  await call.bot.send_photo(call.message.chat.id, photo, caption='Характеристики:\nПроцессор: 4HM, 2,8ГГЦ\nОперативная память: 12GB\nВстроенная память: 256/512GB\nБатарея: 5000 MA-Ч\nЭкран: 6,8 дюма, AMOLED, 120ГГЦ\nКамера: 108Mn + 13 Mn\nФронтальная камера: 40МП\n\nЦена: 2.000$.',reply_markup=cancelmenu)

  await call.answer(cache_time=60)


@dp. callback_query_handler(text="thinkpad")
async def thinkpad(call: CallbackQuery):
  global photo
  photo = open('PHOTOS/LNVTHINKPAD.png', 'rb')
  await call.bot.send_photo(call.message.chat.id, photo, caption='Характеристики:\nПроцессор: 4HM, 2,8ГГЦ\nОперативная память: 12GB\nВстроенная память: 256/512GB\nБатарея: 5000 MA-Ч\nЭкран: 6,8 дюма, AMOLED, 120ГГЦ\nКамера: 108Mn + 13 Mn\nФронтальная камера: 40МП\n\nЦена: 2.000$.',reply_markup=cancelmenu)

  await call.answer(cache_time=60)


@dp.callback_query_handler(text="cancel1")
async def cancel_buying(call: CallbackQuery):
 await call.message.edit_reply_markup(reply_markup=laptopsMenu)
 await call.answer()