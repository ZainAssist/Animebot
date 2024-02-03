from pyrogram import Client, filters
import requests
import random
import os
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup  
from myrogram import notJoin , forceMe

TOKEN = os.environ.get("TOKEN", "")

API_ID = int(os.environ.get("API_ID", ))

API_HASH = os.environ.get("API_HASH", "")

app = Client("anime-gen", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)

regex_photo = ["waifu","neko"]
pht = random.choice(regex_photo)
url = f"https://api.waifu.pics/sfw/{pht}"
      
@app.on_callback_query()
async def handle_query(client, query):
    if query.data == "again":
     response = requests.get(url).json()
     up = response['url']
     if up:
      but = [[InlineKeyboardButton("Generate again ✨", callback_data=f'again')],
             [InlineKeyboardButton("Join 🌺", url=f'https://t.me/+-o9-tiKTRrhmY2Zl')]]
      markup = InlineKeyboardMarkup(but)
      await query.message.reply_photo(up,caption="**@The_Eternity_Soul**",reply_markup=markup)
     else:
      await query.message.reply("Request failed try /again")
    		
@app.on_message(filters.private)
def get_waifu(client, message):
    res = forceMe(message.chat.id)
    if res == "no":
      return notJoin(client,message)
    response = requests.get(url).json()
    up = response['url']
    if up:
        button = [[InlineKeyboardButton("Generate again ✨", callback_data=f'again')],
                  [InlineKeyboardButton("Join 🌺", url=f'https://t.me/+-o9-tiKTRrhmY2Zl')]]
        markup = InlineKeyboardMarkup(button)
        message.reply_photo(up,caption="**@The_Eternity_Soul**",reply_markup=markup)
    else:
        message.reply("Request failed try /again")
        
app.run()
