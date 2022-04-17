from bot_commands import *
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


updater = Updater('5386113366:AAFMfSe4zMkKkdSyjEVzurctlMZ4y6b0O58')

updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))

print('Server start.')
updater.start_polling()
updater.idle()