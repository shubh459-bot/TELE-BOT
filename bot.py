import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Your Bot Token
BOT_TOKEN = '8155687165:AAH2IZKDVLZj4UnBvSHFm9wrtdnEHtPCwOA'

# Random welcome messages
WELCOME_MESSAGES = [
    "👋 Hey there! Ready to explore?",
    "✨ Welcome aboard, my friend!",
    "🚀 Let's get started with something awesome!",
    "🌟 Hello Superstar! What would you like today?",
    "🎯 Choose an option and let's go!"
]

# Start Command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("ℹ️ About", callback_data='about'),
            InlineKeyboardButton("❓ Help", callback_data='help')
        ],
        [
            InlineKeyboardButton("💬 Contact", url='https://t.me/trexshubh')  # Change to your username
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    welcome_text = random.choice(WELCOME_MESSAGES)

    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")
    await update.message.reply_text(
        welcome_text,
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

# Button Handler
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'about':
        keyboard = [
            [InlineKeyboardButton("🔙 Back", callback_data='back')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "ℹ️ *About this Bot*:\n\n"
            "This bot is built with ❤️ using Python.\n"
            "Enjoy an interactive experience!",
            parse_mode='Markdown',
            reply_markup=reply_markup
        )

    elif query.data == 'help':
        keyboard = [
            [InlineKeyboardButton("🔙 Back", callback_data='back')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "❓ *Need Help?*\n\n"
            "👉 Click the buttons to navigate.\n"
            "👉 Contact admin for personal support.",
            parse_mode='Markdown',
            reply_markup=reply_markup
        )

    elif query.data == 'back':
        await start(update, context)

# Main Function
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    print("Bot is running and more attractive now!")
    app.run_polling()

if __name__ == '__main__':
    main()
