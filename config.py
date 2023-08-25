from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("22839633")
API_HASH = getenv("5287f94935d4830bbbb242fc09ef050d")

BOT_TOKEN = getenv("BOT_TOKEN")
OWNER_ID = int(getenv("OWNER_ID"))

MONGO_DB_URI = getenv("MONGO_DB_URI")
MUST_JOIN = getenv("MUST_JOIN", None)
