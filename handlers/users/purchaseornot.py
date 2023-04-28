from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from handlers.users.contacthandler import keyboard


from loader import dp





@dp.callback_query_handler(text="purchase") #ASKING CONTACT
async def show_contact_keys(call: CallbackQuery):
  await call.message.answer(text="Отправьте свой Контакт👇", reply_markup=keyboard)

@dp.message_handler(content_types='contact')
async def get_contact(message: Message):
  contact = message.contact
  await message.answer(f"Спасибо {message.from_user.full_name}!\n"
    f"{contact.phone_number} телефон номер был принят.\nCотрудники скоро свяжутся с вами☺️",reply_markup=ReplyKeyboardRemove())


@dp.callback_query_handler(text="notbuy") #CANCELLING
async def show_contact_keys(call: CallbackQuery):
  await call.message.answer(text="Ваш заказ Отменено.", reply_markup=ReplyKeyboardRemove())