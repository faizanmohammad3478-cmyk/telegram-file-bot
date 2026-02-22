import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = await update.message.reply_text("Generating download link...")

    file = await update.message.document.get_file()
    file_path = file.file_path

    direct_link = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"

    await msg.edit_text(f"Direct Download Link:\n\n{direct_link}")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.Document.ALL, handle_file))
app.run_polling()
