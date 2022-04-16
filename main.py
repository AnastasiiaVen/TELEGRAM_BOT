from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')


updater = Updater('5352372609:AAEk1VYI9_G-2-q57PYGlTP7RUN0mO4wq4A')

updater.dispatcher.add_handler(CommandHandler('hello', hello))
print('I started')

updater.start_polling()
updater.idle()
