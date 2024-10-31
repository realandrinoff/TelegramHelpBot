from telegram import Update # type: ignore
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, ConversationHandler, MessageHandler, filters, Updater # type: ignore

class DirectMessages:
    async def dm(update: Update, context: ContextTypes.DEFAULT_TYPE)   -> None: 
        pass
    