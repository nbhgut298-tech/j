# Copyright (c) ShaHm

from pyrogram import StopPropagation, filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

import config
from ZelzalMusic import app
from ZelzalMusic.logging import LOGGER


MEMBER_STATUSES = {
    ChatMemberStatus.OWNER,
    ChatMemberStatus.ADMINISTRATOR,
    ChatMemberStatus.MEMBER,
}

@app.on_message(filters.text & ~filters.via_bot, group=-1)
async def force_subscribe(_, message: Message):
    """Block all text commands until the sender joins the configured channel."""
    if (
        not message.from_user
        or not config.FORCE_SUBSCRIBE_CHANNEL
    ):
        return

    try:
        member = await app.get_chat_member(
            config.FORCE_SUBSCRIBE_CHANNEL, message.from_user.id
        )
        if member.status in MEMBER_STATUSES:
            return
    except UserNotParticipant:
        pass
    except Exception:
        LOGGER(__name__).exception("Unable to check force-subscribe membership")
        await message.reply_text(
            "تعذر التحقق من الاشتراك. تأكد من إضافة البوت مشرفاً في قناة الاشتراك الإجباري."
        )
        raise StopPropagation

    channel_url = f"https://t.me/{config.FORCE_SUBSCRIBE_CHANNEL}"
    keyboard = InlineKeyboardMarkup(
        [[InlineKeyboardButton("اشترك بالقناة", url=channel_url)]]
    )
    await message.reply_text(
        "يجب الاشتراك في القناة أولاً لاستخدام أوامر البوت.",
        reply_markup=keyboard,
    )
    raise StopPropagation
