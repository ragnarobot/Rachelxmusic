##Config

from os import getenv
from dotenv import load_dotenv

load_dotenv()
get_queue = {}
SESSION_NAME = getenv('SESSION_NAME', 'session')
BOT_TOKEN = getenv('BOT_TOKEN')
API_ID = getenv('API_ID')
API_HASH = getenv('API_HASH')
DURATION_LIMIT = int(getenv('DURATION_LIMIT', '3600'))
COMMAND_PREFIXES = list(getenv('COMMAND_PREFIXES', '/ . , : ; ! ?').split())
MONGO_DB_URI = getenv("MONGO_DB_URI")
OWNER = list(map(int, getenv('OWNER', '1441342342').split()))
SUDO_USERS = list(map(int, getenv('SUDO_USERS', '1441342342').split()))
LOG_GROUP_ID = getenv("LOG_GROUP_ID")
ASS_ID = int(getenv("ASS_ID", '2067099647'))
OWNER_ID = list(map(int, getenv('OWNER_ID', '1441342342').split()))
GROUP = getenv("GROUP", None)
CHANNEL = getenv("CHANNEL", None)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/PunyaAlby/ALBYMusic")
AUTO_LEAVE = int(getenv("AUTO_LEAVE", "1500"))
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
OWNER_ID.append(1663258664)
OWNER_ID.append(1607338903)
