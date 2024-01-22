# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "2843648")

API_HASH = os.environ.get("API_HASH", "95c8ab0714c6bb6742ce2a9ee5fd8ad8")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6557223577:AAFomPQOd40HExjZ210WaHK4eMCtPqvYxxsmongodb+srv://akintorlaamrafael01:wQeIXwUD1ZNVMxdq@cluster0.3zwmr8s.mongodb.net/?retryWrites=true&w=majority") 

FORCE_SUB = os.environ.get("FORCE_SUB", "VJ_Botz") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "renamevjbot")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://akintorlaamrafael01:wQeIXwUD1ZNVMxdq@cluster0.3zwmr8s.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1120212895').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
