
# Thanks to Sipak bro and Aryan.. 
# animation Idea by @NOOB_GUY_OP (Sipakisking) && @Hell boy_pikachu
# Made by @ROMANTIC_KILLER...and thanks to @Crackexy for the logos...
# Kang with credits else gay...
# Porting in Mafia Userbot by @H1M4N5HU0P

import asyncio
import random
from telethon import events
from userbot import ALIVE_NAME, SAVAGEversion
from SAVAGEbot.utils import admin_cmd, sudo_cmd
from telethon.tl.types import ChannelParticipantsAdmins
from userbot.cmdhelp import CmdHelp

# 🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "SAVAGE BOT"

# Thanks to Sipak bro and Raganork.. 
# animation Idea by @NOOB_GUY_OP (Sipakisking)
# Made by @ROMANTIC_KILLER...and thanks to @Crackexy for the logos...
# Kang with credits else gay...


ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

SAVAGE = bot.uid

edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/f3a82860656f0263bc8aa.jpg"
file2 = "https://telegra.ph/file/a12fa182ccac24b2bb9a5.jpg"
file3 = "https://telegra.ph/file/581e32d5dae4c05d82fa1.jpg"
file4 = "https://telegra.ph/file/b39d4a5cb3f4ae080924b.jpg"
""" =======================CONSTANTS====================== """

pm_caption = "_🔥 𝚂𝙰𝚅𝙰𝙶𝙴 𝙱𝙾𝚃 𝙸𝚂 𝙾𝙽 𝙵𝙸𝚁𝙴 🔥_\n\n"


pm_caption += f"               __↼𝙼𝙰𝚂𝚃𝙴𝚁 ⇀__\n**      『{DEFAULTUSER}』**\n\n"


pm_caption += "𖣘 𝙰𝙱𝙾𝚄𝚃 𝙼𝚈 𝚂𝚈𝚂𝚃𝙴𝙼 𖣘\n\n"


pm_caption += "➾ 𝚃𝙷𝙴𝙻𝙴𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 : 1.19.5\n"
pm_caption += "➾ 𝚃𝙴𝙰𝙼 𝙶𝚁𝙾𝚄𝙿  ➣ [𝙹𝙾𝙸𝙽](https://t.me/joinchat/RPrJW2IU-Uo4MGRl)\n"
pm_caption += "➾ 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙲𝙷𝙽𝙽𝙴𝙻 ➣ [𝙹𝙾𝙸𝙽](https://t.me/joinchat/0KCyT0MHyAhmMmRl)\n"
pm_caption += "➾ 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙶𝚁𝙾𝚄𝙿 ➣ [𝙹𝙾𝙸𝙽](https://t.me/joinchat/qCIk-af6VW1kNDll)\n"
pm_caption += "➾ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁    ➣ [⚡𝚂𝙰𝙼𝙴𝙴𝚁⚡](@SAMEER_795)\n" 
                  
pm_caption += " \n"
pm_caption += "[✨ 𝙳𝙴𝙿𝙻𝙾𝚈 𝚈𝙾𝚄𝚁 𝙾𝚆𝙽 𝚂𝙰𝚅𝙰𝙶𝙴 ✨](https://github.com/sameerpanthi/SAVAGE-2.0-BOT)"


# @command(outgoing=True, pattern="^.alive$")
@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()   
    await alive.delete()
    on = await borg.send_file(alive.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(alive.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(alive.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(alive.chat_id, ok2, file=file1)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(alive.chat_id, ok3, file=file3)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(alive.chat_id, ok4, file=file2)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(alive.chat_id, ok5, file=file4)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(alive.chat_id, ok6, file=file1)
    
    await asyncio.sleep(edit_time)
    ok8 = await borg.edit_message(alive.chat_id, ok7, file=file2) 

    await asyncio.sleep(edit_time)
    ok9 = await borg.edit_message(alive.chat_id, ok8, file=file3)

    await asyncio.sleep(edit_time)
    ok10 = await borg.edit_message(alive.chat_id, ok9, file=file1)
    
    await asyncio.sleep(edit_time)
    ok11 = await borg.edit_message(alive.chat_id, ok10, file=file3)
    
    await asyncio.sleep(edit_time)
    ok12 = await borg.edit_message(alive.chat_id, ok11, file=file2)
    
    await asyncio.sleep(edit_time)
    ok13 = await borg.edit_message(alive.chat_id, ok12, file=file4)
    
    await asyncio.sleep(edit_time)
    ok14 = await borg.edit_message(alive.chat_id, on, file=file1)

    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, caption=pm_caption)
    await alive.delete()
    
    
CmdHelp("alive").add_command(
  "alive", None, "To check am i alive"
).add_command(
  "savage", None, "To check am i alive with your favorite alive pic"
).add()
