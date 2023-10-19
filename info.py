import re, os
from os import environ
import asyncio
import json
from collections import defaultdict
from typing import Dict, List, Union
from pyrogram import Client
from time import time

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.strip().lower() in ["on", "true", "yes", "1", "enable", "y"]:
        return True
    elif value.strip().lower() in ["off", "false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


# Bot information
PORT = environ.get("PORT", "8080")
WEBHOOK = bool(environ.get("WEBHOOK", True)) # for web support on/off
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', ''))
API_HASH = environ.get('API_HASH', '')
BOT_TOKEN = environ.get('BOT_TOKEN', "")


# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))
PICS = (environ.get('PICS' ,'https://graph.org/file/01ddfcb1e8203879a63d7.jpg https://graph.org/file/d69995d9846fd4ad632b8.jpg https://graph.org/file/a125497b6b85a1d774394.jpg https://graph.org/file/43d26c54d37f4afb830f7.jpg https://graph.org/file/60c1adffc7cc2015f771c.jpg https://graph.org/file/d7b520240b00b7f083a24.jpg https://graph.org/file/0f336b0402db3f2a20037.jpg https://graph.org/file/39cc4e15cad4519d8e932.jpg https://graph.org/file/d59a1108b1ed1c6c6c144.jpg https://te.legra.ph/file/3a4a79f8d5955e64cbb8e.jpg https://graph.org/file/d69995d9846fd4ad632b8.jpg')).split()
BOT_START_TIME = time()

NOR_IMG = environ.get("NOR_IMG", "https://te.legra.ph/file/a27dc8fe434e6b846b0f8.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://graph.org/file/8a567f3ad1905a75298cc.mp4")
SPELL_IMG = environ.get("SPELL_IMG", "https://graph.org/file/2be2ef024a5bbf336b7d5.jpg")


# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '0').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '0').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '0').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
PREMIUM_USER = [int(user) if id_pattern.search(user) else user for user in environ.get('PREMIUM_USER', '6433510598').split()]
auth_channel = environ.get('AUTH_CHANNEL','')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', " ")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

#maximum search result buttos count in number#
MAX_RIST_BTNS = int(environ.get('MAX_RIST_BTNS', "10"))
START_MESSAGE = environ.get('START_MESSAGE', '<b>ʜᴇʏ,  {user}\n\nɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴍᴏᴠɪᴇꜱ ᴊᴜꜱᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ</b>')
BUTTON_LOCK_TEXT = environ.get("BUTTON_LOCK_TEXT", "ᴏʏᴇ {𝙦𝙪𝙚𝙧𝙮}! \nʀᴇQᴜᴇꜱᴛ ʏᴏᴜʀ ᴏᴡɴ ᴍᴏᴠɪᴇ 🎥")
FORCE_SUB_TEXT = environ.get('FORCE_SUB_TEXT', 'ᴊᴏɪɴ ᴍʏ ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜꜱᴇ ᴍᴇ 🥳')
RemoveBG_API = environ.get("RemoveBG_API", "")
WELCOM_PIC = environ.get("WELCOM_PIC", "https://graph.org/file/d69995d9846fd4ad632b8.jpg")
WELCOM_TEXT = environ.get("WELCOM_TEXT", "👋 𝐎𝐲𝐞 {user} \nᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {chat}🌹\n\nꜱᴇɴᴅ ᴍᴇ ᴀɴʏ ᴍᴏᴠɪᴇ ɴᴀᴍᴇ ɪ ᴡɪʟʟ ɢɪᴠᴇ ᴛʜᴀʏ ᴍᴏᴠɪᴇ 🎥😁")
PMFILTER = is_enabled(environ.get('PMFILTER', "True"), True)
G_FILTER = is_enabled(environ.get("G_FILTER", "True"), True)
BUTTON_LOCK = is_enabled(environ.get("BUTTON_LOCK", "False"), False)

# url shortner
SHORT_URL = environ.get("SHORT_URL")
SHORT_API = environ.get("SHORT_API")

# Others
VERIFY = bool(environ.get('VERIFY', False))
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'ziplinker.net')
SHORTLINK_API = environ.get('SHORTLINK_API', 'b13a8022cb09d3a1dd7b40f251e5cc306099dfb4')
SECOND_SHORTLINK_URL = environ.get('SECOND_SHORTLINK_URL', 'ziplinker.net')
SECOND_SHORTLINK_API = environ.get('SECOND_SHORTLINK_API', 'b13a8022cb09d3a1dd7b40f251e5cc306099dfb4')
IS_SHORTLINK = bool(environ.get('IS_SHORTLINK', True))
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]
MAX_B_TN = environ.get("MAX_B_TN", "5")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/+z2b3yBUUMf80NWVl')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/Thunnder_Bot')
TUTORIAL = environ.get('TUTORIAL', 'https://t.me/MS_Mihir/17')
IS_TUTORIAL = bool(environ.get('IS_TUTORIAL', True))
MSG_ALRT = environ.get('MSG_ALRT', 'ᴡᴀɪᴛ ɪ ᴀᴍ ꜱʟɪɢʜᴛʟʏ ʙᴜꜱʏ')
IMDB_DELET_TIME = int(environ.get('IMDB_DELET_TIME', "300"))
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '0'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'MS_Movvis')
P_TTI_SHOW_OFF = is_enabled(environ.get('P_TTI_SHOW_OFF', "False"), False)
PM_IMDB = is_enabled(environ.get('PM_IMDB', "False"), False)
IMDB = is_enabled(environ.get('IMDB', "False"), False)
SINGLE_BUTTON = is_enabled(environ.get('SINGLE_BUTTON', "True"), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "🗄️ ᴍᴏᴠɪᴇ : {file_name}\n\n🥀 sɪᴢᴇ : {file_size}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", None)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>📛 𝐍𝐚𝐦𝐞 : {query}</b> \n‌\n🏷 𝐓𝐢𝐭𝐥𝐞 : <a href={url}>{title}</a>\n🎭 𝐆𝐞𝐧𝐫𝐞𝐬 : {genres}\n📆 𝐑𝐞𝐥𝐞𝐚𝐬𝐞 : <a href={url}/releaseinfo>{year}</a>\n🌟 𝐑𝐚𝐭𝐢𝐧𝐠 : <a href={url}/ratings>{rating}</a> / 10")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '0')).split()]
MELCOW_NEW_USERS = is_enabled(environ.get('MELCOW_NEW_USERS', "True"), True)
PROTECT_CONTENT = is_enabled(environ.get('PROTECT_CONTENT', "False"), False)
PUBLIC_FILE_STORE = is_enabled(environ.get('PUBLIC_FILE_STORE', "True"), True)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)




