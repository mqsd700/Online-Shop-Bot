from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import phones_callback

# 1-usul.
householdsMenu = InlineKeyboardMarkup(
     inline_keyboard=[
    [
        InlineKeyboardButton(text="Микроволновки", callback_data="mk"),
        #InlineKeyboardButton(text="IPHONE", callback_data="iphone"),
     ],[
        InlineKeyboardButton(text="Пылесосы", callback_data="pl"),

     ],[
        InlineKeyboardButton(text="Холодильники", callback_data="xl"),

    ],
        [

        InlineKeyboardButton(text="📤Поделиться", switch_inline_query="Hello!  this is PRESTIGE ELECTRONICS BOT"),
        ]
     ])


mkmenu = InlineKeyboardMarkup(
     inline_keyboard=[
    [
        InlineKeyboardButton(text="SAMSUNG", callback_data="slmsung"),
        #InlineKeyboardButton(text="P40 PRO", callback_data="p40pro"),
    ],[
        InlineKeyboardButton(text="PANASONIC", callback_data="panasonic"),
             ],


         [
        InlineKeyboardButton(text="🔙Назад", callback_data="cancel2")
            ],

     ])



               #FOR PILESOSI

plmenu = InlineKeyboardMarkup(
     inline_keyboard=[
    [
        InlineKeyboardButton(text="DYSON", callback_data="dyson"),
        #InlineKeyboardButton(text="P40 PRO", callback_data="p40pro"),
    ],[
        InlineKeyboardButton(text="LG", callback_data="lg"),
             ],


         [
        InlineKeyboardButton(text="🔙Назад", callback_data="cancel2")
            ],

     ])


                        #FOR XOLODILNIKI


xlmenu = InlineKeyboardMarkup(
     inline_keyboard=[
    [
        InlineKeyboardButton(text="HITACHI", callback_data="hitachi"),
        #InlineKeyboardButton(text="P40 PRO", callback_data="p40pro"),
    ],[
        InlineKeyboardButton(text="BOSCH", callback_data="bosch"),
             ],


         [
        InlineKeyboardButton(text="🔙Назад", callback_data="cancel2")
            ],

     ])