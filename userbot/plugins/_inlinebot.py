
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
                custom.Button.inline(f"π " + pair, data=f"Information[{page}]({pair})")
                for pair in pairs
            ]
        )

    buttons.append(
        [
            custom.Button.inline(
               f"βοΈοΈοΈ π±π°π²πΊΰΌ", data=f"page({(max_pages - 1) if page == 0 else (page - 1)})"
            ),
            custom.Button.inline(
               f"ΰΌοΈ π²π»πΎππ΄ ΰΌοΈ", data="close"
            ),
            custom.Button.inline(
               f"ΰΌπ½π΄ππ βοΈοΈοΈ", data=f"page({0 if page == (max_pages - 1) else page + 1})"
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
                text=f"**πππ½π½πΈπ½πΆ π΄π»πΈππ΄π π±πΎπ**\n\n__π½πΎ. πΎπ΅ πΏπ»ππΆπΆπΈπ½π πΈπ½πππ°π»π»π΄π³__ :`{len(CMD_HELP)}`\n**πΏπ°πΆπ΄:** 1/{veriler[0]}",
                buttons=veriler[1],
                link_preview=False,
            )                
        elif query.startswith("http"):
            part = query.split(" ")
            result = builder.article(
                "File uploaded",
                text=f"**File uploaded successfully to {part[2]} site.\n\nUpload Time : {part[1][:3]} second\n[βββ β]({part[0]})",
                buttons=[[custom.Button.url("URL", part[0])]],
                link_preview=True,
            )
        elif event.text=='':
            result = builder.article(
                "@ELITES_USERBOT",
                text="""π₯ π΄π»πΈππ΄π'π ππ΄πΏπΎ , πππΏπΏπΎππ π²π·π°π , ππππΈπ½πΆ , π°π±πΎππ π±πΎπ ππ₯\n [π΄π»πΈππ΄π](t.me/elites_userbot)β’""",
                buttons=[
                    [            
                        custom.Button.url("π π²πππΈπ½πΆ  π", "https://replit.com/@sameerpanthi/SAVAGE-BOT#main.py"),
                        custom.Button.url(
                            "π« π²ππΏπΏπΎππ π«", "https://t.me/ELITES_USERBOT"
                        ),
                    ],
                    [
                        custom.Button.url(
                            "β π±π΄πΏπΎ β", "https://github.com/TEAM-ELITES-OP/ELITES-OP"),
                        custom.Button.url
                    (
                            "π creator π", "t.me/ELITEBOY_X"
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
                "Hα΄Κ BΙͺα΄α΄Κ Dα΄Ι΄α΄ Usα΄ MΚ Κα΄α΄ .. α΄α΄α΄α΄ UΚ Oα΄‘Ι΄ Usα΄ΚΚα΄α΄ AΙ΄α΄ Usα΄ @ELITES_USERBOT",
                cache_time=0,
                alert=True,
            )
        page = int(event.data_match.group(1).decode("UTF-8"))
        veriler = button(page, CMD_HELP)
        await event.edit(
            f"**Lα΄Ι’α΄Ι΄α΄ΚΚ A?** [π΄π»πΈππ΄π π±πΎπ](https://t.me/ELITES_USERBOT) __Wα΄Κα΄ΙͺΙ΄Ι’...__\n\n**Nα΄α΄Ι΄α΄Κ O? Mα΄α΄α΄Κα΄s IΙ΄sα΄α΄ΚΚα΄α΄ :** `{len(CMD_HELP)}`\n**Pα΄Ι’α΄:** {page + 1}/{veriler[0]}",
            buttons=veriler[1],
            link_preview=False,
        )                                    
                    
    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"close")))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:
            await delete_elitesbot(event,
              "βοΈ π΄π»πΈππ΄π π±πΎπ Mα΄Ι΄α΄ PΚα΄α΄ Ιͺα΄α΄Κ Ιͺs CLα΄sα΄α΄ Nα΄α΄‘βοΈ\n\n         **[Β© π΄π»πΈππ΄π β’](t.me/elites_USERBOT)**", 5, link_preview=False
            )
        else:
            SAVAGE_alert = "Hα΄Κ BΙͺα΄α΄Κ Dα΄Ι΄α΄ Usα΄ MΚ Κα΄α΄ .. α΄α΄α΄α΄ UΚ Oα΄‘Ι΄ Usα΄ΚΚα΄α΄ AΙ΄α΄ Usα΄ @elites_USERBOT"
            await event.answer(elites_alert, cache_time=0, alert=True)
          
    @tgbot.on(
        callbackquery.CallbackQuery(data=compile(b"Information\[(\d*)\]\((.*)\)"))
    )
    async def Information(event):
        if not event.query.user_id == bot.uid:
            return await event.answer(
                "Hα΄Κ BΙͺα΄α΄Κ Dα΄Ι΄α΄ Usα΄ MΚ Κα΄α΄ .. α΄α΄α΄α΄ UΚ Oα΄‘Ι΄ Usα΄ΚΚα΄α΄ AΙ΄α΄ Usα΄ @ELITES_USERBOT",
                cache_time=0,
                alert=True,
            )

        page = int(event.data_match.group(1).decode("UTF-8"))
        commands = event.data_match.group(2).decode("UTF-8")
        try:
            buttons = [
                custom.Button.inline(
                    "π " + cmd[0], data=f"commands[{commands}[{page}]]({cmd[0]})"
                )
                for cmd in CMD_HELP_BOT[commands]["commands"].items()
            ]
        except KeyError:
            return await event.answer(
                "No Description is written for this plugin", cache_time=0, alert=True
            )

        buttons = [buttons[i : i + 2] for i in range(0, len(buttons), 2)]
        buttons.append([custom.Button.inline("βοΈοΈοΈ πΏππ΄ππΈπΎππΰΌ", data=f"page({page})")])
        await event.edit(
            f"**π File:** `{commands}`\n**π’ Number of commands :** `{len(CMD_HELP_BOT[commands]['commands'])}`",
            buttons=buttons,
            link_preview=False,
        )

    @tgbot.on(
        callbackquery.CallbackQuery(data=compile(b"commands\[(.*)\[(\d*)\]\]\((.*)\)"))
    )
    async def commands(event):
        if not event.query.user_id == bot.uid:
            return await event.answer(
                "Hα΄Κ BΙͺα΄α΄Κ Dα΄Ι΄α΄ Usα΄ MΚ Κα΄α΄ .. α΄α΄α΄α΄ UΚ Oα΄‘Ι΄ Usα΄ΚΚα΄α΄ AΙ΄α΄ Usα΄ @ELITES_USERBOT",
                cache_time=0,
                alert=True,
            )

        cmd = event.data_match.group(1).decode("UTF-8")
        page = int(event.data_match.group(2).decode("UTF-8"))
        commands = event.data_match.group(3).decode("UTF-8")

        result = f"**π File:** `{cmd}`\n"
        if CMD_HELP_BOT[cmd]["info"]["info"] == "":
            if not CMD_HELP_BOT[cmd]["info"]["warning"] == "":
                result += f"**β¬οΈ Official:** {'β' if CMD_HELP_BOT[cmd]['info']['official'] else 'β'}\n"
                result += f"**β οΈ Warning :** {CMD_HELP_BOT[cmd]['info']['warning']}\n\n"
            else:
                result += f"**β¬οΈ Official:** {'β' if CMD_HELP_BOT[cmd]['info']['official'] else 'β'}\n\n"
        else:
            result += f"**β¬οΈ Official:** {'β' if CMD_HELP_BOT[cmd]['info']['official'] else 'β'}\n"
            if not CMD_HELP_BOT[cmd]["info"]["warning"] == "":
                result += f"**β οΈ Warning:** {CMD_HELP_BOT[cmd]['info']['warning']}\n"
            result += f"**βΉοΈ Info:** {CMD_HELP_BOT[cmd]['info']['info']}\n\n"

        command = CMD_HELP_BOT[cmd]["commands"][commands]
        if command["params"] is None:
            result += f"**π  Commands:** `{COMMAND_HAND_LER[:1]}{command['command']}`\n"
        else:
            result += f"**π  Commands:** `{COMMAND_HAND_LER[:1]}{command['command']} {command['params']}`\n"

        if command["example"] is None:
            result += f"**π¬ Explanation:** `{command['usage']}`\n\n"
        else:
            result += f"**π¬ Explanation:** `{command['usage']}`\n"
            result += f"**β¨οΈ For Example:** `{COMMAND_HAND_LER[:1]}{command['example']}`\n\n"

        await event.edit(
            result,
            buttons=[
                custom.Button.inline("βοΈοΈοΈ πΏππ΄ππΈπΎππΰΌ", data=f"Information[{page}]({cmd})")
            ],
            link_preview=False,
        )


