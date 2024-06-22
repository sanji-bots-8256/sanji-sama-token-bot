#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>Owner - @Bad_Pirate_LUFFY \n My Channel - <a href=https://t.me/jjustanime>Hindi Sub Anime</a>\nMy Team - <a href=https://t.me/Team_JXG>Team_JXG</a>\nSupport Group - <a href=https://t.me/Request4anime>Support</a>\n\n👨‍💻 Developed by - <a href=https://t.me/Urr_Sanjii>𝐒ᴀɴJɪ 𝐒αᴍᴀ™</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pas
