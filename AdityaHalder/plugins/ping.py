import requests
from datetime import datetime
from pyrogram import filters, Client
from AdityaHalder.utilities.misc import SUDOERS
# ping checker

@Client.on_message(filters.command(["ping"], ["/", ".", "!"]) & SUDOERS)
async def ping(Client, message):
    start = datetime.now()
    loda = await message.reply_text("**» 𝙳𝙷𝙸𝙼𝙰𝙽 𝚄𝚂𝙴𝚁 𝙱𝙾𝚃**")
    end = datetime.now()
    mp = (end - start).microseconds / 1000
    await loda.edit_text(f"**🤖 𝙿𝙾𝙽𝙶\n»** `{mp} ms`")


__MODULE__ = "Pɪɴɢ"
__HELP__ = f"""
**🥀 𝙲𝙷𝙴𝙲𝙺 𝚈𝙾𝚄𝚁 𝙳𝙷𝙸𝙼𝙰𝙽 𝚄𝚂𝙴𝚁𝙱𝙾𝚃 𝙿𝙸𝙽𝙶.**

`.ping` - **𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙲𝙾𝙼𝙼𝙰𝙽𝙳 𝚃𝙾 𝙲𝙷𝙴𝙲𝙺**
"""
