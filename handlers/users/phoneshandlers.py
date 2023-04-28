import logging
from aiogram.types import Message, CallbackQuery
from keyboards.inline.phoneskeyboard import categoryMenu, samsungMenu, cancelmenu, iphonemenu, huaweimenu, redmimenu, oppomenu
from loader import dp
import PHOTOS




@dp.message_handler(text_contains= "Смартфоны")
async def select_category(message: Message):
 await message.answer(f"Выберите марку телефона:", reply_markup=categoryMenu)



# FOR SAMSUNG PHONES!

@dp.callback_query_handler(text="samsung")
async def buy_samsung(call: CallbackQuery):
  await call.message.answer("Выберите модель телефона👇", reply_markup=samsungMenu)
  await call.message.delete()
  await call.answer(cache_time=60)


@dp. callback_query_handler(text="s22ultra")
async def s22ultra(call: CallbackQuery):
  global photo
  photo = open('PHOTOS/S22ULTRA.png', 'rb')
  await call.bot.send_photo(call.message.chat.id, photo, caption='Характеристики:\nПроцессор: 4HM, 2,8ГГЦ\nОперативная память: 12GB\nВстроенная память: 256/512GB\nБатарея: 5000 MA-Ч\nЭкран: 6,8 дюма, AMOLED, 120ГГЦ\nКамера: 108Mn + 13 Mn\nФронтальная камера: 40МП\n\nЦена: 2.000$.',reply_markup=cancelmenu)

  await call.answer(cache_time=60)


@dp.callback_query_handler(text="s21ultra")
async def s21ultra(call: CallbackQuery):
  global photo
  photo = open('PHOTOS/S21.png', 'rb')
  await call.bot.send_photo(call.message.chat.id, photo, caption='Характеристики:\nПроцессор: 4HM, 2,8ГГЦ\nОперативная память: 12GB\nВстроенная память: 256/512GB\nБатарея: 5000 MA-Ч\nЭкран: 6,8 дюма, AMOLED, 120ГГЦ\nКамера: 108Mn + 13 Mn\nФронтальная камера: 40МП\n\nЦена: 1.000$.',reply_markup=cancelmenu)

  await call.answer(cache_time=60)

@dp.callback_query_handler(text="zflip4")
async def s21ultra(call: CallbackQuery):
  global photo
  photo = open('PHOTOS/ZFLIP4.png', 'rb')
  await call.bot.send_photo(call.message.chat.id, photo, caption='Характеристики:\nПроцессор: 4HM, 2,8ГГЦ\nОперативная память: 12GB\nВстроенная память: 256/512GB\nБатарея: 5000 MA-Ч\nЭкран: 6,8 дюма, AMOLED, 120ГГЦ\nКамера: 108Mn + 13 Mn\nФронтальная камера: 40МП\n\nЦена: 5.000$.',reply_markup=cancelmenu)

  await call.answer(cache_time=60)


@dp.callback_query_handler(text="a52")
async def s21ultra(call: CallbackQuery):
  global photo
  photo = open('PHOTOS/A52.png', 'rb')
  await call.bot.send_photo(call.message.chat.id, photo, caption='Характеристики:\nПроцессор: 4HM, 2,8ГГЦ\nОперативная память: 12GB\nВстроенная память: 256/512GB\nБатарея: 5000 MA-Ч\nЭкран: 6,8 дюма, AMOLED, 120ГГЦ\nКамера: 108Mn + 13 Mn\nФронтальная камера: 40МП\n\nЦена: 700$.',reply_markup=cancelmenu)
  await call.answer(cache_time=60)


@dp.callback_query_handler(text="s10")
async def s21ultra(call: CallbackQuery):
  global photo
  photo = open('PHOTOS/S10.png', 'rb')
  await call.bot.send_photo(call.message.chat.id, photo, caption='Характеристики:\nПроцессор: 4HM, 2,8ГГЦ\nОперативная память: 12GB\nВстроенная память: 256/512GB\nБатарея: 5000 MA-Ч\nЭкран: 6,8 дюма, AMOLED, 120ГГЦ\nКамера: 108Mn + 13 Mn\nФронтальная камера: 40МП\n\nЦена: 900$.',reply_markup=cancelmenu)
  await call.answer(cache_time=60)

