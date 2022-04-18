

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram_game import *
import random

board = list(range(1, 10))

def hi_command(update: Update, context: CallbackContext):
    
    update.message.reply_text(f'Hi {update.effective_user.first_name}')

def help_command(update: Update, context: CallbackContext):
    
    update.message.reply_text(f'/hi\n/help\n/start')


def start_game_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'Начало игры!')
    


def draw_board(update: Update, context: CallbackContext):
    arg = ""
    for i in range(3):
        if i == 0: arg += f'{"-" * 15}\n'
        arg += f'| {board[0 + i * 3]} | {board[1 + i * 3]} | {board[2 + i * 3]} |\n'
        if i == 2: arg += f'{"-" * 15}\n'
    update.message.reply_text(f'Текущее состояние игрового поля:\n{arg}')

def who_is_first(update: Update, context: CallbackContext):
    draw = False
    while not draw:
        hidden_number = random.randint(0,10)
        update.message.reply_text(f'Я выберу цифру от нуля до 9. Введите цифру от 0 до 9. Если вы будете ближе, чем NPC, к моей цифре - ваша очередь будет первой!')
        user_choice = update.message.text.strip()

        npc_choice = random.randint(0,10)
        if abs(hidden_number - user_choice) == abs(hidden_number - npc_choice):
            update.message.reply_text(f"Я выбрал: {hidden_number}. Ты взял: {user_choice}, но NPC взял: {npc_choice}. Это означает ничью, ещё раз!")
        elif abs(hidden_number - user_choice) > abs(hidden_number - npc_choice):
            update.message.reply_text(f"Я выбрал: {hidden_number}. Ты взял: {user_choice}, но NPC взял {npc_choice}. NPC ходит первым!")
            draw = True
            return 'NPC'
        else:
            print(f"Я выбрал: {hidden_number}. Ты взял: {user_choice}, но NPC взял {npc_choice}. Ты ходишь первым! ")
            draw = True
            return 'Player'


