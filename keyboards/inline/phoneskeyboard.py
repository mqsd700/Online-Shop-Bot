from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import phones_callback

# 1-usul.
categoryMenu = InlineKeyboardMarkup(
     inline_keyboard=[
    [
        InlineKeyboardButton(text="SAMSUNG", callback_data="samsung"),
        InlineKeyboardButton(text="IPHONE", callback_data="iphone"),
     ],[
        InlineKeyboardButton(text="HUAWEI", callback_data="huawei"),
        InlineKeyboardButton(text="REDMI", callback_data="redmi"),
     ],[
        InlineKeyboardButton(text="OPPO", callback_data="oppo"),

    ],
        [

        InlineKeyboardButton(text="📤Поделиться", switch_inline_query="Hello! this is PRESTIGE ELECTRONICS BOT"),
        ]
     ])
                                            #FOR SAMSUNG PHONES!
samsungMenu = InlineKeyboardMarkup(
     inline_keyboard=[
    [
        InlineKeyboardButton(text="S22 Ultra", callback_data="s22ultra"),
        InlineKeyboardButton(text="S21 Ultra", callback_data="s21ultra"),
    ],[
        InlineKeyboardButton(text="ZFLIP 4", callback_data="zflip4"),
        InlineKeyboardButton(text="A52", callback_data="a52"),
     ], [
        InlineKeyboardButton(text="S10", callback_data="s10"),
         ],
         [
        InlineKeyboardButton(text="🔙Назад", callback_data="cancel")
             ],

     ])

cancelmenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
          InlineKeyboardButton(text="Покупка✅", callback_data="purchase"),
          InlineKeyboardButton(text="Отменить🚫", callback_data="notbuy")
        ],
    ]
)
#                                                FOR IPHONE PHONES!
iphonemenu = InlineKeyboardMarkup(
     inline_keyboard=[
    [
        InlineKeyboardButton(text="14 PRO MAX", callback_data="14promax"),
        InlineKeyboardButton(text="13 PRO MAX", callback_data="13promax"),
    ],[
        InlineKeyboardButton(text="13 MINI", callback_data="13mini"),
        InlineKeyboardButton(text="12 PRO MAX", callback_data="12promax"),
     ], [
        InlineKeyboardButton(text="11 PRO MAX", callback_data="11promax"),
         ],
         [
        InlineKeyboardButton(text="🔙Назад", callback_data="cancel")
            ],

     ])

                         #FOR HUAWEI PHONES!

huaweimenu = InlineKeyboardMarkup(
     inline_keyboard=[
    [
        InlineKeyboardButton(text="P50 PRO", callback_data="p50pro"),
        #InlineKeyboardButton(text="P40 PRO", callback_data="p40pro"),
    ],[
        InlineKeyboardButton(text="Y7 A", callback_data="y7a"),
             ],
         [
        InlineKeyboardButton(text="P40 PRO", callback_data="p40pro"),
         ],

         [
        InlineKeyboardButton(text="🔙Назад", callback_data="cancel")
            ],

     ])


                                   #FOR REDMI PHONES!

redmimenu = InlineKeyboardMarkup(
     inline_keyboard=[
    [
        InlineKeyboardButton(text="11 PRO MAX", callback_data="11promax"),
        #InlineKeyboardButton(text="P40 PRO", callback_data="p40pro"),
    ],[
        InlineKeyboardButton(text="10 PRO MAX", callback_data="10promax"),
             ],
         [
        InlineKeyboardButton(text="9 PRO MAX", callback_data="9promax"),
         ],

         [
        InlineKeyboardButton(text="🔙Назад", callback_data="cancel")
            ],

     ])

                                #FOR OPPO PHONES!

oppomenu = InlineKeyboardMarkup(
     inline_keyboard=[
    [
        InlineKeyboardButton(text="RENO 5", callback_data="reno5"),
        #InlineKeyboardButton(text="P40 PRO", callback_data="p40pro"),
    ],[
        InlineKeyboardButton(text="F19 PRO", callback_data="f19pro"),
             ],
         [
        InlineKeyboardButton(text="F17 PRO", callback_data="f17pro"),
         ],

         [
        InlineKeyboardButton(text="🔙Назад", callback_data="cancel")
            ],

     ])