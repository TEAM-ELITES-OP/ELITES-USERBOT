
import asyncio
import random
from telethon import events
from userbot import ALIVE_NAME, SAVAGEversion
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

pm_caption = "_🔥 𝙀𝙇𝙄𝙏𝙀𝙎 𝘽𝙊𝙏 𝙄𝙎 𝙊𝙉 𝙁𝙄𝙍𝙀🔥_\n\n"


pm_caption += f"               __↼𝙈𝘼𝙎𝙏𝙀𝙍 ⇀__\n**      『{DEFAULTUSER}』**\n\n"


pm_caption += "𖣘 𝘼𝘽𝙊𝙐𝙏 𝙈𝙔 𝙎𝙔𝙎𝙏𝙀𝙈 𖣘\n\n"


pm_caption += "➾ 𝙏𝙀𝙇𝙀𝙏𝙃𝙊𝙉 : 1.19.5\n"
pm_caption += "➾ 𝙀𝙇𝙄𝙏𝙀𝙎 𝙂𝙍𝙋  ➣ [𝙹𝙾𝙸𝙽](t.me/ELITES_official)\n"
pm_caption += "➾ 𝙎𝙐𝙋𝙋𝙊𝙍𝙏 𝘾𝙃𝙉𝙇 ➣ [𝙹𝙾𝙸𝙽](https://t.me/ELITE_BOT_OFFICIAL)\n"
pm_caption += "➾ 𝙎𝙐𝙋𝙋𝙊𝙍𝙏 𝙂𝙍𝙋➣ [𝙹𝙾𝙸𝙽](https://t.me/ELITES_USERBOT)\n"
pm_caption += "➾ 𝘾𝙍𝙀𝘼𝙏𝙊𝙍    ➣ [🔥𝙀𝙇𝙄𝙏𝙀 𝘽𝙊𝙔🔥](t.me/ELITEBOY_X)\n" 
                  
pm_caption += " \n"
pm_caption += "[✨ 𝙳𝙴𝙿𝙻𝙾𝚈 𝚈𝙾𝚄𝚁 𝙾𝚆𝙽 𝙱𝙾𝚃 ✨](https://github.com/TEAM-ELITES-OP/ELITES-BOT)"

                       
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
