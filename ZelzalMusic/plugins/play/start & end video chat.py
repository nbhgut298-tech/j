# Copyright (c) ShaHm

from pyrogram import Client, filters
from pyrogram.types import Message
from ZelzalMusic import app
# vc on
@app.on_message(filters.video_chat_started)
async def zed(_, msg):
       await msg.reply("<b>↞ فتحوا المكالمه اللي وده يسمعنا صوته يصعد 🦦</b>")
# vc off
@app.on_message(filters.video_chat_ended)
async def zed2(_, msg):
       await msg.reply("<b>المكالمه تقفلت ↞ أصواتكم كانت تفتح النفس 🍧🙊</b>")

# invite members on vc
@app.on_message(filters.video_chat_members_invited)
async def zed3(client, message):
           text = f"↞ هالحلو يبيك : {message.from_user.mention}"
           x = 0
           for user in message.video_chat_members_invited.users:
             try:
               text += f"\n↞ تعال يا حلو للمكالمه : <a href='tg://user?id={user.id}'>{user.first_name}</a>"
               x += 1
             except Exception:
               pass
           try:
             await message.reply(text)
           except:
             pass