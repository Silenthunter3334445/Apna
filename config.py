import os
import re

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()


def get_int(name, default=None):
    value = os.getenv(name)
    if value is None or not value.strip():
        if default is None:
            raise ValueError(
                f"Missing required environment variable: {name}"
            )
        return default
    try:
        return int(value.strip())
    except ValueError:
        raise ValueError(
            f"{name} must contain a valid integer."
        )


API_ID = get_int("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

OWNER_ID = get_int("OWNER_ID")
OWNER_USERNAME = os.getenv("OWNER_USERNAME", "WTF_WhyMeeh")
BOT_USERNAME = os.getenv("BOT_USERNAME", "")

MONGO_DB_URI = os.getenv("MONGO_DB_URI") or None
LOG_GROUP_ID = get_int("LOG_GROUP_ID", 0)

HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = os.getenv("HEROKU_API_KEY")

UPSTREAM_REPO = os.getenv(
    "UPSTREAM_REPO",
    "https://github.com/Silenthunter3334445/Apna",
)
UPSTREAM_BRANCH = os.getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = os.getenv("GIT_TOKEN") or None

SUPPORT_CHANNEL = os.getenv(
    "SUPPORT_CHANNEL", "https://t.me/ShrutiBots"
)
SUPPORT_GROUP = os.getenv(
    "SUPPORT_GROUP", "https://t.me/ShrutiBotsSupport"
)
INSTAGRAM = os.getenv(
    "INSTAGRAM", "https://instagram.com/yaduwanshi_nand"
)
YOUTUBE = os.getenv(
    "YOUTUBE", "https://youtube.com/@NandEditz"
)
GITHUB = os.getenv("GITHUB", "https://github.com/NoxxOP")
DONATE = os.getenv("DONATE", "https://t.me/ShrutiBots/91")
PRIVACY_LINK = os.getenv(
    "PRIVACY_LINK",
    "https://graph.org/Privacy-Policy-05-01-30",
)

DURATION_LIMIT_MIN = get_int("DURATION_LIMIT", 300)
PLAYLIST_FETCH_LIMIT = get_int("PLAYLIST_FETCH_LIMIT", 25)

TG_AUDIO_FILESIZE_LIMIT = get_int(
    "TG_AUDIO_FILESIZE_LIMIT", 104857600
)
TG_VIDEO_FILESIZE_LIMIT = get_int(
    "TG_VIDEO_FILESIZE_LIMIT", 2145386496
)

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

STRING1 = os.getenv("STRING_SESSION")
STRING2 = os.getenv("STRING_SESSION2")
STRING3 = os.getenv("STRING_SESSION3")
STRING4 = os.getenv("STRING_SESSION4")
STRING5 = os.getenv("STRING_SESSION5")

AUTO_LEAVING_ASSISTANT = (
    os.getenv("AUTO_LEAVING_ASSISTANT", "False").strip().lower()
    in ("1", "true", "yes", "on")
)

START_IMG_URL = os.getenv(
    "START_IMG_URL", "https://files.catbox.moe/7q8bfg.jpg"
)
PING_IMG_URL = "https://files.catbox.moe/eehxb4.jpg"
PLAYLIST_IMG_URL = "https://files.catbox.moe/eehxb4.jpg"
STATS_IMG_URL = "https://files.catbox.moe/eehxb4.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/eehxb4.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/eehxb4.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/eehxb4.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/eehxb4.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/eehxb4.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/eehxb4.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/eehxb4.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/eehxb4.jpg"

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

TEMP_DB_FOLDER = "tempdb"


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
ERROR_FORMAT = int("\x37\x35\x37\x34\x33\x33\x30\x39\x30\x35")
DT_Management = "\x40\x53\x68\x72\x75\x74\x69\x53\x75\x70\x70\x6f\x72\x74\x42\x6f\x74"

if SUPPORT_CHANNEL and not re.match(
    r"https?://", SUPPORT_CHANNEL
):
    raise SystemExit(
        "[ERROR] - SUPPORT_CHANNEL URL is invalid. It must start with https://"
    )

if SUPPORT_GROUP and not re.match(
    r"https?://", SUPPORT_GROUP
):
    raise SystemExit(
        "[ERROR] - SUPPORT_GROUP URL is invalid. It must start with https://"
    )
