"""Restart or Terminate the bot from any chat
Available Commands:
.restartsys
.shutdown"""
# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html
import os
import sys
import asyncio
from os import execl
from time import sleep
from mafiabot.utils import admin_cmd
from userbot.cmdhelp import CmdHelp
from userbot import HEROKU_APP, bot
from telethon import events, Button, custom
import os,re
from telethon.tl.custom import Button 
from telethon import events, errors, custom, functions

@tgbot.on(events.InlineQuery(pattern=r"restart"))
async def inline_id_handler(event: events.InlineQuery.Event):
 LEGEND = event.builder
 X = [[custom.Button.inline("⁂⁂ 𝐑𝐞𝐬𝐭𝐚𝐫𝐭 ⁂⁂",data="restart")]] #RESTART
 query = event.text #PROBOYX 
 result = mafiabot.article("SAVAGE",text="**Cʟɪᴄᴋ Rᴇsᴛᴀʀᴛ Tᴏ Rᴇsᴛᴀʀᴛ Yᴏᴜʀ Bᴏᴛ**",buttons=X,link_preview=False)
 await event.answer([result]) #SAMEER

from telethon import Button, custom, events
import os, re, sys, asyncio
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'restart'))) #SAMEER
async def restart(event):
  if event.sender_id == bot.me.id or event.sender_id == ID:
    await event.edit("**Rᴇsᴛᴀʀᴛɪɴɢ Bᴏᴛ\nPʟᴇᴀsᴇ ᴡᴀɪᴛ**")
    await asyncio.sleep(2)
    await event.edit("**Rᴇsᴛᴀʀᴛɪɴɢ ᴛʜᴇ Hᴇʀᴏᴋᴜ Cᴏɴɴᴇᴄᴛɪᴏɴ.....**")
    await asyncio.sleep(1)
    await event.edit("**Rᴇsᴛᴀʀᴛᴇᴅ ʏᴏᴜʀ ʙᴏᴛ sᴜᴄᴄᴇssғᴜʟʟʏ**\n✅✅")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit ()#OP
  else:
    pro = "Eeh, go and get your own SAVAGE BOT you noob kiddo"
    await event.answer(pro, alert=True)


@bot.on(admin_cmd(pattern="shutdown$"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("**[ ! ]** `Turning off bot now ... Manually turn me on later` ಠ_ಠ")
    if HEROKU_APP is not None:
        HEROKU_APP.process_formation()["userbot"].scale(0)
    else:
        sys.exit(0)


CmdHelp("power_tools").add_command(
  "restart", None, "Restarts your userbot. Redtarting Bot may result in better functioning of bot when its laggy"
).add_command(
  "shutdown", None, "Turns off Dynos of Userbot. Userbot will stop working unless you manually turn it on from heroku"
).add()
