from telethon import TelegramClient, events, sync
from gtts import gTTS
# import os
# import random

api_id = '913414'
api_hash = 'e1f35bbc705e05e245aea455083f7040'
bot_token = '927467383:AAGmCO4PsCBHxEqheSU8aVcUMehjXULfNGQ'
tg_group = 'KinoUndCoByLoco'

client = TelegramClient('slap', api_id, api_hash)
client.start(bot_token=bot_token)

# SLAP action
@client.on(events.NewMessage(pattern='\!slap'))
async def handler(event):
    users = await client.get_participants(tg_group)
    sender = (await event.get_sender()).first_name
    slapped = random.choice(users)

    await event.reply(sender + ' has slapped @' + slapped.username)

# TTS action
"""
@client.on(events.NewMessage(pattern='\!tts (.+)'))
async def handler(event):
    filename = str(int(round(time.time() * 1000))) + '.mp3'
    text = event.pattern_match.group(1)[:50]
    tts = gTTS(text=text, lang='en')
    tts.save(filename)

    await event.reply(file=filename)
    os.remove(filename)
"""

client.run_until_disconnected()
