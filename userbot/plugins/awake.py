import time

from userbot import ALIVE_NAME, StartTime, elitesbotversion
from elitesbot.utils import admin_cmd, edit_or_reply, sudo_cmd
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName

async def reply_id(event):
    reply_to_id = None
    if event.sender_id in Config.SUDO_USERS:
        reply_to_id = event.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    return reply_to_id


DEFAULTUSER = ALIVE_NAME or "elites User"
MAFIA_IMG = Config.ALIVE_PIC
CUSTOM_ALIVE_TEXT = Config.ALIVE_MSG or "ππππππππ£πͺ_πΈπ½_ππππ₯ππ€ππ π₯"
                                  
USERID = bot.uid

mention = f"[{DEFAULTUSER}](tg://user?id={USERID})"


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""             
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


uptime = get_readable_time((time.time() - StartTime))


@bot.on(admin_cmd(outgoing=True, pattern="elites$"))
@bot.on(sudo_cmd(pattern="elites$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)

    if MAFIA_IMG:
        SAVAGE_caption = f"**{CUSTOM_ALIVE_TEXT}**\n\n"
        SAVAGE_caption += f"ββββββββββββββββββββββββββββ\n"
        SAVAGE_caption += f"__π£ πππππ΄πΌ πππ°πππ π£__\n\n"
        SAVAGE_caption += f"β° ππ΄π»π΄ππ·πΎπ½ ππ΄πππΈπΎπ½  : `1.15.0`\n\n"
        SAVAGE_caption += f"β° π΄π»πΈππ΄π ππ΄πππΈπΎπ½ : `{elitesbotversion}`\n\n"
        SAVAGE_caption += f"β° πΌπ π±πΎππ : {mention}\n\n"
        SAVAGE_caption += f"β° πππΏπΏπΎππ : [πΆππΎππΏ](t.me/eLITES_userbot)\n\n"
        SAVAGE_caption += f"β° ππΏ ππΈπΌπ΄ : `{uptime}\n`"

        await alive.client.send_file(
            alive.chat_id, MAFIA_IMG, caption=SAVAGE_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"**{CUSTOM_ALIVE_TEXT}**\n\n"
            f"ββββββββββββββββββββββββββββ\n"
            f"__π£ πππππ΄πΌ πππ°πππ π£__\n\n"
            f"β° ππ΄π»π΄ππ·πΎπ½ ππ΄πππΈπΎπ½  :** `1.15.0`\n\n"
            f"β° π΄π»πΈππ΄π ππ΄πππΈπΎπ½ :**`{elitesbotversion}`\n\n"
            f"β° πΌπ π±πΎππ :** {mention}\n\n"
            f"β° πππΏπΏπΎππ : [πΆππΎππΏ](t.me/ELITES_userbot)\n\n"
            f"β° ππΏ ππΈπΌπ΄ : `{uptime}\n`"
        )
