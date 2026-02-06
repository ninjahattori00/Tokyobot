import re
import os
from os import environ, getenv
from Script import script

# Utility functions
id_pattern = re.compile(r'^.\d+$')

def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# ============================
# Bot Information Configuration
# ============================
SESSION = environ.get('SESSION', 'royal_search')
API_ID = int(environ.get('API_ID', ''))
API_HASH = environ.get('API_HASH', '')
BOT_TOKEN = environ.get('BOT_TOKEN', "")

# ============================
# Bot Settings Configuration
# ============================
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))
INDEX_CAPTION = bool(environ.get('SAVE_CAPTION', True))

# ============================
# Images & Visuals
# ============================
PICS = [environ.get('PICS', 'https://ibb.co/zHjmmDfy')]  # Intro image replaced
NOR_IMG = environ.get("NOR_IMG", "https://t.me/tokyohdseries")
MELCOW_PHOTO = environ.get("MELCOW_PHOTO", "https://t.me/tokyohdseries")
SPELL_IMG = environ.get("SPELL_IMG", "https://t.me/tokyohdseries")
SUBSCRIPTION = environ.get('SUBSCRIPTION', 'https://t.me/UPROFESESR')
FSUB_PICS = [environ.get('FSUB_PICS', 'https://t.me/movieiuniverse https://t.me/UPROFESESR')]  # Two Fsub pics

# ============================
# Admin, Channels & Users Configuration
# ============================
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-100').split()]

LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-100'))
BIN_CHANNEL = int(environ.get('BIN_CHANNEL', '-100'))
PREMIUM_LOGS = int(environ.get('PREMIUM_LOGS', '-100'))
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '-100').split()]
support_chat_id = environ.get('SUPPORT_CHAT_ID', '-100')
reqst_channel = environ.get('REQST_CHANNEL_ID', '-100')
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://t.me/tokyohdseries')

auth_req_channels = environ.get("AUTH_REQ_CHANNELS", "-100")
auth_channels = environ.get("AUTH_CHANNELS", "-100")

# ============================
# Payment Configuration
# ============================
QR_CODE = environ.get('QR_CODE', 'Your_Qr_Code')
OWNER_UPI_ID = environ.get('OWNER_UPI_ID', 'ɴᴏ ᴀᴠᴀɪʟᴀʙʟᴇ ʀɪɢʜᴛ ɴᴏᴡ')

STAR_PREMIUM_PLANS = {10: "7day", 20: "15day", 40: "1month", 55: "45day", 75: "60day"}

# ============================
# MongoDB Configuration
# ============================
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'royal_files')
MULTIPLE_DB = is_enabled(os.environ.get('MULTIPLE_DB', "False"), False)
DATABASE_URI2 = environ.get('DATABASE_URI2', "")

# ============================
# Movie Notification & Update Settings
# ============================
MOVIE_UPDATE_NOTIFICATION = bool(environ.get('MOVIE_UPDATE_NOTIFICATION', False))
MOVIE_UPDATE_CHANNEL = int(environ.get('MOVIE_UPDATE_CHANNEL', '-100'))
DREAMXBOTZ_IMAGE_FETCH = bool(environ.get('DREAMXBOTZ_IMAGE_FETCH', True))
LINK_PREVIEW = bool(environ.get('LINK_PREVIEW', False))
ABOVE_PREVIEW = bool(environ.get('ABOVE_PREVIEW', True))
TMDB_API_KEY = environ.get('TMDB_API_KEY', '')
TMDB_POSTER = bool(environ.get('TMDB_POSTER', False))
LANDSCAPE_POSTER = bool(environ.get('LANDSCAPE_POSTER', True))

# ============================
# Verification Settings
# ============================
IS_VERIFY = is_enabled(environ.get('IS_VERIFY', 'False'), False)
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '-100'))
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', '-100'))
VERIFY_IMG = environ.get("VERIFY_IMG", "https://telegra.ph/file/9ecc5d6e4df5b83424896.jpg")

TUTORIAL = environ.get("TUTORIAL", "https://t.me/UPROFESESR")
TUTORIAL_2 = environ.get("TUTORIAL_2", "https://t.me/UPROFESESR")
TUTORIAL_3 = environ.get("TUTORIAL_3", "https://t.me/UPROFESESR")

SHORTENER_API = environ.get("SHORTENER_API", "2469484d258897da1dc9edaf4face6f466301f39")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", "https://t.me/tokyohdseries")

SHORTENER_API2 = environ.get("SHORTENER_API2", "yei5ei5eie6id6d")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", "https://t.me/tokyohdseries")

SHORTENER_API3 = environ.get("SHORTENER_API3", "5353e68e866ee")
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", "https://t.me/tokyohdseries")

TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "1200"))
THREE_VERIFY_GAP = int(environ.get('THREE_VERIFY_GAP', "54000"))

# ============================
# Channel & Group Links
# ============================
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/tokyohdseries')
OWNER_LNK = environ.get('OWNER_LNK', 'https://t.me/UPROFESESR')
UPDATE_CHNL_LNK = environ.get('UPDATE_CHNL_LNK', 'https://t.me/movieiuniverse')

# ============================
# Captions / IMDB Template
# ============================
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "https://t.me/tokyohdseries")
BATCH_FILE_CAPTION = CUSTOM_FILE_CAPTION
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "https://t.me/tokyohdseries")

# ============================
# Bot Users Configuration
# ============================
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
PREMIUM_USER = [int(user) if id_pattern.search(user) else user for user in environ.get('PREMIUM_USER', '').split()]

# ============================
# Miscellaneous
# ============================
ULTRA_FAST_MODE = is_enabled(environ.get('ULTRA_FAST_MODE', "False"), True)
MAX_B_TN = environ.get("MAX_B_TN", "5")
PORT = int(environ.get("PORT", "8080"))
MSG_ALRT = environ.get('MSG_ALRT', 'Share & Support Us ♥️')
DELETE_TIME = int(environ.get("DELETE_TIME", "300"))
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", True))
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "False")), False)
TMDB_ON_SEARCH = is_enabled((environ.get('TMDB_ON_SEARCH', "False")), False)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "False")), False)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PM_SEARCH = bool(environ.get('PM_SEARCH', True))
EMOJI_MODE = bool(environ.get('EMOJI_MODE', False))
BUTTON_MODE = is_enabled((environ.get('BUTTON_MODE', "False")), False)
STREAM_MODE = bool(environ.get('STREAM_MODE', False))
PREMIUM_STREAM_MODE = bool(environ.get('PREMIUM_STREAM_MODE', False))

# ============================
# Bot Commands
# ============================
Bot_cmds = {
    "start": "Sᴛᴀʀᴛ Mᴇ Bᴀʙʏ",
    "stats": "Gᴇᴛ Bᴏᴛ Sᴛᴀᴛs",
    "alive": " Cʜᴇᴄᴋ Bᴏᴛ Aʟɪᴠᴇ ᴏʀ Nᴏᴛ ",
    "settings": "ᴄʜᴀɴɢᴇ sᴇᴛᴛɪɴɢs",
    "id": "ɢᴇᴛ ɪᴅ ᴛᴇʟᴇɢʀᴀᴍ ",
    "info": "Gᴇᴛ Usᴇʀ ɪɴғᴏ ",
}
