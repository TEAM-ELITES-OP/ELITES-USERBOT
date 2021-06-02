# COPYRIGHT (C) 2021-22 BY LEGENDX22
from telethon import events, Button, custom
from telethon import events, Button, custom

from math import ceil
from re import compile
import asyncio

from telethon.events import InlineQuery, callbackquery
from telethon.sync import custom
from telethon.tl.functions.channels import JoinChannelRequest

from userbot import *
from userbot.cmdhelp import *
from SAVAGEbot.utils import *
from userbot.Config import Config
import os,re
from telethon.tl.custom import Button 
from telethon import events, errors, custom, functions
@tgbot.on(callbackquery.CallbackQuery(data=re.compile(b"savage")))
async def inline_id_handler(event: events.InlineQuery.Event):
 SAVAGEbot = event.builder
 X= [[custom.Button.inline("🔥 Cʟɪᴄᴋ Hᴇʀᴇ 🔥",data="oobhai")]]
 query = event.text
 result = SAVAGEbot.article("ᴅᴀɪsʏX",text="**ᴅᴀɪsʏX's Rᴇᴘᴏ, Dᴇᴘʟᴏʏ ᴀɴᴅ Sᴜᴘᴘᴏʀᴛ\n\n© @ULTRAXOT**",buttons=X,link_preview=False)
 await event.answer([result])
@tgbot.on(callbackquery.CallbackQuery(data=re.compile(b"oobhai")))
async def callback_query_handler(event):
  await event.edit(text=f"**{BOT} Rᴇᴘᴏ, Dᴇᴘʟᴏʏ ᴀɴᴅ Gʀᴏᴜᴘ Lɪɴᴋ\n\n© @ULTRAXOT**",buttons=[Button.url(f"⚜️ Rᴇᴘᴏ ⚜️", url="https://github.com/ULTRA-OP/ULTRA-X")])
