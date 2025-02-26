# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "28817205"))
API_HASH = getenv("API_HASH", "f319d02866bf7b83e4de31002f6ba8a3")
BOT_TOKEN = getenv("BOT_TOKEN", "7854445987:AAEAvdj-LYEOEXWvdgcoL1XI179LEeIMY5I")
OWNER_ID = int(getenv("OWNER_ID", "7935947598"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "mongodb+srv://chiruedizz:WmzSiQlS35fLDImn@cluster0.4o4zl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = int(getenv("LOG_GROUP", "-1002468082777"))
FORCESUB = getenv("FORCESUB", "")
