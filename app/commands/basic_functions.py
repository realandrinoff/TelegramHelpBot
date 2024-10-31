from telegram import Update # type: ignore
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, ConversationHandler, MessageHandler, filters, Updater # type: ignore

class BasicCommands:
    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text(f'Hello {update.effective_user.first_name}')

    async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        pass

