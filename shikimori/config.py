# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os

from Shikimori.vars import HEROKU_API_KEY, HEROKU_APP_NAME, REDIS_URL

def get_user_list(config, key):
    with open("{}/Senku/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 20845525  # integer value, dont use ""
    API_HASH = "0050453e7ad58679e823fa5767117ff7"
    BOT_TOKEN = "5918398685:AAESsrTJ0YwIASlYIe7u-UZbWWmVIIE8CKA"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 1981344911  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "shoushuke"
    SUPPORT_CHAT = "humans_are_here"  # Your own group for support, do not add the @
    LOG_CHANNEL = (
        -1504590700
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "something://somewhat:user@hosturl:port/databasename"  # needed for any database modules
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    URL = None
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "awoo"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "awoo"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "awoo"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = "awoo"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None
    ERROR_LOG_CHANNEL = -1001501815938  # needed to make sure 'save from' messages persist
    HEROKU_API_KEY = 2088106582  # Your Heroku API key, get it from 'https://dashboard.heroku.com/account
    HEROKU_APP_NAME = (
        "awoo"  # Enter the Heroku app name here (Must an exact same name with your input above)
    )
    ARQ_API = "FCGUBP-TMPNAX-APQOHT-GQKNVU-ARQ"
    APOD_API_KEY = "IeulgCzxQ2WfdCDtfXsaMbSGnJTFqNM8wPsncBN6"
    REDIS_URL = "redis://default:cdgiOMJGyZsqx97p5S7S@containers-us-west-27.railway.app:6644"
    ANIME_NAME = "Shikimori's not just a cutie"
    START_MEDIA = "https://telegra.ph/file/9235d57807362b4e227a3.mp4"
    BOT_USERNAME = "shikimori_noobbot"
    UPDATE_CHANNEL = "knights-x-association"
    ALIVE_MEDIA = "https://telegra.ph/file/2b04f7812f22b983f8a10.mp4"
    BOT_ID = 5918398685
    STATS_IMG = ""
    NETWORK_USERNAME = "knights-x-association"
    NETWORK = "knights network"
    INLINE_IMG = "https://telegra.ph/file/8cec66d01df8c0071ebaa.jpg"
    API_WEATHER = ""
    OWNER_WELCOME_MEDIA = ""

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
