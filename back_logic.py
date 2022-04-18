#
import random
#from logic import *




def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False


# def draw_board(board):
#     print("-" * 13)
#     for i in range(3):
#         print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
#         print("-" * 13)

