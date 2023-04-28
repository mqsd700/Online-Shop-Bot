from aiogram.dispatcher.filters.state import StatesGroup, State
class PersonalData(StatesGroup):
    fullname = State()
    phoneNum = State()
    tgusername = State()
    location = State()
