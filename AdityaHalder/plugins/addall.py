import asyncio
from pyrogram import Client, filters 
from pyrogram.types import Message
from AdityaHalder.modules.helpers.basics import edit_or_reply
from AdityaHalder.modules.helpers.filters import command
from AdityaHalder.modules.helpers.command import commandpro
from AdityaHalder.utilities.misc import SUDOERS


@Client.on_message(command(["addall", "inviteall"]) & SUDOERS)
async def inviteall(client: Client, message: Message):
    kaal = await edit_or_reply(message, "Processing ...")
    text = message.text.split(" ", 1)
    queryy = text[1]
    chat = await client.get_chat(queryy)
    tgchat = message.chat
    await kaal.edit_text(f"**🥀 𝙸𝙽𝚅𝙸𝚃𝙸𝙽𝙶 𝚄𝚂𝙴𝚁𝚂 𝙵𝚁𝙾𝙼 {chat.username} ✨ ...**")
    async for member in client.iter_chat_members(chat.id):
        user= member.user
        kal= ["online", "offline" , "recently", "within_week"]
        if user.status in kal:
           try:
            await client.add_chat_members(tgchat.id, user.id)
           except Exception as e:
            mg= await client.send_message("me", f"error-   {e}")
            await asyncio.sleep(0.3)
            await mg.delete()



__MODULE__ = "𝙰𝙳𝙳 𝙰𝙻𝙻"
__HELP__ = f"""
`.addall [@groupusername]` **- 𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙲𝙾𝙼𝙼𝙰𝙽𝙳 𝚃𝙾 𝙰𝙳𝙳 𝙼𝙴𝙼𝙱𝙴𝚁𝚂 𝙸𝙽 𝚈𝙾𝚄𝚁 𝙲𝙷𝙰𝚃**

**Ex:-** `.addall @DHIMAN_FEELINGS`
"""
