# Credits to @spechide and his team for @TROLLVOICEBOT
# made by @eliteboy_the_badass from the snippets of waifu AKA stickerizerbot....
# kang karega kya madarchod?
# aukaat h bsdk teri...jake baap ka loda chus ke aa....


import re

from userbot import bot
from elitesbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp
from userbot.helpers.functions import deEmojify


@bot.on(admin_cmd(pattern="mev(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="mev(?: |$)(.*)", allow_sudo=True))
async def nope(eliteboy):
    SAVAGE = eliteboy.pattern_match.group(1)
    if not SAVAGE:
        if eliteboy.is_reply:
            (await eliteboy.get_reply_message()).message
        else:
            await edit_or_reply(eliteboy, "`Sir please give some query to search and download it for you..!`"
            )
            return

    troll = await bot.inline_query("TrollVoiceBot", f"{(deEmojify(SAVAGE))}")

    await troll[0].click(
        eliteboy.chat_id,
        reply_to=eliteboy.reply_to_msg_id,
        silent=True if eliteboy.is_reply else False,
        hide_via=True,
    )
    await eliteboy.delete()
    

CmdHelp("memevoice").add_command(
  "mev", "<meme txt>", "Searches and uploads the meme in voice format (if any)."
).add()