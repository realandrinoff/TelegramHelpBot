import logging
import os
import sys
from commands.basic_functions import BasicCommands
from commands.direct_messages import DirectMessages
from telegram import Update # type: ignore
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, ConversationHandler, MessageHandler, filters, Updater # type: ignore


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)



if __name__ == '__main__':
    basic = BasicCommands()
    dm = DirectMessages()
    application = ApplicationBuilder().token(os.getenv('TELEGRAM_TOKEN')).build()
    application.add_handler(CommandHandler('start', basic.start))
    application.run_polling()