import asyncio
import html
import os
import tempfile

import yt_dlp
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtube_search import YoutubeSearch

import config
from strings.filters import command
from ZelzalMusic import app


def _download_audio(link: str, output_dir: str):
    options = {
        "format": "bestaudio[ext=m4a]/bestaudio",
        "outtmpl": os.path.join(output_dir, "%(id)s.%(ext)s"),
        "restrictfilenames": True,
        "noplaylist": True,
        "quiet": True,
        "no_warnings": True,
    }
    if config.YTDLP_COOKIES_FILE and os.path.isfile(config.YTDLP_COOKIES_FILE):
        options["cookiefile"] = config.YTDLP_COOKIES_FILE
        clients = [
            client.strip()
            for client in config.YTDLP_PLAYER_CLIENT.split(",")
            if client.strip()
        ]
        if clients:
            options["extractor_args"] = {"youtube": {"player_client": clients}}
    options["retries"] = 3
    options["extractor_retries"] = 3
    with yt_dlp.YoutubeDL(options) as ydl:
        info = ydl.extract_info(link, download=True)
        requested = info.get("requested_downloads") or []
        filepath = requested[0].get("filepath") if requested else None
        return info, filepath or ydl.prepare_filename(info)


@app.on_message(command(["يوت", "نزل", "بحث"]))
async def song_downloader(client, message: Message):
    query = " ".join(message.command[1:]).strip()
    if not query:
        return await message.reply_text("<b>اكتب اسم المقطع بعد أمر بحث.</b>")

    status = await message.reply_text("<b>⇜ جارِ البحث...</b>")
    try:
        results = await asyncio.to_thread(
            lambda: YoutubeSearch(query, max_results=1).to_dict()
        )
        if not results:
            return await status.edit("<b>لم يتم العثور على نتائج.</b>")

        link = f"https://youtube.com{results[0]['url_suffix']}"
        await status.edit("<b>⇜ جارِ تحميل المقطع...</b>")

        os.makedirs("downloads", exist_ok=True)
        with tempfile.TemporaryDirectory(prefix="search_", dir="downloads") as temp_dir:
            info, audio_file = await asyncio.to_thread(_download_audio, link, temp_dir)
            if not audio_file or not os.path.isfile(audio_file):
                raise FileNotFoundError("لم يُنشأ ملف الصوت بعد التنزيل")

            await message.reply_audio(
                audio=audio_file,
                caption=f"ᏟᎻᎪΝΝᎬᏞ 𓏺 @{config.CH_US}",
                title=str(info.get("title") or results[0]["title"])[:64],
                performer=str(info.get("uploader") or "YouTube")[:64],
                duration=int(info.get("duration") or 0),
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton("قناة الدعم", url=config.SUPPORT_CHANNEL)]]
                ),
            )
        await status.delete()
    except Exception as exc:
        error = html.escape(str(exc)[:250])
        await status.edit(f"<b>تعذر تحميل المقطع:</b> <code>{error}</code>")
