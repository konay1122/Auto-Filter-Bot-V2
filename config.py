
import os
import logging
from logging.handlers import RotatingFileHandler


# Get a bot token from botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

# Get from my.telegram.org (or @UseTGXBot)
APP_ID = int(os.environ.get("APP_ID", "6691216"))

# Get from my.telegram.org (or @UseTGXBot)
API_HASH = os.environ.get("API_HASH", "56170666b4adfa400f7ef9f18f1fe6f3")

# Generate a user session string 
TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQAW7d5l9ZqiAhxQPJmggXSV9bBf-XpojULYnL8d4HZKJUHJm7kKkQ2ERk4QEINRBDOcXZylkKKGeLGYcCiSm62_e8pDOq5MAPGICSYQfW6aqIVD_FmhZNIeLmG9MYk9rFlXzFS0t2kE8v7flrSEWrhIVlORzfT0sgNEUn39wI4pODWRK_i73Hgw6_AsS7QXNslyMM2mqTHvKrbLTD7CjulHKkNz2y2yXdBaNqsxCxKBnowxPJjCnsCKv0p-PSUrUn8n6GxUp1m_bIhgjpQ_gXmncHiXiWu2xFuL4lPdpra1bb30jlm4azi30o8VrV58WzbvJcopmEnpXN7D-txeftXjYw7WPQA")

# Database URL from https://cloud.mongodb.com/
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://new_user_user1212:thuta12345@cluster0.lhmmymb.mongodb.net/?retryWrites=true&w=majority")

# Your database name from mongoDB
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

# ID of users that can use the bot commands
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1661916733 5015698762").split())

# Should bot search for document files in channels
DOC_SEARCH = os.environ.get("DOC_SEARCH", "yes").lower()

# Should bot search for video files in channels
VID_SEARCH = os.environ.get("VID_SEARCH", "yes").lower()

# Should bot search for music files in channels
MUSIC_SEARCH = os.environ.get("MUSIC_SEARCH", "yes").lower()




TG_BOT_SESSION = os.environ.get("TG_BOT_SESSION", "bot")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
LOG_FILE_NAME = "filterbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
