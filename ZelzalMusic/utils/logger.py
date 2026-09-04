# Copyright (c) ShaHm

from pyrogram.enums import ParseMode

from ZelzalMusic import app
from ZelzalMusic.utils.database import is_on_off
from config import LOGGER_ID


async def play_logs(message, streamtype):
    if await is_on_off(2):
        logger_text = f"""
ٴ<b>•────‌‌‏✯ ʑB_ᴍᴜsɪᴄ ✯──‌‌‏─‌‌‏─•</b>
<b>إشعـارات  الميـوزك 𝄞</b>
ٴ<b>•────‌‌‏✯ B_ᴍᴜsɪᴄ ✯──‌‌‏─‌‌‏─•</b>
<b>- سيـدي المطـور 🧑🏻‍💻</b>
<b>- هنـاك شخص يستخـدم الميـوزك حاليـاً 🎻</b>

<b>- الاسم :</b> {message.from_user.mention}
<b>- اليوزر :</b> @{message.from_user.username}
<b>- ايدي المستخدم :</b> <code>{message.from_user.id}</code>

<b>- اسم المجموعة :</b> {message.chat.title}
<b>- يوزر المجموعة :</b> @{message.chat.username}
<b>- ايدي المجموعة :</b> <code>{message.chat.id}</code>

<b>- الطلب :</b> {message.text.split(None, 1)[1]}
<b>- نوع التشغيل :</b> {streamtype}"""
        if message.chat.id != LOGGER_ID:
            try:
                await app.send_message(
                    chat_id=LOGGER_ID,
                    text=logger_text,
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