@dp.callback_query_handler(text="cancel")
async def cancel_buying(call: CallbackQuery):
  await call.message.edit_reply_markup(reply_markup=categoryMenu)
  await call.answer()


# FOR IPHONE PHONES!

@dp.callback_query_handler(text="iphone")
async def buy_iphone(call: CallbackQuery):
  await call.message.answer("Выберите модель телефона👇", reply_markup=iphonemenu)
  await call.message.delete()
  await call.answer(cache_time=60)


@dp. callback_query_handler(text="14promax")
async def fourteen(call: CallbackQuery):
  global photo
  photo = open('PHOTOS/IPH14PROMAX.png', 'rb')
  await call.bot.send_photo(call.message.chat.id, photo, caption='Характеристики:\nПроцессор: 4HM, 2,8ГГЦ\nОперативная память: 12GB\nВстроенная память: 256/512GB\nБатарея: 5000 MA-Ч\nЭкран: 6,8 дюма, AMOLED, 120ГГЦ\nКамера: 108Mn + 13 Mn\nФронтальная камера: 40МП\n\nЦена: 3.000$.',reply_markup=cancelmenu)

  await call.answer(cache_time=60)


@dp.callback_query_handler(text="13promax")
async def thirteenpro(call: CallbackQuery):
  global photo
  photo = open('PHOTOS/IPH13PROMAX.png', 'rb')
  await call.bot.send_photo(call.message.chat.id, photo, caption='Характеристики:\nПроцессор: 4HM, 2,8ГГЦ\nОперативная память: 12GB\nВстроенная память: 256/512GB\nБатарея: 5000 MA-Ч\nЭкран: 6,8 дюма, AMOLED, 120ГГЦ\nКамера: 108Mn + 13 Mn\nФронтальная камера: 40МП\n\nЦена: 2.500$.',reply_markup=cancelmenu)

  await call.answer(cache_time=60)

@dp.callback_query_handler(text="13mini")
async def thirdteenmini(call: CallbackQuery):
  global photo
  photo = open('PHOTOS/IPH13MINI.png', 'rb')
  await call.bot.send_photo(call.message.chat.id, photo, caption='Характеристики:\nПроцессор: 4HM, 2,8ГГЦ\nОперативная память: 12GB\nВстроенная память: 256/512GB\nБатарея: 5000 MA-Ч\nЭкран: 6,8 дюма, AMOLED, 120ГГЦ\nКамера: 108Mn + 13 Mn\nФронтальная камера: 40МП\n\nЦена: 5.000$.',reply_markup=cancelmenu)

  await call.answer(cache_time=60)


@dp.callback_query_handler(text="12promax")
async def tvelf(call: CallbackQuery):
  global photo
  photo = open('PHOTOS/IPH12PROMAX.png', 'rb')
  await call.bot.send_photo(call.message.chat.id, photo, caption='Характеристики:\nПроцессор: 4HM, 2,8ГГЦ\nОперативная память: 12GB\nВстроенная память: 256/512GB\nБатарея: 5000 MA-Ч\nЭкран: 6,8 дюма, AMOLED, 120ГГЦ\nКамера: 108Mn + 13 Mn\nФронтальная камера: 40МП\n\nЦена: 700$.',reply_markup=cancelmenu)
  await call.answer(cache_time=60)


@dp.callback_query_handler(text="11promax")
async def eleven(call: CallbackQuery):
  global photo
  photo = open('PHOTOS/IPH11PROMAX.png', 'rb')
  await call.bot.send_photo(call.message.chat.id, photo, caption='Характеристики:\nПроцессор: 4HM, 2,8ГГЦ\nОперативная память: 12GB\nВстроенная память: 256/512GB\nБатарея: 5000 MA-Ч\nЭкран: 6,8 дюма, AMOLED, 120ГГЦ\nКамера: 108Mn + 13 Mn\nФронтальная камера: 40МП\n\nЦена: 900$.',reply_markup=cancelmenu)
  await call.answer(cache_time=60)

