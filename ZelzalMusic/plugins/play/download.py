"""Compatibility aliases for the safe YouTube search downloader."""

from pyrogram.types import Message

from ZelzalMusic import app
from ZelzalMusic.plugins.play.filters import command
from ZelzalMusic.plugins.play.بحث import song_downloader


@app.on_message(command(["song", "music"]))
async def legacy_song_downloader(client, message: Message):
    await song_downloader(client, message)
