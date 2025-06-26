import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "200"))

DEVS = list(map(int, os.getenv("DEVS", "7763380474").split()))

API_ID = int(os.getenv("API_ID", "13777245"))

API_HASH = os.getenv("API_HASH", "625d95334e22b3566dd223bbccfc3223")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8150694852:AAF3V3Nom7cSmAZ8nzXreCqaVQcfyk7PC0c")

OWNER_ID = int(os.getenv("OWNER_ID", "7763380474"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002633472922").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://userbotzanx:userbotzanx@cluster0.y6upssf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", " -1002633472922"))
