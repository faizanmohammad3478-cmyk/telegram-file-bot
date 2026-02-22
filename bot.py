import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = await update.message.reply_text("Downloading file...")

    file = await update.message.document.get_file()
    file_path = update.message.document.file_name

    await file.download_to_drive(file_path)

    await msg.edit_text("Uploading file...")

    with open(file_path, "rb") as f:
        response = requests.put(
            f"https://transfer.sh/{file_path}",
            data=f
        )

    download_link = response.text.strip()

    await msg.edit_text(f"Done ✅\n\nDownload here:\n{download_link}")

    os.remove(file_path)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.Document.ALL, handle_file))
app.run_polling()
