# Copyright (c) ShaHm

from ZelzalMusic.compat import install_pyrogram_peer_id_fix

# This must run before any Client is created. Pyrogram 2.0.106 otherwise
# rejects channel/supergroup IDs whose numeric part exceeds 32 bits.
install_pyrogram_peer_id_fix()

from ZelzalMusic.core.bot import Zelzaly
from ZelzalMusic.core.dir import dirr
from ZelzalMusic.core.git import git
from ZelzalMusic.core.userbot import Userbot
from ZelzalMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Zelzaly()
userbot = Userbot()

from .utils.inline.styles import install_markup_styles

install_markup_styles()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
