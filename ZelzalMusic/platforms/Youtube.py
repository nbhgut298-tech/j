# Copyright (c) ShaHm

import asyncio
import os
import re
import tempfile
from typing import Union

import yt_dlp
from pyrogram.enums import MessageEntityType
from pyrogram.types import Message
from youtubesearchpython.__future__ import VideosSearch

import config
from ZelzalMusic.utils.formatters import time_to_seconds


class YouTubeAPI:
    def __init__(self):
        self.base = "https://www.youtube.com/watch?v="
        self.regex = r"(?:youtube\.com|youtu\.be)"
        self.status = "https://www.youtube.com/oembed?url="
        self.listbase = "https://youtube.com/playlist?list="
        self.reg = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")

    @staticmethod
    def _ydl_options(**options):
        """Return yt-dlp options shared by streams, downloads and playlists."""
        cookiefile = config.YTDLP_COOKIES_FILE
        if cookiefile and os.path.isfile(cookiefile):
            options["cookiefile"] = cookiefile
            clients = [
                client.strip()
                for client in config.YTDLP_PLAYER_CLIENT.split(",")
                if client.strip()
            ]
            if clients:
                options["extractor_args"] = {
                    "youtube": {"player_client": clients}
                }
        options.setdefault("retries", 3)
        options.setdefault("extractor_retries", 3)
        return options

    @staticmethod
    def _clean_link(link: str) -> str:
        return link.split("&", 1)[0]

    async def exists(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        if re.search(self.regex, link):
            return True
        else:
            return False

    async def url(self, message_1: Message) -> Union[str, None]:
        messages = [message_1]
        if message_1.reply_to_message:
            messages.append(message_1.reply_to_message)
        text = ""
        offset = None
        length = None
        for message in messages:
            if offset:
                break
            if message.entities:
                for entity in message.entities:
                    if entity.type == MessageEntityType.URL:
                        text = message.text or message.caption
                        offset, length = entity.offset, entity.length
                        break
            elif message.caption_entities:
                for entity in message.caption_entities:
                    if entity.type == MessageEntityType.TEXT_LINK:
                        return entity.url
        if offset in (None,):
            return None
        return text[offset : offset + length]

    async def details(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        if "&" in link:
            link = link.split("&")[0]
        results = VideosSearch(link, limit=1)
        for result in (await results.next())["result"]:
            title = result["title"]
            duration_min = result["duration"]
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
            vidid = result["id"]
            if str(duration_min) == "None":
                duration_sec = 0
            else:
                duration_sec = int(time_to_seconds(duration_min))
        return title, duration_min, duration_sec, thumbnail, vidid

    async def title(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        if "&" in link:
            link = link.split("&")[0]
        results = VideosSearch(link, limit=1)
        for result in (await results.next())["result"]:
            title = result["title"]
        return title

    async def duration(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        if "&" in link:
            link = link.split("&")[0]
        results = VideosSearch(link, limit=1)
        for result in (await results.next())["result"]:
            duration = result["duration"]
        return duration

    async def thumbnail(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        if "&" in link:
            link = link.split("&")[0]
        results = VideosSearch(link, limit=1)
        for result in (await results.next())["result"]:
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
        return thumbnail

    async def video(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        link = self._clean_link(link)

        def extract_url():
            options = self._ydl_options(
                format="best[height<=720][width<=1280][vcodec!=none][acodec!=none]/best[height<=720][vcodec!=none][acodec!=none]/best",
                quiet=True,
                no_warnings=True,
                geo_bypass=True,
            )
            with yt_dlp.YoutubeDL(options) as ydl:
                info = ydl.extract_info(link, download=False)
                return info["url"]

        try:
            return 1, await asyncio.to_thread(extract_url)
        except Exception as exc:
            return 0, str(exc)

    async def playlist(self, link, limit, user_id, videoid: Union[bool, str] = None):
        if videoid:
            link = self.listbase + link
        link = self._clean_link(link)

        def extract_playlist():
            options = self._ydl_options(
                extract_flat=True, skip_download=True, playlistend=limit,
                ignoreerrors=True, quiet=True, no_warnings=True,
            )
            with yt_dlp.YoutubeDL(options) as ydl:
                info = ydl.extract_info(link, download=False)
            return [entry.get("id") for entry in info.get("entries", []) if entry and entry.get("id")]

        try:
            return await asyncio.to_thread(extract_playlist)
        except Exception:
            return []

    async def track(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        if "&" in link:
            link = link.split("&")[0]
        results = VideosSearch(link, limit=1)
        for result in (await results.next())["result"]:
            title = result["title"]
            duration_min = result["duration"]
            vidid = result["id"]
            yturl = result["link"]
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
        track_details = {
            "title": title,
            "link": yturl,
            "vidid": vidid,
            "duration_min": duration_min,
            "thumb": thumbnail,
        }
        return track_details, vidid

    async def formats(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        if "&" in link:
            link = link.split("&")[0]
        ytdl_opts = self._ydl_options(quiet=True)
        ydl = yt_dlp.YoutubeDL(ytdl_opts)
        with ydl:
            formats_available = []
            r = ydl.extract_info(link, download=False)
            for format in r["formats"]:
                try:
                    str(format["format"])
                except:
                    continue
                if not "dash" in str(format["format"]).lower():
                    try:
                        format["format"]
                        format["filesize"]
                        format["format_id"]
                        format["ext"]
                        format["format_note"]
                    except:
                        continue
                    formats_available.append(
                        {
                            "format": format["format"],
                            "filesize": format["filesize"],
                            "format_id": format["format_id"],
                            "ext": format["ext"],
                            "format_note": format["format_note"],
                            "yturl": link,
                        }
                    )
        return formats_available, link

    async def slider(
        self,
        link: str,
        query_type: int,
        videoid: Union[bool, str] = None,
    ):
        if videoid:
            link = self.base + link
        if "&" in link:
            link = link.split("&")[0]
        a = VideosSearch(link, limit=10)
        result = (await a.next()).get("result")
        title = result[query_type]["title"]
        duration_min = result[query_type]["duration"]
        vidid = result[query_type]["id"]
        thumbnail = result[query_type]["thumbnails"][0]["url"].split("?")[0]
        return title, duration_min, thumbnail, vidid

    async def download(
        self,
        link: str,
        mystic,
        video: Union[bool, str] = None,
        videoid: Union[bool, str] = None,
        songaudio: Union[bool, str] = None,
        songvideo: Union[bool, str] = None,
        format_id: Union[bool, str] = None,
        title: Union[bool, str] = None,
    ) -> str:
        if videoid:
            link = self.base + link
        loop = asyncio.get_running_loop()

        def audio_dl():
            ydl_optssx = self._ydl_options(**{
                "format": "bestaudio/best",
                "outtmpl": "downloads/%(id)s.%(ext)s",
                "geo_bypass": True,
                "nocheckcertificate": True,
                "quiet": True,
                "no_warnings": True,
            })
            x = yt_dlp.YoutubeDL(ydl_optssx)
            info = x.extract_info(link, False)
            xyz = os.path.join("downloads", f"{info['id']}.{info['ext']}")
            if os.path.exists(xyz):
                return xyz
            x.download([link])
            return xyz

        def video_dl():
            temp_dir = os.path.join(tempfile.gettempdir(), "zelzal_music")
            os.makedirs(temp_dir, exist_ok=True)
            ydl_optssx = self._ydl_options(**{
                # Prefer separate high-quality tracks and let ffmpeg merge them.
                # The fallbacks cover videos that expose only combined formats.
                "format": "bv*[height<=720][width<=1280]+ba/b[height<=720]/b",
                "outtmpl": os.path.join(temp_dir, "%(id)s.%(ext)s"),
                "geo_bypass": True,
                "nocheckcertificate": True,
                "quiet": True,
                "no_warnings": True,
                "merge_output_format": "mp4",
                "retries": 5,
                "fragment_retries": 5,
                "socket_timeout": 30,
            })
            with yt_dlp.YoutubeDL(ydl_optssx) as x:
                info = x.extract_info(link, download=True)
                # requested_downloads contains the real path after merging.
                requested = info.get("requested_downloads") or []
                candidates = [item.get("filepath") for item in requested]
                candidates.extend(
                    [
                        info.get("filepath"),
                        os.path.join(temp_dir, f"{info['id']}.mp4"),
                        x.prepare_filename(info),
                    ]
                )
                for candidate in candidates:
                    if candidate and os.path.isfile(candidate):
                        return candidate
            raise RuntimeError("yt-dlp did not produce a playable video file")

        def song_video_dl():
            formats = f"{format_id}+140"
            fpath = f"downloads/{title}"
            ydl_optssx = self._ydl_options(**{
                "format": formats,
                "outtmpl": fpath,
                "geo_bypass": True,
                "nocheckcertificate": True,
                "quiet": True,
                "no_warnings": True,
                "prefer_ffmpeg": True,
                "merge_output_format": "mp4",
            })
            x = yt_dlp.YoutubeDL(ydl_optssx)
            x.download([link])

        def song_audio_dl():
            fpath = f"downloads/{title}.%(ext)s"
            ydl_optssx = self._ydl_options(**{
                "format": format_id,
                "outtmpl": fpath,
                "geo_bypass": True,
                "nocheckcertificate": True,
                "quiet": True,
                "no_warnings": True,
                "prefer_ffmpeg": True,
                "postprocessors": [
                    {
                        "key": "FFmpegExtractAudio",
                        "preferredcodec": "mp3",
                        "preferredquality": "192",
                    }
                ],
            })
            x = yt_dlp.YoutubeDL(ydl_optssx)
            x.download([link])

        if songvideo:
            await loop.run_in_executor(None, song_video_dl)
            fpath = f"downloads/{title}.mp4"
            return fpath
        elif songaudio:
            await loop.run_in_executor(None, song_audio_dl)
            fpath = f"downloads/{title}.mp3"
            return fpath
        elif video:
            # Many YouTube videos no longer expose a combined audio/video URL.
            # Merge both tracks in the operating system's temporary directory;
            # auto_clean removes the result when it leaves the playback queue.
            downloaded_file = await loop.run_in_executor(None, video_dl)
            direct = True
        else:
            # Normal playback is streamed directly.  Explicit song-download
            # commands above still create a file because Telegram needs one.
            def stream_url():
                options = self._ydl_options(
                    format="bestaudio/best", quiet=True, no_warnings=True,
                    geo_bypass=True,
                )
                with yt_dlp.YoutubeDL(options) as ydl:
                    return ydl.extract_info(link, download=False)["url"]

            downloaded_file = await loop.run_in_executor(None, stream_url)
            direct = None
        return downloaded_file, direct
