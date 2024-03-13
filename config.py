from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("12380656"
API_HASH = getenv("d927c13beaaf5110f25c505b7c071273"

BOT_TOKEN = getenv("BOT_TOKEN")
OWNER_ID = int(getenv("OWNER_ID"))

MONGO_DB_URI = getenv("MONGO_DB_URI")
MUST_JOIN = getenv("MUST_JOIN", None)
