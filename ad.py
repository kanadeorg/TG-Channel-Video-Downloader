import asyncio
import time
import mimetypes
import re
from telethon import TelegramClient, events
api_id = "" # Your API ID
api_hash = "" # Your API Hash
session_name = "" # Session Name
client = TelegramClient(session_name, api_id, api_hash)
@client.on(events.NewMessage(chats=("https://t.me/"))) # Channel goes here
async def anime_download_handler(event):
    rstr = r"[\/\\\:\*\?\"\<\>\|]"
    print(event.message.message+" start downloading....")
    def callback(current, total):
        print("Downloaded ", current, ' out of ', total, 'bytes: {:.2%}'.format(current/total))
    filename = re.sub(rstr, "", event.message.message)
    await client.download_media(event.message, filename+mimetypes.guess_extension(event.message.document.mime_type), progress_callback=callback)
    print(event.message.message+" downloaded")
client.start()
client.run_until_disconnected()