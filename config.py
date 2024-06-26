# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "28526237"))
API_HASH = getenv("API_HASH", "936db76a74f9a52cfb2cea8a62e4c20e")
BOT_TOKEN = getenv("BOT_TOKEN", "7346915962:AAGt7U1tdKUkijAPKCJRgrB3ft_jwuEq-JU")
OWNER_ID = list(map(int, getenv("OWNER_ID", "").split()))
MONGO_DB = getenv("MONGO_DB", "")
LOG_GROUP = getenv("LOG_GROUP", "")
CHANNEL_ID = int(getenv("CHANNEL_ID", ""))
