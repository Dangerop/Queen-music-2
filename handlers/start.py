import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, CHANNEL_UPDATES, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgUAAx0CZ80CewABAn7iY0QmDt7nsecHlSDH7oMXmtavNH4AAhMHAALnnCFW1zONdkHrocAeBA")
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f""" ** Hey {message.from_user.mention()}Β , π₯\n\n
ΰΉ This is [{bn}](t.me/{bu}) ,Β  !
β» The most Powerful telegram music  bot with some awesome and useful features.

ββββββββββββββββββ
ΰΉ  All of my command can be used with My command handle : ( / . β’ $ ^ ~ + * ? ) ** """,
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "βΒ AddΒ meΒ toΒ yourΒ Group", url=f"https://t.me/{bu}?startgroup=true"
                       ),
                 ],[
                    InlineKeyboardButton(
                        "π¨ Channel ", url=f"https://t.me/{CHANNEL_UPDATES}"
                    ),
                    InlineKeyboardButton(
                        "π¨ Support ", url=f"https://t.me/{SUPPORT_GROUP}"
                    )
                  ],[
                    InlineKeyboardButton(
                        "π€ Bot Owner ", url=f"https://t.me/{me}"
                    ),
                    InlineKeyboardButton(
                        "π¨βπ» Developer ", url=f"https://t.me/MAFIA_RJ"
                    ),
                  ],[
                    InlineKeyboardButton(
                        "β Inline ", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "π‘ Git repo", url="https://te.legra.ph/file/d3f87fbd9a9337eaaa148.jpg"
                    )]
            ]
       ),
    )

