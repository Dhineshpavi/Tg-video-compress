import os, time, re

id_pattern = re.compile(r'^.\d+$') 


class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "11973721")  # ⚠️ Required
    API_HASH  = os.environ.get("API_HASH", "5264bf4663e9159565603522f58d3c18") # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7459860752:AAFytOo0K9HmUY1gyLdIUjAd67tNjowzvLw") # ⚠️ Required
    FORCE_SUB = os.environ.get('FORCE_SUB', '-1002008853384') # ⚠️ Required
    AUTH_CHANNEL = int(FORCE_SUB) if FORCE_SUB and id_pattern.search(
    FORCE_SUB) else None
   
    # database config
    DB_URL  = os.environ.get("DB_URL", "mongodb+srv://evamusicbot:mrwaris04@cluster0.5ad8zuj.mongodb.net/?retryWrites=true&w=majority")  # ⚠️ Required
    DB_NAME  = os.environ.get("DB_NAME","Dp_Botz&Comp") 

    # Other Configs 
    ADMIN = int(os.environ.get("ADMIN", "1242556540")) # ⚠️ Required
    LOG_CHANNEL = int(os.environ.get('LOG_CHANNEL', '-1001789244683')) # ⚠️ Required
    BOT_UPTIME = BOT_UPTIME  = time.time()
    START_PIC = os.environ.get("START_PIC", "https://graph.org/file/15e82d7e665eccc8bd9c5.jpg")

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))


    caption = """
**File Name**: {0}

**Original File Size:** {1}
**Encoded File Size:** {2}
**Compression Percentage:** {3}

__Downloaded in {4}__
__Encoded in {5}__
__Uploaded in {6}__
"""
