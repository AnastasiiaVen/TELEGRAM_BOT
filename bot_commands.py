

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def hi_command(update: Update, context: CallbackContext):
    
    update.message.reply_text(f'Hi {update.effective_user.first_name}')

def help_command(update: Update, context: CallbackContext):
    
    update.message.reply_text(f'/hi\n/help')