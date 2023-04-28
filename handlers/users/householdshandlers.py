import logging
from aiogram.types import Message, CallbackQuery
from keyboards.inline.householdskeyboard import householdsMenu, mkmenu, plmenu, xlmenu
from keyboards.inline.phoneskeyboard import cancelmenu
from loader import dp
import PHOTOS




@dp.message_handler(text_contains='Бытовые Техники')
async def select_nhijhyg(message: Message):
 await message.answer(f"Выберите тип Бытовой Техники:", reply_markup=householdsMenu)




                             #FOR MIKROVOLNOVKI


@dp.callback_query_handler(text="mk")
async def buy_mk(call: CallbackQuery):
  await call.message.answer("Выберите Бренд Микроволновки👇", reply_markup=mkmenu)
  await call.message.delete()
  await call.answer(cache_time=60)


@dp. callback_query_handler(text="slmsung")
async def SLMSNG(call: CallbackQuery):
  global photo
  photo = open('PHOTOS/MIKROSAM.png', 'rb')
  await call.bot.send_photo(call.message.chat.id, photo, caption='Характеристики:\nПроцессор: 4HM, 2,8ГГЦ\nОперативная память: 12GB\nВстроенная память: 256/512GB\nБатарея: 5000 MA-Ч\nЭкран: 6,8 дюма, AMOLED, 120ГГЦ\nКамера: 108Mn + 13 Mn\nФронтальная камера: 40МП\n\nЦена: 2.000$.',reply_markup=cancelmenu)

  await call.answer(cache_time=60)

@dp. callback_query_handler(text="panasonic")
async def EFFFF(call: CallbackQuery):
  global photo
  photo = open('PHOTOS/MIKROPANASONIC.png', 'rb')
  await call.bot.send_photo(call.message.chat.id, photo, caption='Характеристики:\nПроцессор: 4HM, 2,8ГГЦ\nОперативная память: 12GB\nВстроенная память: 256/512GB\nБатарея: 5000 MA-Ч\nЭкран: 6,8 дюма, AMOLED, 120ГГЦ\nКамера: 108Mn + 13 Mn\nФронтальная камера: 40МП\n\nЦена: 2.000$.',reply_markup=cancelmenu)

  await call.answer(cache_time=60)


@dp.callback_query_handler(text="cancel2")
async def cancel_fghgf(call: CallbackQuery):
  await call.message.edit_reply_markup(reply_markup=householdsMenu)
  await call.answer()



                                  #FOR PILESOSI


@dp.callback_query_handler(text="pl")
async def buy_mk(call: CallbackQuery):
  await call.message.answer("Выберите Бренд Пылесоса👇", reply_markup=plmenu)
  await call.message.delete()
  await call.answer(cache_time=60)


@dp. callback_query_handler(text="dyson")
async def hitachi(call: CallbackQuery):
  global photo
  photo = open('PHOTOS/PILDYSON.png', 'rb')
  await call.bot.send_photo(call.message.chat.id, photo, caption='Характеристики:\nПроцессор: 4HM, 2,8ГГЦ\nОперативная память: 12GB\nВстроенная память: 256/512GB\nБатарея: 5000 MA-Ч\nЭкран: 6,8 дюма, AMOLED, 120ГГЦ\nКамера: 108Mn + 13 Mn\nФронтальная камера: 40МП\n\nЦена: 15.000$.',reply_markup=cancelmenu)

  await call.answer(cache_time=60)

@dp. callback_query_handler(text="lg")
async def EFFFF(call: CallbackQuery):
  global photo
  photo = open('PHOTOS/PILLG.png', 'rb')
  await call.bot.send_photo(call.message.chat.id, photo, caption='Характеристики:\nПроцессор: 4HM, 2,8ГГЦ\nОперативная память: 12GB\nВстроенная память: 256/512GB\nБатарея: 5000 MA-Ч\nЭкран: 6,8 дюма, AMOLED, 120ГГЦ\nКамера: 108Mn + 13 Mn\nФронтальная камера: 40МП\n\nЦена: 99.000$.',reply_markup=cancelmenu)

  await call.answer(cache_time=60)


@dp.callback_query_handler(text="cancel2")
async def cancel_fghgf(call: CallbackQuery):
  await call.message.edit_reply_markup(reply_markup=householdsMenu)
  await call.answer()



                        #FOR XOLODILNIKI

@dp.callback_query_handler(text="xl")
async def buy_mk(call: CallbackQuery):
  await call.message.answer("Выберите Бренд Холодильника👇", reply_markup=xlmenu)
  await call.message.delete()
  await call.answer(cache_time=60)


@dp. callback_query_handler(text="hitachi")
async def SLMSNG(call: CallbackQuery):
  global photo
  photo = open('PHOTOS/XOLHITACHI.png', 'rb')
  await call.bot.send_photo(call.message.chat.id, photo, caption='Характеристики:\nПроцессор: 4HM, 2,8ГГЦ\nОперативная память: 12GB\nВстроенная память: 256/512GB\nБатарея: 5000 MA-Ч\nЭкран: 6,8 дюма, AMOLED, 120ГГЦ\nКамера: 108Mn + 13 Mn\nФронтальная камера: 40МП\n\nЦена: 5.000$.',reply_markup=cancelmenu)

  await call.answer(cache_time=60)

@dp. callback_query_handler(text="bosch")
async def EFFFF(call: CallbackQuery):
  global photo
  photo = open('PHOTOS/XOLBOSCH.png', 'rb')
  await call.bot.send_photo(call.message.chat.id, photo, caption='Характеристики:\nПроцессор: 4HM, 2,8ГГЦ\nОперативная память: 12GB\nВстроенная память: 256/512GB\nБатарея: 5000 MA-Ч\nЭкран: 6,8 дюма, AMOLED, 120ГГЦ\nКамера: 108Mn + 13 Mn\nФронтальная камера: 40МП\n\nЦена: 1.000$.',reply_markup=cancelmenu)

  await call.answer(cache_time=60)


@dp.callback_query_handler(text="cancel2")
async def cancel_fghgf(call: CallbackQuery):
  await call.message.edit_reply_markup(reply_markup=householdsMenu)
  await call.answer()