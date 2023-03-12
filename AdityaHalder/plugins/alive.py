# AdityaHalder
import asyncio
from pyrogram import *
from pyrogram.types import *
from AdityaHalder.modules.helpers.basics import edit_or_reply
from AdityaHalder.modules.helpers.filters import command
from AdityaHalder.utilities.misc import SUDOERS


@Client.on_message(command(["alive"]) & SUDOERS)
async def mother_chod(client: Client, message: Message):
    await edit_or_reply(message, "**🥀 𝙸 𝙰𝙼 𝙰𝙻𝙸𝚅𝙴 𝙼𝚈 𝙳𝙴𝙰𝚁 𝙳𝙷𝙸𝙼𝙰𝙽 𝙼𝙰𝚂𝚃𝙴𝚁 🍷✨ ...**")



__MODULE__ = "Aʟɪᴠᴇ"
__HELP__ = f"""
**🥀 𝚃𝙴𝚂𝚃 𝚈𝙾𝚄𝚁 𝙱𝙾𝚃 𝚆𝙾𝚁𝙺𝙸𝙽𝙶 𝙾𝚁 𝙽𝙾𝚃.**

`.alive` - **𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙲𝙾𝙼𝙼𝙰𝙽𝙳 𝚃𝙾 𝙲𝙷𝙴𝙲𝙺**
"""
