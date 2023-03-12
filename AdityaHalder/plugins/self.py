import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from AdityaHalder.modules.clientbot.clientbot import client
from AdityaHalder.modules.helpers.command import commandpro
from AdityaHalder.modules.helpers.decorators import sudo_users_only, errors
from AdityaHalder.utilities.misc import SUDOERS

@Client.on_message(commandpro(["op", "x", ".op", "wow", "nice", "beautiful"]) & filters.me)
async def downloader(_, message: Message):
    targetcontent = message.reply_to_message
    downloadtargetcontent = await client.download_media(targetcontent)
    send = await client.send_document("me", downloadtargetcontent)
    os.remove(downloadtargetcontent)


__MODULE__ = "Sᴇʟғ"
__HELP__ = f"""
**🥀 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙰𝙽𝚈 𝚂𝙴𝙻𝙵-𝙳𝙴𝚂𝚃𝚁𝚄𝙲𝚃 𝙼𝙴𝙳𝙸𝙰 𝙰𝙽𝙳 𝚂𝙰𝚅𝙴 𝙸𝚃 𝚃𝙾 𝚈𝙾𝚄𝚁 𝚂𝙰𝚅𝙴 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 ✨**

**𝚄𝚂𝙰𝙶𝙴 ✨:**
`op|.op` - **𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝚂𝙴𝙻𝙵-𝙳𝙴𝚂𝚃𝚁𝚄𝙲𝚃 𝙿𝙷𝙾𝚃𝙾 𝙾𝚁 𝚅𝙸𝙳𝙴𝙾 𝚃𝙾 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 🥂.**
"""
