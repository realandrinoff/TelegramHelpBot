import logging
import os

from telegram import Update # type: ignore
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler # type: ignore


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    pass

async def dm(update: Update, context: ContextTypes.DEFAULT_TYPE)   -> None: 
    message = " ".join(context.args)
    await context.bot.send_message(chat_id=os.getenv("YOUR_ID"), text=f"@{update.effective_user.username} {update.effective_user.first_name} says: \n{message}\nTo answer /reply {update.effective_user.id}")


    

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE)   -> None:
    if str(update.effective_user.id) == os.getenv("YOUR_ID"):
        print('authorized')
        id = context.args[0]
        message = []
        for arg in context.args[1:]:
            message.append(arg)
        message = " ".join(message)
        await context.bot.send_message(chat_id=id, text=f"The administrator got back to you: \n{message}")
    else: 
        print(update.effective_user.id, os.getenv("YOUR_ID"))
        print('not authorized')

if __name__ == '__main__':
    application = ApplicationBuilder().token(os.getenv('TELEGRAM_TOKEN')).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('dm', dm))
    application.add_handler(CommandHandler('reply', reply))
    application.run_polling()