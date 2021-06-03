
from math import ceil
from re import compile
import asyncio

from telethon.events import InlineQuery, callbackquery
from telethon.sync import custom
from telethon.tl.functions.channels import JoinChannelRequest

from userbot import *
from userbot.cmdhelp import *
from elitesbot.utils import *
from userbot.Config import Config

Elites_row = 5
Elites_emoji = 5
# thats how a lazy guy imports
# elites op

def button(page, modules):
    Row = 5
    Column = 5

    modules = sorted([modul for modul in modules if not modul.startswith("_")])
    pairs = list(map(list, zip(modules[::3], modules[1::3])))
    if len(modules) % 2 == 1:
        pairs.append([modules[-1]])
    max_pages = ceil(len(pairs) / Row)
    pairs = [pairs[i : i + Row] for i in range(0, len(pairs), Row)]
    buttons = []
    for pairs in pairs[page]:
        buttons.append(
            [
                custom.Button.inline(f"👑 " + pair, data=f"Information[{page}]({pair})")
                for pair in pairs
            ]
        )

    buttons.append(
        [
            custom.Button.inline(
               f"☜︎︎︎ 𝙱𝙰𝙲𝙺༆", data=f"page({(max_pages - 1) if page == 0 else (page - 1)})"
            ),
            custom.Button.inline(
               f"༒︎ 𝙲𝙻𝙾𝚂𝙴 ༒︎", data="close"
            ),
            custom.Button.inline(
               f"༆𝙽𝙴𝚇𝚃 ☞︎︎︎", data=f"page({0 if page == (max_pages - 1) else page + 1})"
            ),
        ]
    )
    return [max_pages, buttons]
    # Changing this line may give error in bot as i added some special cmds in elitesbot channel to get this module work...
                
    modules = CMD_HELP
