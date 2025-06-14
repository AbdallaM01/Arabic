import re
import os
from os import environ, getenv
from Script import script

id_pattern = re.compile(r'^.\d+$')

def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


SESSION = environ.get('SESSION', 'media_search')
API_ID = int(environ.get('API_ID', ''))
API_HASH = environ.get('API_HASH', '')
BOT_TOKEN = environ.get('BOT_TOKEN', "")

CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

PICS = (environ.get('PICS', 'https://telegra.ph/file/8acd09d4ae9084ce0b761.jpg https://telegra.ph/file/25df2285c3e9f8f5daa54.jpg https://telegra.ph/file/252da793f0869b44e8163.jpg https://telegra.ph/file/1c8580738ae6deec3f581.jpg https://telegra.ph/file/eff28922d00a8da7b1bd1.jpg https://telegra.ph/file/f499445c4d0f5e792557d.jpg https://telegra.ph/file/263c112b4d581af9f5f24.jpg https://telegra.ph/file/552d4957910951123fb94.jpg https://telegra.ph/file/dcf4d746c4e737b69741f.jpg https://telegra.ph/file/880f7ece872c6280001a4.jpg https://telegra.ph/file/ffef21e1b0e24a7c06545.jpg https://telegra.ph/file/7a3a461df8ad623b84f46.jpg https://telegra.ph/file/8e369170e7de25ba97289.jpg https://telegra.ph/file/47653f56183fa46a5f457.jpg https://telegra.ph/file/80c20feda44714d02d8f6.jpg https://telegra.ph/file/31c59c503d75128aeb279.jpg https://telegra.ph/file/69b21bbed78c7533c1c48.jpg https://telegra.ph/file/1e9bf17811ef574e001e8.jpg https://telegra.ph/file/610a9305f7a2318c852ac.jpg https://telegra.ph/file/27ea4e5a1a7736bef46c4.jpg https://telegra.ph/file/99b711e2d24eacb84651f.jpg')).split()
NOR_IMG = environ.get("NOR_IMG", "https://graph.org/file/62efbcc4e7580b76530ba.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://graph.org/file/e215d12bfd4fa2155e90e.mp4")
SPELL_IMG = environ.get("SPELL_IMG", "https://graph.org/file/13702ae26fb05df52667c.jpg")
SUBSCRIPTION = (environ.get('SUBSCRIPTION', 'https://telegra.ph/file/f983d857f3ce40795e4b8.jpg'))
FSUB_IMG = (environ.get('FSUB_IMG', 'https://files.catbox.moe/rp148s.jpg')).split() 

ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]  #Admin Id
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-100').split()] #Movie Database Channel Id
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-100'))  #Log Channel Id
BIN_CHANNEL = int(environ.get('BIN_CHANNEL', '-100'))  #Streming Log Channel Id
MOVIE_UPDATE_CHANNEL = int(environ.get('MOVIE_UPDATE_CHANNEL', '-100'))  #Movie Update Channel Id
PREMIUM_LOGS = int(environ.get('PREMIUM_LOGS', '-100')) #Premium Subscription Log Channel Id
reqst_channel = environ.get('REQST_CHANNEL_ID', '-100') #Movie Request Channel Id
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
support_chat_id = environ.get('SUPPORT_CHAT_ID', '-100') #Support Chat Id
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None

DATABASE_URI = environ.get('DATABASE_URI', "") #MongoDB Url
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'ArrowFlix')

# If MULTIPLE_DB Is True Then Fill DATABASE_URI2 Value Else You Will Get Error.
MULTIPLE_DB = is_enabled(os.environ.get('MULTIPLE_DB', "false"), False) # Type True For Turn On MULTIPLE DB FUNTION 
DATABASE_URI2 = environ.get('DATABASE_URI2', "")

GRP_LNK = environ.get('GRP_LNK', 'https://t.me/ArrowFlix2')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/TorrentSeriess')
OWNER_LNK = environ.get('OWNER_LNK', 'https://t.me/AbdallaGX')
UPDATE_CHANNEL_LNK = environ.get('UPDATE_CHANNEL_LNK', 'https://t.me/TorrentSeriess')

#Force Subscription Channel (Put Same Channel Id In Both Veriables)
AUTH_CHANNEL = int(environ.get('AUTH_CHANNEL', '-100')) 
AUTH_REQ_CHANNEL = int(environ.get('AUTH_REQ_CHANNEL', '-100'))

IS_VERIFY = is_enabled('IS_VERIFY', False)
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '-100')) #Verification Channel Id 
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', '-100')) #If Anyone Set Your Bot In Any Group And Set Shortner In That Group Then In This Channel The All Details Come
VERIFY_IMG = environ.get("VERIFY_IMG", "https://telegra.ph/file/9ecc5d6e4df5b83424896.jpg")

TUTORIAL = environ.get("TUTORIAL", "https://t.me/")
TUTORIAL_2 = environ.get("TUTORIAL_2", "https://t.me/")
TUTORIAL_3 = environ.get("TUTORIAL_3", "https://t.me/")

# Verification (Must Fill All Veriables. Else You Got Error
SHORTENER_API = environ.get("SHORTENER_API", "")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", "")

SHORTENER_API2 = environ.get("SHORTENER_API2", "")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", "")

