import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "1954786730"))
    API_HASH = os.environ.get("API_HASH", "cf7a3453abd8bc841a495ba655d2cef0")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    STRING_SESSION = os.environ.get("STRING_SESSION", None)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "http://t.me/AnanyaMusic_bot")
    SUPPORT = os.environ.get("SUPPORT", "https://t.me/ananyamusicBot6789") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "https://t.me/ananya_update56") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
