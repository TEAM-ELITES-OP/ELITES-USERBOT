
import asyncio
import random
from telethon import events
from userbot import ALIVE_NAME, elitesbotversion
from elitesbot.utils import admin_cmd, sudo_cmd
from telethon.tl.types import ChannelParticipantsAdmins
from userbot.cmdhelp import CmdHelp

# π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "ELITES BOT"


ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

ELITES = bot.uid

edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/74686cebff547b3cd20da.jpg"
""" =======================CONSTANTS====================== """

pm_caption = "_π₯ #πππππππ_πππ_ππ_ππππ π₯_\n\n"


pm_caption += f"               __βΌππΌππππ β__\n**      γ{DEFAULTUSER}γ**\n\n"


pm_caption += "π£ πΌπ½πππ ππ ππππππ π£\n\n"


pm_caption += "βΎ Tα΄Κα΄α΄Κα΄Ι΄ : 1.21.5\n"
pm_caption += "βΎ Bα΄sα΄Ιͺα΄s GΚα΄α΄α΄  β£ [πΉπΎπΈπ½](https://t.me/joinchat/O7FUnmgmSw5lNjA1)\n"
pm_caption += "βΎ Sα΄α΄α΄α΄Κα΄ CΚα΄Ι΄Κ β£ [πΉπΎπΈπ½](https://t.me/ELITE_BOT_OFFICIAL)\n"
pm_caption += "βΎ Sα΄α΄α΄α΄Κα΄ GΚα΄α΄α΄ β£ [πΉπΎπΈπ½](https://t.me/ELITES_USERBOT)\n"
pm_caption += "βΎ CΚα΄α΄α΄α΄Κ    β£ [π₯EΚΙͺα΄α΄ Bα΄Κπ₯](t.me/ELITEBOY_OFFICIAL)\n" 
                                          
pm_caption += " \n"
pm_caption += "[β¨ Dα΄α΄Κα΄Κ Yα΄α΄Κ Oα΄‘Ι΄ Bα΄sα΄Ιͺα΄s Bα΄α΄β¨](https://github.com/TEAM-ELITES-OP/BESTIES-BOT)"

                       
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
