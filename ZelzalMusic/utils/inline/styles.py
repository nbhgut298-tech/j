# Copyright (c) ShaHm

import asyncio
import json
import inspect

import aiohttp

import config
from ZelzalMusic.logging import LOGGER


def _button_style(button) -> str:
    callback = str(getattr(button, "callback_data", "") or "").lower()
    text = str(getattr(button, "text", "") or "").lower()
    if "stop" in callback or callback == "close" or "اغلاق" in text or "▢" in text:
        return "danger"
    return "primary"


def _styled_markup(buttons):
    rows = []
    for row in buttons:
        styled_row = []
        for button in row:
            item = {"text": button.text, "style": _button_style(button)}
            if button.callback_data:
                item["callback_data"] = button.callback_data
            elif button.url:
                item["url"] = button.url
            elif getattr(button, "user_id", None):
                item["url"] = f"tg://user?id={button.user_id}"
            else:
                # Do not replace a keyboard if a button cannot be represented.
                return None
            styled_row.append(item)
        rows.append(styled_row)
    return {"inline_keyboard": rows}


async def _apply_styles(message, buttons) -> None:
    if not config.BOT_TOKEN or not message:
        return
    markup = _styled_markup(buttons)
    if markup is None:
        return
    payload = {
        "chat_id": message.chat.id,
        "message_id": message.id,
        "reply_markup": json.dumps(markup, ensure_ascii=False),
    }
    endpoint = f"https://api.telegram.org/bot{config.BOT_TOKEN}/editMessageReplyMarkup"
    try:
        timeout = aiohttp.ClientTimeout(total=10)
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.post(endpoint, data=payload) as response:
                result = await response.json(content_type=None)
                description = result.get("description", "unknown error")
                if not result.get("ok") and "not modified" not in description.lower():
                    LOGGER(__name__).warning(
                        "Telegram did not apply player button styles: %s",
                        description,
                    )
    except asyncio.CancelledError:
        # Cancellation is expected while the bot is shutting down.
        return
    except asyncio.TimeoutError:
        # Styling is cosmetic. A slow Bot API request must not make the
        # original Pyrogram send/edit operation look like it failed.
        LOGGER(__name__).debug("Timed out while applying player button styles")
    except aiohttp.ClientError as exc:
        LOGGER(__name__).warning(
            "Unable to apply player button styles (%s): %r",
            type(exc).__name__,
            exc,
        )
    except Exception:
        LOGGER(__name__).exception("Unable to apply player button styles")


async def style_player_markup(message, buttons) -> None:
    """Apply official Bot API colors to a player keyboard."""
    await _apply_styles(message, buttons)


async def style_inline_markup(message, markup) -> None:
    """Apply colors to any Pyrogram inline keyboard."""
    buttons = getattr(markup, "inline_keyboard", None)
    if buttons:
        await _apply_styles(message, buttons)


async def edit_styled_markup(message, markup_or_buttons) -> None:
    """Replace an existing keyboard without a colourless intermediate frame."""
    buttons = getattr(markup_or_buttons, "inline_keyboard", markup_or_buttons)
    if buttons:
        await _apply_styles(message, buttons)


def _message_from_result(result, owner):
    if getattr(result, "chat", None) and getattr(result, "id", None):
        return result
    if getattr(owner, "chat", None) and getattr(owner, "id", None):
        return owner
    return getattr(owner, "message", None)


def _wrap_markup_method(owner_class, method_name) -> None:
    original = getattr(owner_class, method_name, None)
    if original is None or getattr(original, "_shahm_styled", False):
        return
    signature = inspect.signature(original)

    async def wrapped(*args, __original=original, __signature=signature, **kwargs):
        bound = __signature.bind_partial(*args, **kwargs)
        markup = bound.arguments.get("reply_markup")
        result = await __original(*bound.args, **bound.kwargs)
        if markup is not None:
            await style_inline_markup(_message_from_result(result, args[0]), markup)
        return result

    wrapped._shahm_styled = True
    setattr(owner_class, method_name, wrapped)


def install_markup_styles() -> None:
    """Color every inline keyboard sent or edited through Pyrogram."""
    from pyrogram import Client
    from pyrogram.types import CallbackQuery, Message

    for method in (
        "send_message", "send_photo", "send_audio", "send_video", "send_document",
        "send_animation", "send_voice", "send_sticker",
    ):
        _wrap_markup_method(Client, method)
    for method in (
        "reply_text", "reply_photo", "reply_audio", "reply_video", "reply_document",
        "reply_animation", "edit_text", "edit_caption", "edit_media", "edit_reply_markup",
    ):
        _wrap_markup_method(Message, method)
    for method in (
        "edit_message_text", "edit_message_caption", "edit_message_media",
        "edit_message_reply_markup",
    ):
        _wrap_markup_method(CallbackQuery, method)