if Var.TG_BOT_USER_NAME_BF_HER is not None and tgbot is not None:
    @tgbot.on(InlineQuery)  # pylint:disable=E0602
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        if event.query.user_id == bot.uid and query == "@ELITES_USERBOT":
            rev_text = query[::-1]
            veriler = button(0, sorted(CMD_HELP))
            result = await builder.article(
                f"Hey! Only use .help please",
                text=f"**𝚁𝚄𝙽𝙽𝙸𝙽𝙶 𝙴𝙻𝙸𝚃𝙴𝚂 𝙱𝙾𝚃**\n\n__𝙽𝙾. 𝙾𝙵 𝙿𝙻𝚄𝙶𝙶𝙸𝙽𝚂 𝙸𝙽𝚂𝚃𝙰𝙻𝙻𝙴𝙳__ :`{len(CMD_HELP)}`\n**𝙿𝙰𝙶𝙴:** 1/{veriler[0]}",
                buttons=veriler[1],
                link_preview=False,
            )                
        elif query.startswith("http"):
            part = query.split(" ")
            result = builder.article(
                "File uploaded",
                text=f"**File uploaded successfully to {part[2]} site.\n\nUpload Time : {part[1][:3]} second\n[‏‏‎ ‎]({part[0]})",
                buttons=[[custom.Button.url("URL", part[0])]],
                link_preview=True,
            )
        elif event.text=='':
            result = builder.article(
                "@ELITES_USERBOT",
                text="""🔥 𝙴𝙻𝙸𝚃𝙴𝚂'𝚜 𝚁𝙴𝙿𝙾 , 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙲𝙷𝙰𝚃 , 𝚂𝚃𝚁𝙸𝙽𝙶 , 𝙰𝙱𝙾𝚄𝚃 𝙱𝙾𝚃 👇🔥\n [𝙴𝙻𝙸𝚃𝙴𝚂](t.me/elites_userbot)™""",
                buttons=[
                    [            
                        custom.Button.url("🔗 𝖲𝚃𝚁𝙸𝙽𝙶  🔗", "https://replit.com/@sameerpanthi/SAVAGE-BOT#main.py"),
                        custom.Button.url(
                            "💫 𝖲𝚄𝙿𝙿𝙾𝚁𝚃 💫", "https://t.me/ELITES_USERBOT"
                        ),
                    ],
                    [
                        custom.Button.url(
                            "⚜ 𝖱𝙴𝙿𝙾 ⚜", "https://github.com/TEAM-ELITES-OP/ELITES-OP"),
                        custom.Button.url
                    (
                            "👑 creator 👑", "t.me/ELITEBOY_X"
                    )
                    ],
                ],
                link_preview=False,
            )
        await event.answer([result] if result else None)

    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"page\((.+?)\)")))
    async def page(event):
        if not event.query.user_id == bot.uid:
            return await event.answer(
                "Hᴇʏ Bɪᴛᴄʜ Dᴏɴᴛ Usᴇ Mʏ ʙᴏᴛ .. ᴍᴀᴋᴇ Uʀ Oᴡɴ Usᴇʀʙᴏᴛ Aɴᴅ Usᴇ @ELITES_USERBOT",
                cache_time=0,
                alert=True,
            )
        page = int(event.data_match.group(1).decode("UTF-8"))
        veriler = button(page, CMD_HELP)
        await event.edit(
            f"**Lᴇɢᴇɴᴅʀʏ Aғ** [𝙴𝙻𝙸𝚃𝙴𝚂 𝙱𝙾𝚃](https://t.me/ELITES_USERBOT) __Wᴏʀᴋɪɴɢ...__\n\n**Nᴜᴍɴᴇʀ Oғ Mᴏᴅᴜʟᴇs Iɴsᴛᴀʟʟᴇᴅ :** `{len(CMD_HELP)}`\n**Pᴀɢᴇ:** {page + 1}/{veriler[0]}",
            buttons=veriler[1],
            link_preview=False,
        )                                    
                    
    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"close")))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:
            await delete_elitesbot(event,
              "⚜️ 𝙴𝙻𝙸𝚃𝙴𝚂 𝙱𝙾𝚃 Mᴇɴᴜ Pʀᴏᴠɪᴅᴇʀ ɪs CLᴏsᴇᴅ Nᴏᴡ⚜️\n\n         **[© 𝙴𝙻𝙸𝚃𝙴𝚂 ™](t.me/elites_USERBOT)**", 5, link_preview=False
            )
        else:
            SAVAGE_alert = "Hᴇʏ Bɪᴛᴄʜ Dᴏɴᴛ Usᴇ Mʏ ʙᴏᴛ .. ᴍᴀᴋᴇ Uʀ Oᴡɴ Usᴇʀʙᴏᴛ Aɴᴅ Usᴇ @elites_USERBOT"
            await event.answer(elites_alert, cache_time=0, alert=True)
          
    @tgbot.on(
        callbackquery.CallbackQuery(data=compile(b"Information\[(\d*)\]\((.*)\)"))
    )
    async def Information(event):
        if not event.query.user_id == bot.uid:
            return await event.answer(
                "Hᴇʏ Bɪᴛᴄʜ Dᴏɴᴛ Usᴇ Mʏ ʙᴏᴛ .. ᴍᴀᴋᴇ Uʀ Oᴡɴ Usᴇʀʙᴏᴛ Aɴᴅ Usᴇ @ELITES_USERBOT",
                cache_time=0,
                alert=True,
            )

        page = int(event.data_match.group(1).decode("UTF-8"))
        commands = event.data_match.group(2).decode("UTF-8")
        try:
            buttons = [
                custom.Button.inline(
                    "👑 " + cmd[0], data=f"commands[{commands}[{page}]]({cmd[0]})"
                )
                for cmd in CMD_HELP_BOT[commands]["commands"].items()
            ]
        except KeyError:
            return await event.answer(
                "No Description is written for this plugin", cache_time=0, alert=True
            )

        buttons = [buttons[i : i + 2] for i in range(0, len(buttons), 2)]
        buttons.append([custom.Button.inline("☜︎︎︎ 𝙿𝚁𝙴𝚅𝙸𝙾𝚄𝚂༆", data=f"page({page})")])
        await event.edit(
            f"**📗 File:** `{commands}`\n**🔢 Number of commands :** `{len(CMD_HELP_BOT[commands]['commands'])}`",
            buttons=buttons,
            link_preview=False,
        )

    @tgbot.on(
        callbackquery.CallbackQuery(data=compile(b"commands\[(.*)\[(\d*)\]\]\((.*)\)"))
    )
    async def commands(event):
        if not event.query.user_id == bot.uid:
            return await event.answer(
                "Hᴇʏ Bɪᴛᴄʜ Dᴏɴᴛ Usᴇ Mʏ ʙᴏᴛ .. ᴍᴀᴋᴇ Uʀ Oᴡɴ Usᴇʀʙᴏᴛ Aɴᴅ Usᴇ @ELITES_USERBOT",
                cache_time=0,
                alert=True,
            )

        cmd = event.data_match.group(1).decode("UTF-8")
        page = int(event.data_match.group(2).decode("UTF-8"))
        commands = event.data_match.group(3).decode("UTF-8")

        result = f"**📗 File:** `{cmd}`\n"
        if CMD_HELP_BOT[cmd]["info"]["info"] == "":
            if not CMD_HELP_BOT[cmd]["info"]["warning"] == "":
                result += f"**⬇️ Official:** {'✅' if CMD_HELP_BOT[cmd]['info']['official'] else '❌'}\n"
                result += f"**⚠️ Warning :** {CMD_HELP_BOT[cmd]['info']['warning']}\n\n"
            else:
                result += f"**⬇️ Official:** {'✅' if CMD_HELP_BOT[cmd]['info']['official'] else '❌'}\n\n"
        else:
            result += f"**⬇️ Official:** {'✅' if CMD_HELP_BOT[cmd]['info']['official'] else '❌'}\n"
            if not CMD_HELP_BOT[cmd]["info"]["warning"] == "":
                result += f"**⚠️ Warning:** {CMD_HELP_BOT[cmd]['info']['warning']}\n"
            result += f"**ℹ️ Info:** {CMD_HELP_BOT[cmd]['info']['info']}\n\n"

        command = CMD_HELP_BOT[cmd]["commands"][commands]
        if command["params"] is None:
            result += f"**🛠 Commands:** `{COMMAND_HAND_LER[:1]}{command['command']}`\n"
        else:
            result += f"**🛠 Commands:** `{COMMAND_HAND_LER[:1]}{command['command']} {command['params']}`\n"

        if command["example"] is None:
            result += f"**💬 Explanation:** `{command['usage']}`\n\n"
        else:
            result += f"**💬 Explanation:** `{command['usage']}`\n"
            result += f"**⌨️ For Example:** `{COMMAND_HAND_LER[:1]}{command['example']}`\n\n"

        await event.edit(
            result,
            buttons=[
                custom.Button.inline("☜︎︎︎ 𝙿𝚁𝙴𝚅𝙸𝙾𝚄𝚂༆", data=f"Information[{page}]({cmd})")
            ],
            link_preview=False,
        )


