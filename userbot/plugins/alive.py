
import asyncio
import random
from telethon import events
from userbot import ALIVE_NAME, elitesbotversion
from elitesbot.utils import admin_cmd, sudo_cmd
from telethon.tl.types import ChannelParticipantsAdmins
from userbot.cmdhelp import CmdHelp

# 🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "ELITES BOT"


ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

ELITES = bot.uid

edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/cf218c1f0934581d0db48.jpg"
""" =======================CONSTANTS====================== """

pm_caption = "_🔥 #𝐄𝐋𝐈𝐓𝐄𝐒_𝐁𝐎𝐓_𝐎𝐍_𝐅𝐈𝐑𝐄 🔥_\n\n"


pm_caption += f"               __↼𝙈𝘼𝙎𝙏𝙀𝙍 ⇀__\n**      『{DEFAULTUSER}』**\n\n"


pm_caption += "𖣘 𝘼𝘽𝙊𝙐𝙏 𝙈𝙔 𝙎𝙔𝙎𝙏𝙀𝙈 𖣘\n\n"


pm_caption += "➾ Tᴇʟᴇᴛʜᴏɴ : 1.21.5\n"
pm_caption += "➾ Eʟɪᴛᴇs Gʀᴏᴜᴘ  ➣ [𝙹𝙾𝙸𝙽](t.me/ELITES_official)\n"
pm_caption += "➾ Sᴜᴘᴘᴏʀᴛ Cʜᴀɴʟ ➣ [𝙹𝙾𝙸𝙽](https://t.me/ELITE_BOT_OFFICIAL)\n"
pm_caption += "➾ Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ ➣ [𝙹𝙾𝙸𝙽](https://t.me/ELITES_USERBOT)\n"
pm_caption += "➾ Cʀᴇᴀᴛᴏʀ    ➣ [🔥Eʟɪᴛᴇ Bᴏʏ🔥](t.me/INNOCENT_ELITEBOY)\n" 
                  
pm_caption += " \n"
pm_caption += "[✨ Dᴇᴘʟᴏʏ Yᴏᴜʀ Oᴡɴ Eʟɪᴛᴇs Bᴏᴛ✨](https://github.com/TEAM-ELITES-OP/ELITES-BOT)"

                       
# @command(outgoing=True, pattern="^.alive$")
@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()   
    await alive.delete()
    on = await borg.send_file(alive.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(alive.chat_id, on, file=file2) 

    
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, caption=pm_caption)
    await alive.delete()
    
    
CmdHelp("alive").add_command(
  "alive", None, "To check am i alive"
).add_command(
  "awake", None, "To check am i alive with your favorite alive pic"
).add()
