from userbot import bot
from sys import argv
import sys
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
import os
from telethon import TelegramClient
from var import Var
from userbot.Config import Config
from userbot.utils import load_module
from userbot import LOAD_PLUG, LOGS, mafiaversion
from pathlib import Path
import asyncio
import telethon.utils

os.system("pip install -U telethon")

async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me() 
    bot.uid = telethon.utils.get_peer_id(bot.me)



if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialisation finished with no errors")
        print("Starting elites")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("elites Startup Completed")
    else:
        bot.start()


import glob
path = 'userbot/plugins/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

import userbot._core

print(f"""𝐂𝐎𝐍𝐆𝐑𝐀𝐓𝐔𝐋𝐀𝐓𝐈𝐎𝐍 𝐘𝐎𝐔𝐑 𝙴𝙻𝙸𝚃𝙴𝚂 𝙱𝙾𝚃 𝐈𝐒 𝐃𝐄𝐏𝐋𝐎𝐘𝐄𝐃 𝐒𝐔𝐂𝐂𝐄𝐒𝐒𝐅𝐔𝐋𝐋𝐘 😈💖💥 .. 𝐓𝐘𝐏𝐄 (.alive or .ping) 𝐅𝐎𝐑 𝐂𝐇𝐄𝐂𝐊 𝐓𝐇𝐀𝐓 𝐁𝐎𝐓 𝐈𝐒 𝐀𝐋𝐈𝐕𝐄 𝐎𝐑 𝐍𝐎𝐓...𝐉𝐎𝐈𝐍 @elites_userbot 𝐅𝐎𝐑 𝐀𝐍𝐘 𝐇𝐄𝐋𝐏 ..𝐄𝐍𝐉𝐎𝐘 𝐔𝐑 𝐁𝐎𝐓🤘😉.""")

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