BLACKLIST_WORDS = (
    list(os.environ.get("BLACKLIST_WORDS").split(","))
    if os.environ.get("BLACKLIST_WORDS")
    else []
)

BLACKLIST_WORDS = ["@BM Links", "[BindasMovies]", "[Hezz Movies]", "www Tamilblasters rent", "E4E", "[D&O]", "[MM]", "[", "]", "[FC]", "[CF]", "LinkZz", "[DFBC]", "@New_Movie", "@Infinite_Movies2", "MM", "@R A R B G", "[F&T]", "[KMH]", "[DnO]", "[F&T]", "MLM", "@TM_LMO", "@x265_E4E", "@HEVC MoviesZ", "SSDMovies", "@MM Linkz", "[CC]", "@Mallu_Movies", "@DK Drama", "@luxmv_Linkz", "@Akw_links", "CK HEVC", "@Team_HDT", "[CP]", "www 1TamilMV men", "www TamilRockers", "@MM", "@mm", "[MW]", "@TN68 Linkzz", "@Clipmate_Movie", "[MASHOBUC]", "Official TheMoviesBoss", "www CineVez one", "www 7MovieRulz lv", "www 1TamilMV vip", "[SMM Official]"]

LANGUAGES = ["malayalam", "mal", "tamil", "tam" ,"english", "eng", "hindi", "hin", "telugu", "tel", "kannada", "kan"]

SEASONS = ["season 1" , "season 2" , "season 3" , "season 4", "season 5" , "season 6" , "season 7" , "season 8" , "season 9" , "season 10"]



LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