@dp.callback_query_handler(text="cancel")
async def cancel_buying(call: CallbackQuery):
  await call.message.edit_reply_markup(reply_markup=categoryMenu)
  await call.answer()


                     #                      FOR HUAWEI PHONES
@dp.callback_query_handler(text="huawei")
async def buy_iphone(call: CallbackQuery):
  await call.message.answer("Выберите модель телефона👇", reply_markup=huaweimenu)
  await call.message.delete()
  await call.answer(cache_time=60)


@dp. callback_query_handler(text="p50pro")
async def fiftypro(call: CallbackQuery):
  global photo
  photo = open('PHOTOS/HWIP50PRO.png', 'rb')
  await call.bot.send_photo(call.message.chat.id, photo, caption='Характеристики:\nПроцессор: 4HM, 2,8ГГЦ\nОперативная память: 12GB\nВстроенная память: 256/512GB\nБатарея: 5000 MA-Ч\nЭкран: 6,8 дюма, AMOLED, 120ГГЦ\nКамера: 108Mn + 13 Mn\nФронтальная камера: 40МП\n\nЦена: 8.000$.',reply_markup=cancelmenu)

  await call.answer(cache_time=60)

@dp. callback_query_handler(text="p40pro")
async def fourtypro(call: CallbackQuery):
  global photo
  photo = open('PHOTOS/P40PRO.png', 'rb')
  await call.bot.send_photo(call.message.chat.id, photo, caption='Характеристики:\nПроцессор: 4HM, 2,8ГГЦ\nОперативная память: 12GB\nВстроенная память: 256/512GB\nБатарея: 5000 MA-Ч\nЭкран: 6,8 дюма, AMOLED, 120ГГЦ\nКамера: 108Mn + 13 Mn\nФронтальная камера: 40МП\n\nЦена: 8.000$.',reply_markup=cancelmenu)

  await call.answer(cache_time=60)



@dp.callback_query_handler(text="y7a")
async def ysevena(call: CallbackQuery):
  global photo
  photo = open('PHOTOS/HWIY7A.png', 'rb')
  await call.bot.send_photo(call.message.chat.id, photo, caption='Характеристики:\nПроцессор: 4HM, 2,8ГГЦ\nОперативная память: 12GB\nВстроенная память: 256/512GB\nБатарея: 5000 MA-Ч\nЭкран: 6,8 дюма, AMOLED, 120ГГЦ\nКамера: 108Mn + 13 Mn\nФронтальная камера: 40МП\n\nЦена: 6.000$.',reply_markup=cancelmenu)

  await call.answer(cache_time=60)

@dp.callback_query_handler(text="cancel")
async def cancel_buying(call: CallbackQuery):
  await call.message.edit_reply_markup(reply_markup=categoryMenu)
  await call.answer()

                             #FOR REDMI PHONES!

@dp.callback_query_handler(text="redmi")
async def buy_redmi(call: CallbackQuery):
  await call.message.answer("Выберите модель телефона👇", reply_markup=redmimenu)
  await call.message.delete()
  await call.answer(cache_time=60)


@dp. callback_query_handler(text="11promax")
async def elevenpromax(call: CallbackQuery):
  global photo
  photo = open('PHOTOS/RDM11PROMAX.png', 'rb')
  await call.bot.send_photo(call.message.chat.id, photo, caption='Характеристики:\nПроцессор: 4HM, 2,8ГГЦ\nОперативная память: 12GB\nВстроенная память: 256/512GB\nБатарея: 5000 MA-Ч\nЭкран: 6,8 дюма, AMOLED, 120ГГЦ\nКамера: 108Mn + 13 Mn\nФронтальная камера: 40МП\n\nЦена: 4.000$.',reply_markup=cancelmenu)

  await call.answer(cache_time=60)

