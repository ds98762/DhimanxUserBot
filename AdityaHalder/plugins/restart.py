import os
import shutil
import asyncio
from git import Repo
from pyrogram.types import Message
from pyrogram import filters, Client
from git.exc import GitCommandError, InvalidGitRepositoryError
from AdityaHalder.modules.helpers.basics import edit_or_reply
from AdityaHalder.modules.helpers.filters import command
from AdityaHalder.utilities.misc import SUDOERS


@Client.on_message(command(["restart", "reboot"]) & filters.me)
async def restart(client, m: Message):
    reply = await m.edit("**🔁 𝚁𝙴𝚂𝚃𝙰𝚁𝚃𝙸𝙽𝙶 🔥 ...**")
    
    await reply.edit(
        "🥀 𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈 𝚁𝙴𝚂𝚃𝙰𝚁𝚃𝙴𝙳\n𝙳𝙷𝙸𝙼𝙰𝙽 シ︎ 𝚄𝚂𝙴𝚁𝙱𝙾𝚃 🔥 ...\n\n💕 Pʟᴇᴀsᴇ Wᴀɪᴛ 1-2 MɪN Fᴏʀ\nLᴏᴀᴅ Usᴇʀ Pʟᴜɢɪɴs ✨ ...</b>"
    )
    os.system(f"kill -9 {os.getpid()} && python3 -m modules")





__MODULE__ = "𝚁𝙴𝚂𝚃𝙰𝚁𝚃"
__HELP__ = f"""
`.restart` **- 𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙲𝙼𝙳 𝚃𝙾 𝚁𝙴𝚂𝚃𝙰𝚁𝚃 𝙳𝙷𝙸𝙼𝙰𝙽 𝚄𝚂𝙴𝚁𝙱𝙾𝚃 **

"""
