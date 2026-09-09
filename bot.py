import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]

WELCOME = """🙏 Welcome to BSL Living God AI Bot.

I am here to provide information about BSL Living God TEMPLE.

Send me a message and I will reply."""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME)

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🙏 Thank you for your message. BSL Living God AI Bot is online."
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, reply)
    )

    print("BSL Living God AI Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
