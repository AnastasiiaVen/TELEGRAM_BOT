# from telegram import Update
# from telegram.ext import Updater, CommandHandler, CallbackContext
# import bot_commands as bc
# import random

# board = list(range(1, 10))


# def take_NPC_turn(player_token):
#     win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
#     valid = False
#     while not valid:
#         for each in win_coord:
#             if "XO" not in each:
#                 NPC_turn = random.randint(0, len(each) - 1)
#                 valid = True
#         else:
#             available = False
#             while not available:
#                 NPC_turn = random.randint(1, 9)
#                 if (str(board[NPC_turn - 1]) not in "XO"):
#                     board[NPC_turn - 1] = player_token
#                     available = True
#             valid = True


# def take_input(player_token):
#     valid = False
#     while not valid:
#         player_answer = input("Куда поставим " + player_token + "? ")
#         try:
#             player_answer = int(player_answer)
#         except:
#             print("Некорректный ввод. Вы уверены, что ввели число?")
#             continue
#         if player_answer >= 1 and player_answer <= 9:
#             if (str(board[player_answer - 1]) not in "XO"):
#                 board[player_answer - 1] = player_token
#                 valid = True
#             else:
#                 print("Эта клеточка уже занята")
#         else:
#             print("Некорректный ввод. Введите число от 1 до 9, чтобы сделать ход.")


# def main(board):
#     counter = 0
#     win = False
#     first_is = who_is_first()
#     while not win:
#         bc.draw_board(board)
#         if first_is == 'Player':
#             if counter%2 == 0:
#                 take_input("X")
#                 print('Ход NPC.')
#             else:
#                 take_NPC_turn("O")
#         elif first_is == 'NPC':
#             if counter%2 == 0:
#                 take_NPC_turn("X")
#             else:
#                 take_input("O")
#                 print('Ход NPC.')
#             # take_input("O")
#         counter += 1
#         if counter > 4:
#             tmp = check_win(board)
#             if tmp:
#                 print(tmp, "выиграл!")
#                 win = True
#                 break
#         if counter == 9:
#             print("Ничья!")
#             break
#     bc.draw_board(board)


# main(board)