@dp. callback_query_handler(text="10promax")
async def ninetypro(call: CallbackQuery):
  global photo
  photo = open('PHOTOS/KOTREDMI.png', 'rb')
  await call.bot.send_photo(call.message.chat.id, photo, caption='Характеристики:\nПроцессор: 4HM, 2,8ГГЦ\nОперативная память: 12GB\nВстроенная память: 256/512GB\nБатарея: 5000 MA-Ч\nЭкран: 6,8 дюма, AMOLED, 120ГГЦ\nКамера: 108Mn + 13 Mn\nФронтальная камера: 40МП\n\nЦена: 8.000$.',reply_markup=cancelmenu)

  await call.answer(cache_time=60)



@dp.callback_query_handler(text="9promax")
async def ysevenafrfr(call: CallbackQuery):
  global photo
  photo = open('PHOTOS/RDM9PROMAX.png', 'rb')
  await call.bot.send_photo(call.message.chat.id, photo, caption='Характеристики:\nПроцессор: 4HM, 2,8ГГЦ\nОперативная память: 12GB\nВстроенная память: 256/512GB\nБатарея: 5000 MA-Ч\nЭкран: 6,8 дюма, AMOLED, 120ГГЦ\nКамера: 108Mn + 13 Mn\nФронтальная камера: 40МП\n\nЦена: 6.000$.',reply_markup=cancelmenu)

  await call.answer(cache_time=60)

@dp.callback_query_handler(text="cancel")
async def cancel_buying(call: CallbackQuery):
  await call.message.edit_reply_markup(reply_markup=categoryMenu)
  await call.answer()

                                        #FOR OPPO PHONES!

@dp.callback_query_handler(text="oppo")
async def buy_redmi(call: CallbackQuery):
  await call.message.answer("Выберите модель телефона👇", reply_markup=oppomenu)
  await call.message.delete()
  await call.answer(cache_time=60)


@dp. callback_query_handler(text="reno5")
async def elevenpromaxgvg(call: CallbackQuery):
  global photo
  photo = open('PHOTOS/OPPORENO5.png', 'rb')
  await call.bot.send_photo(call.message.chat.id, photo, caption='Характеристики:\nПроцессор: 4HM, 2,8ГГЦ\nОперативная память: 12GB\nВстроенная память: 256/512GB\nБатарея: 5000 MA-Ч\nЭкран: 6,8 дюма, AMOLED, 120ГГЦ\nКамера: 108Mn + 13 Mn\nФронтальная камера: 40МП\n\nЦена: 4.000$.',reply_markup=cancelmenu)

  await call.answer(cache_time=60)

@dp. callback_query_handler(text="f19pro")
async def ninetypro(call: CallbackQuery):
  global photo
  photo = open('PHOTOS/OPPOF19PRO.png', 'rb')
  await call.bot.send_photo(call.message.chat.id, photo, caption='Характеристики:\nПроцессор: 4HM, 2,8ГГЦ\nОперативная память: 12GB\nВстроенная память: 256/512GB\nБатарея: 5000 MA-Ч\nЭкран: 6,8 дюма, AMOLED, 120ГГЦ\nКамера: 108Mn + 13 Mn\nФронтальная камера: 40МП\n\nЦена: 8.000$.',reply_markup=cancelmenu)

  await call.answer(cache_time=60)



@dp.callback_query_handler(text="f17pro")
async def ysevenafrfr(call: CallbackQuery):
  global photo
  photo = open('PHOTOS/OPPOF17PRO.png', 'rb')
  await call.bot.send_photo(call.message.chat.id, photo, caption='Характеристики:\nПроцессор: 4HM, 2,8ГГЦ\nОперативная память: 12GB\nВстроенная память: 256/512GB\nБатарея: 5000 MA-Ч\nЭкран: 6,8 дюма, AMOLED, 120ГГЦ\nКамера: 108Mn + 13 Mn\nФронтальная камера: 40МП\n\nЦена: 6.000$.',reply_markup=cancelmenu)

  await call.answer(cache_time=60)

@dp.callback_query_handler(text="cancel")
async def cancel_buying(call: CallbackQuery):
  await call.message.edit_reply_markup(reply_markup=categoryMenu)
  await call.answer()