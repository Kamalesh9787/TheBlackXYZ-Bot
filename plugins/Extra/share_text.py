# Credit @TheBlackXYZ.
# Please Don't remove credit.
# TheBlackXYZBotz Forever !
# Thanks You For Help Us In This Amazing Creativity 
# Thanks You For Giving Me Credit @TheBlackXYZBotz
# For Any ERROR Please Contact Me -> Telegram ->@TheBlackXYZBotz & Insta @TheBlackXYZ
# Please Love & Support 💗💗🙏


import os
from pyrogram import Client, filters
from urllib.parse import quote
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command(["share_text", "share", "sharetext"]))
async def share_text(client, message):
    TheBlackXYZBotz = await client.ask(chat_id = message.from_user.id, text = "Now Send me your text.")
    if TheBlackXYZBotz and (TheBlackXYZBotz.text or TheBlackXYZBotz.caption):
        input_text = TheBlackXYZBotz.text or TheBlackXYZBotz.caption
    else:
        await TheBlackXYZBotz.reply_text(
            text=f"**Notice:**\n\n1. Send Any Text Messages.\n2. No Media Support\n\n**Any Question Join Support Chat**",               
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Updates Channel", url=f"https://t.me/TheBlackXYZBotz")]])
            )                                                   
        return
    await TheBlackXYZBotz.reply_text(
        text=f"**Here is Your Sharing Text 👇**\n\nhttps://t.me/share/url?url=" + quote(input_text),
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("♂️ Share", url=f"https://t.me/share/url?url={quote(input_text)}"),InlineKeyboardButton("✗ Update ✗", url="t.me/TheBlackXYZBotz")]]]))
