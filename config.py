# Copyright (c) ShaHm

import os
import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get these values from my.telegram.org/apps.
API_ID = int(getenv("API_ID", "0"))
API_HASH = getenv("API_HASH")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 2000))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "0"))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 6066647930 ))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/abbasghazal/music2",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

CH_US = getenv("CH_US", "lggbg")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL") or f"https://t.me/{CH_US}"
SUPPORT_CHAT = getenv("SUPPORT_CHAT") or f"https://t.me/{CH_US}"
# Display names used by the Arabic play plugins imported from the other project.
BOT_NAME = getenv("BOT_NAME", "بوت")
CHANNEL_NAME = getenv("CHANNEL_NAME", "قناة الدعم")

# Channel username required before users can use bot commands. An empty value falls back to CH_US.
FORCE_SUBSCRIBE_CHANNEL = (getenv("FORCE_SUBSCRIBE_CHANNEL") or CH_US).lstrip("@")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "false").lower() == "true"

# Set bot commands during startup.
SET_CMDS = getenv("SET_CMDS", "true").lower() == "true"


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

# A Netscape-format cookies file exported from a YouTube account.  This is
# needed on many VPS IP addresses, where YouTube asks yt-dlp to verify that it
# is not an automated client.  Leave empty to run without cookies.
#
# Do not commit this file.  The default is already ignored by .gitignore.
YTDLP_COOKIES_FILE = getenv("YTDLP_COOKIES_FILE", "cookies.txt").strip()
if YTDLP_COOKIES_FILE:
    YTDLP_COOKIES_FILE = os.path.abspath(YTDLP_COOKIES_FILE)

# YouTube's default logged-in client may intermittently return "The page needs
# to be reloaded" from VPS IPs.  These clients are the yt-dlp recommended
# fallback for cookie-based extraction.  Set this empty only for debugging.
YTDLP_PLAYER_CLIENT = getenv(
    "YTDLP_PLAYER_CLIENT", "default,web_embedded"
).strip()

# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @T66bot on Telegram
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/de8dc2aef9a2636c6d2a4.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/de8dc2aef9a2636c6d2a4.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/de8dc2aef9a2636c6d2a4.jpg"
STATS_IMG_URL = "https://graph.org/file/de8dc2aef9a2636c6d2a4.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/de8dc2aef9a2636c6d2a4.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/de8dc2aef9a2636c6d2a4.jpg"
STREAM_IMG_URL = "https://graph.org/file/de8dc2aef9a2636c6d2a4.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/de8dc2aef9a2636c6d2a4.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/de8dc2aef9a2636c6d2a4.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/de8dc2aef9a2636c6d2a4.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/de8dc2aef9a2636c6d2a4.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/de8dc2aef9a2636c6d2a4.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