SHORTENER_API3 = environ.get("SHORTENER_API3", "")
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", "")

TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "1200"))
THREE_VERIFY_GAP = int(environ.get('THREE_VERIFY_GAP', "54000"))

#Othes
TMDB_API = environ.get("TMDB_API", "6abcb6bb99fb77f33c37016a28866ed2")
MOVIE_UPDATE_NOTIFICATION = bool(environ.get("MOVIE_UPDATE_NOTIFICATION", False)) #suggested not to turn on here , do with command /movie_update on
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", True))
MAX_B_TN = environ.get("MAX_B_TN", "8")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
PORT = environ.get("PORT", "8080")
MSG_ALRT = environ.get('MSG_ALRT', 'إيجى فلكس بلس ⚡')
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://t.me/') #Support Chat Link with https://
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "False")), False)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "False")), True)
DELETE_TIME = int(environ.get("DELETE_TIME", "300"))  
LINK_MODE = is_enabled((environ.get('LINK_MODE', "True")), False)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "False"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), False)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), True)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "False")), True)
PM_SEARCH = bool(environ.get('PM_SEARCH', False)) 
EMOJI_MODE = bool(environ.get('EMOJI_MODE', False)) 

LANGUAGES = ["malayalam", "", "tamil", "", "english", "", "hindi", "", "telugu", "", "kannada", "", "gujarati", "", "marathi", "", "punjabi", ""]
QUALITIES = ["144", "240", "360", "", "480", "", "720", "", "1080", "", ""]
SEASONS = ["s01" , "s02" , "s03" , "s04", "s05" , "s06" , "s07" , "s08" , "s09" , "s10"]

STREAM_MODE = bool(environ.get('STREAM_MODE', True))

#Dont Make Any Changes Here. Creat A Veriable Name "FQDN" In Your Deploying Plartform And Put App Url
NO_PORT = bool(environ.get('NO_PORT', False))
APP_NAME = None
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = environ.get('APP_NAME')
else:
    ON_HEROKU = False
BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
URL = "https://{}/".format(FQDN) if ON_HEROKU or NO_PORT else "https://{}/".format(FQDN, PORT)
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
WORKERS = int(environ.get('WORKERS', '4'))
SESSION_NAME = str(environ.get('SESSION_NAME', 'SilentXBotz'))
MULTI_CLIENT = False
name = str(environ.get('name', 'SilentX'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = str(getenv('APP_NAME'))
else:
    ON_HEROKU = False
HAS_SSL = bool(getenv('HAS_SSL', True))
if HAS_SSL:
    URL = "https://public-barbie-amagdy2307-a5cc535c.koyeb.app/".format(FQDN)
else:
    URL = "https://public-barbie-amagdy2307-a5cc535c.koyeb.app/".format(FQDN)


REACTIONS = ["🤝", "😇", "🤗", "😍", "👍", "😐", "🥰", "🤩", "😱", "🤣", "😘", "👏", "😛", "😈", "🎉", "⚡️", "🫡", "🤓", "😎", "🏆", "🔥", "🤭", "🌚", "🆒", "👻"]


Bot_cmds = {
    "start": "ꜱᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ",
    "trendlist": "ɢᴇᴛ ᴛᴏᴘ ꜱᴇᴀʀᴄʜ ʟɪꜱᴛ",
    "myplan" : "ᴄʜᴇᴄᴋ ᴘʀᴇᴍɪᴜᴍ ꜱᴜʙꜱᴄʀɪᴘᴛɪᴏɴ",
    "plan" :"ᴄʜᴇᴄᴋ ᴘʀᴇᴍɪᴜᴍ ᴘʀɪᴄᴇ",
    "settings": "ᴄʜᴀɴɢᴇ sᴇᴛᴛɪɴɢs",
    "group_cmd": "ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴇ ꜰʀᴏᴍ ᴅʙ.",
    "admin_cmd": "ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴇ ꜰʀᴏᴍ ᴅʙ.",
    "details": "ꜱᴇᴇ ɢʀᴏᴜᴘ ꜱᴇᴛᴛɪɴɢꜱ",
    "reset_group": "ʀᴇꜱᴇᴛ ɢʀᴏᴜᴘ ꜱᴇᴛᴛɪɴɢꜱ", 
    "stats": "ᴄʜᴇᴄᴋ ʙᴏᴛ ꜱᴛᴀᴛᴜꜱ.",
    "delete": "ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴇ ꜰʀᴏᴍ ᴅʙ.",
    "movie_update": "ᴏɴ ᴏғғ ᴀᴄᴄᴏʀᴅɪɴɢ ʏᴏᴜʀ ɴᴇᴇᴅᴇᴅ...",
    "pm_search": "ᴘᴍ sᴇᴀʀᴄʜ ᴏɴ ᴏғғ ᴀᴄᴄᴏʀᴅɪɴɢ ʏᴏᴜʀ ɴᴇᴇᴅᴇᴅ...",
    "restart": "ʀᴇꜱᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ."
}

#Don't Change Anything Here
if MULTIPLE_DB == False:
    DATABASE_URI = DATABASE_URI
    DATABASE_URI2 = DATABASE_URI
else:
    DATABASE_URI = DATABASE_URI
    DATABASE_URI2 = DATABASE_URI2
