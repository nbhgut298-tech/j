import os
import asyncio
import requests
import config
import random
import time
from config import START_IMG_URL
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InputMediaPhoto,
    Message,
)
from strings.filters import command
from ZelzalMusic.utils.decorators import AdminActual
from ZelzalMusic import Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app
from random import  choice, randint
#اتار.ي
lnk= "" +config.SUPPORT_CHANNEL
chat_scope = filters.private | filters.group

REPLY_MESSAGE = "<b>- اهلا بك عزيزي اليك قائمة اوامر التسلية .\n- اصدار السورس ~ 5.8V .\n- اصدار الكيبورد ~ 5.8V .</b>"

#اتاري
#v..vi.zi.n.n

REPLY_MESSAGE_BUTTONS = [

          [

             ("• مطور البوت •"),

             ("• مطور السورس •")
          ],

          [

             ("• السورس •"),

             ("• الاوامر •")

          ],

          [

             ("• افتارات سينمائية •"),

             ("• اقتباسات •")

          ],

          [

             ("• افتارات شباب •"),

             ("• افتارات بنات •")

          ],

          [

             ("• هيدرات •"),

             ("• متحركة •")

          ],
    
          [

            ("• جداريات •"),

            ("• لوكيت •")
  #ا..تاري
#v..v....i.zi..n.n            
          ],
          [
            ("• افتارات سينمائية •"),

            ("• افتارات فنانين •")
              
          ],
          [
            ("• افلام •"),

            ("• قيفات كوكسال •")
              
          ],
          [
            ("• قيفات شباب •"),

            ("• قيفات بنات •")
              
          ],
          [
            ("• قيفات قطط •"),

            ("• قيفات اطفال •")
              
          ],
          [
            ("• قيفات رومانسية •"),

            ("• قيفات كيبوب •")
          ],
          [
             ("• ستوري •"),

             ("• راب •")
          ],
          [
             ("• فيديو •"),

             ("• ريمكس •")
          ],
          [
             ("• فويز •"),
             ("• اخفاء الكيبورد •")

          ]

]

@app.on_message(filters.regex(r"^(?:/cmd|cmd|كيب)$") & chat_scope)
async def cpanel(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )

@app.on_message(filters.regex("• اخفاء الكيبورد •") & chat_scope)
async def down(client, message):
          m = await message.reply("<b>- تم اغلاق الكيبورد .</b>", reply_markup= ReplyKeyboardRemove(selective=True))
