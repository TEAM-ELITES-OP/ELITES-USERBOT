import re

from elitesbot import bot
from elitesbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from elitesbot.cmdhelp import CmdHelp
from elitesbot.helpers.functions import deEmojify


@bot.on(admin_cmd(pattern="anime(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="anime(?: |$)(.*)", allow_sudo=True))
async def nope(eliteboy):
    SAVAGE = eliteboy.pattern_match.group(1)
    if not SAVAGE:
        if eliteboy.is_reply:
            (await eliteboy.get_reply_message()).message
        else:
            await edit_or_reply(eliteboy, "`Sir please give some query to search and download it for you..!`"
            )
            return

    troll = await bot.inline_query("animedb_bot", f"{(deEmojify(SAVAGE))}")

    await troll[0].click(
        eliteboy.chat_id,
        reply_to=eliteboy.reply_to_msg_id,
        silent=True if eliteboy.is_reply else False,
        hide_via=True,
    )
    await eliteboy.delete()
    

CmdHelp("anime").add_command(
  "anime", "<anime name>", "Searches for the given anime and sends the details."
).add()
