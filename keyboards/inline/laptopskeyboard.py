from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import phones_callback

# 1-usul.
laptopsMenu = InlineKeyboardMarkup(
     inline_keyboard=[
    [
        InlineKeyboardButton(text="HP", callback_data="hp"),
        #InlineKeyboardButton(text="IPHONE", callback_data="iphone"),
     ],[
        InlineKeyboardButton(text="ACER", callback_data="acer"),

     ],[
        InlineKeyboardButton(text="LENOVO", callback_data="lenovo"),

    ],
        [

        InlineKeyboardButton(text="📤Поделиться", switch_inline_query=" Hello! this is PRESTIGE ELECTRONICS BOT"),
        ]
     ])


                 #FOR ALL LAPTOPS!

hpmenu = InlineKeyboardMarkup(
     inline_keyboard=[
    [
        InlineKeyboardButton(text="OMEN", callback_data="omen"),
        #InlineKeyboardButton(text="P40 PRO", callback_data="p40pro"),
    ],[
        InlineKeyboardButton(text="PAVILION", callback_data="pavilion"),
             ],
         [
        InlineKeyboardButton(text="PROBOOK", callback_data="probook"),
         ],

         [
        InlineKeyboardButton(text="🔙Назад", callback_data="cancel1")
            ],

     ])

                                      #FOR ACER LAPTOPS!

acermenu = InlineKeyboardMarkup(
     inline_keyboard=[
    [
        InlineKeyboardButton(text="NITRO", callback_data="nitro"),
        #InlineKeyboardButton(text="P40 PRO", callback_data="p40pro"),
    ],[
        InlineKeyboardButton(text="PREDATOR", callback_data="predator"),
             ],
         [
        InlineKeyboardButton(text="ASPIRE", callback_data="aspire"),
         ],

         [
        InlineKeyboardButton(text="🔙Назад", callback_data="cancel1")
            ],

     ])


            #FOR LENOVO LAPTOPS!

lenovomenu = InlineKeyboardMarkup(
     inline_keyboard=[
    [
        InlineKeyboardButton(text="LEGION", callback_data="legion"),
        #InlineKeyboardButton(text="P40 PRO", callback_data="p40pro"),
    ],[
        InlineKeyboardButton(text="IDEAPAD", callback_data="ideapad"),
             ],
         [
        InlineKeyboardButton(text="THINKPAD", callback_data="thinkpad"),
         ],

         [
        InlineKeyboardButton(text="🔙Назад", callback_data="cancel1")
            ],

     ])