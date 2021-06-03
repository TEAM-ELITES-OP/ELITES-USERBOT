import asyncio
import os
from datetime import datetime
from pathlib import Path
from telethon import events
from telethon import functions, types
from telethon.tl.types import InputMessagesFilterDocument
from elitesbot.utils import *
from userbot import *
from userbot import bot as elitesbot

DELETE_TIMEOUT = 5
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "elites User"
elitesbot_logo = "./ELITES-OP/ELITES-BOT-LOGO.jpg"
eliteboy = elitesbot.uid
elitesbot = f"[{DEFAULTUSER}](tg://user?id={eliteboy})"

@elitesbot.on(admin_cmd(pattern=r"send (?P<shortname>\w+)", outgoing=True))
@elitesbot.on(sudo_cmd(pattern=r"send (?P<shortname>\w+)", allow_sudo=True))
async def send(event):
    if event.fwd_from:
        return
    message_id = event.message.id
    thumb = elitesbot_logo
    input_str = event.pattern_match.group(1)
    omk = f"𝖯𝙻𝚄𝙶𝙸𝙽 𝙽𝙰𝙼𝙴 ➪ `{input_str}`\n𝖴𝙿𝙻𝙾𝙰𝙳𝙴𝙳 𝙱𝚈 ➪ {elitesbot}\n\n[𝙴𝙻𝙸𝚃𝙴𝚂 𝚄𝚂𝙴𝚁𝙱𝙾𝚃 ©](t.me/elites_userbot)"
    the_plugin_file = "./userbot/plugins/{}.py".format(input_str)
    if os.path.exists(the_plugin_file):
        lauda = await event.client.send_file(
            event.chat_id,
            the_plugin_file,
            thumb=thumb,
            caption=omk,
            force_document=True,
            allow_cache=False,
            reply_to=message_id,
        )
        await event.delete()
    else:
        await edit_or_reply(event, "File not found..... Kek")

@elitesbot.on(admin_cmd(pattern="install$", outgoing=True))
@elitesbot.on(sudo_cmd(pattern="install$", allow_sudo=True))
async def install(event):
    if event.fwd_from:
        return
    a = "__Installing.__"
    b = 1
    await event.edit(a)
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        try:
            downloaded_file_name = await event.client.download_media(  # pylint:disable=E0602
                await event.get_reply_message(),
                "./userbot/plugins/"  # pylint:disable=E0602
            )
            if "(" not in downloaded_file_name:
                path1 = Path(downloaded_file_name)
                shortname = path1.stem
                load_module(shortname.replace(".py", ""))
                if shortname in CMD_LIST:
                    string = "**Commands found in** `{}` (sudo included)\n".format((os.path.basename(downloaded_file_name)))
                    for i in CMD_LIST[shortname]:
                        string += "  •  `" + i 
                        string += "`\n"
                        if b == 1:
                            a = "__Installing..__"
                            b = 2
                        else:
                            a = "__Installing...__"
                            b = 1
                        await event.edit(a)
                    return await event.edit(f"✅ **Installed module** :- `{shortname}` \n✨ BY :- {SAVAGE}\n\n{string}\n\n        ⚡ **[Lᴇɢᴇɴᴅʀʏ Aғ Sᴀᴠᴀɢᴇ Bᴏᴛ](t.me/SAVAGE_USERBOT)** ⚡", link_preview=False)
                return await event.edit(f"Installed module `{os.path.basename(downloaded_file_name)}`")
            else:
                os.remove(downloaded_file_name)
                return await event.edit(f"**Failed to Install** \n`Error`\nModule already installed or unknown format")
        except Exception as e: 
            await event.edit(f"**Failed to Install** \n`Error`\n{str(e)}")
            return os.remove(downloaded_file_name)
    
@elitesbot.on(admin_cmd(pattern=r"uninstall (?P<shortname>\w+)", outgoing=True))
@elitesbot.on(sudo_cmd(pattern=r"uninstall (?P<shortname>\w+)", allow_sudo=True))
async def uninstall(h1m4n5hu0p):
    if eliteboy.fwd_from:
        return
    shortname = eliteboy.pattern_match["shortname"]
    dir_path =f"./userbot/plugins/{shortname}.py"
    try:
        remove_plugin(shortname)
        os.remove(dir_path)
        await elitebot.edit(f"Uninstalled `{shortname}` successfully")
    except OSError as e:
        await eliteboy.edit("Error: %s : %s" % (dir_path, e.strerror))

@elitesbot.on(admin_cmd(pattern=r"unload (?P<shortname>\w+)$"))
@elitesbot.on(sudo_cmd(pattern=r"upload (?P<shortname>\w+)$", allow_sudo=True))
async def unload(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    try:
        remove_plugin(shortname)
        await event.edit(f"Sᴜᴄᴄᴇssғᴜʟʟʏ Uɴʟᴏᴀᴅᴇᴅ `{shortname}`")
    except Exception as e:
        await event.edit(
            "Sᴜᴄᴄᴇssғᴜʟʟʏ Uɴʟᴏᴀᴅᴇᴅ {shortname}\n{}".format(
                shortname, str(e)
            )
        )


@elitesbot.on(admin_cmd(pattern=r"load (?P<shortname>\w+)$"))
@elitesbot.on(sudo_cmd(pattern=r"load (?P<shortname>\w+)$", allow_sudo=True))
async def load(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    try:
        try:
            remove_plugin(shortname)
        except BaseException:
            pass
        load_module(shortname)
        await event.edit(f"SᴜᴄᴄᴇssFᴜLʟʏ Lᴏᴀᴅᴇᴅ `{shortname}`")
    except Exception as e:
        await event.edit(
            f"Sorry, could not load {shortname} because of the following error.\n{str(e)}"
        )

CmdHelp("core").add_command(
  "install", "<reply to a .py file>", "Installs the replied python file if suitable to userbot codes. (TEMPORARILY DISABLED AS HACKERS MAKE YOU INSTALL SOME PLUGINS AND GET YOUR DATA)"
).add_command(
  "uninstall", "<plugin name>", "Uninstalls the given plugin from userbot. To get that again do .restart", "uninstall alive"
).add_command(
  "load", "<plugin name>", "Loades the unloaded plugin to your userbot", "load alive"
).add_command(
  "unload", "<plugin name>", "Unloads the plugin from your userbot", "unload alive"
).add_command(
  "send", "<file name>", "Sends the given file from your userbot server, if any.", "send alive"
).add_command(
  "cmds", None, "Gives out the list of modules in SAVAGEbot."
).add()
