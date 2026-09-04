import asyncio

import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZelzalMusic import Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app
from config import SUPPORT_CHANNEL
from random import  choice, randint

# 𝐃𝐞𝐩𝐥𝐨𝐲𝐞𝐝 ⛥ 𓏺 Yousef .tele_https://t.me/y_o_v
                
@app.on_message(
    command(["سورس", "السورس"]) | filters.regex(r"^• السورس •$")
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://forkgraph.zaid.pro/file/mZMkbE56phEY",
        caption = "<b>مرحبًا بك في سورس البوت</b>",
reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                         "قناة الدعم", url=SUPPORT_CHANNEL),
                 ],[
                   InlineKeyboardButton(
                        "السورس", url=SUPPORT_CHANNEL),
                ],

            ]

        ),

    )
