import random
import back_logic as bl
import math


board = list(range(1, 10))


def draw_board(board):
    print("-" * 13)
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("-" * 13)


def who_is_first():
    draw = False
    while not draw:
        hidden_number = random.randint(0,10)
        user_choice = int(input("I'll pick a digit zero to 9. Insert digit from 0 to 9. If you will be closer than NPC to my digit - your turn will be first!"))
        npc_choice = random.randint(0,10)
        if abs(hidden_number - user_choice) == abs(hidden_number - npc_choice):
            print(f"I'd picked {hidden_number}. You took {user_choice}, but NPC took {npc_choice}. This means a draw! One more time")
        elif abs(hidden_number - user_choice) > abs(hidden_number - npc_choice):
            print(f"I'd picked {hidden_number}. You took {user_choice}, but NPC took {npc_choice}. NPC do first turn: ")
            draw = True
            return 'NPC'
        else:
            print(f"I'd picked {hidden_number}. You took {user_choice}, but NPC took {npc_choice}. You do first turn: ")
            draw = True
            return 'Player'


def take_NPC_turn(player_token):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    valid = False
    while not valid:
        for each in win_coord:
            if "XO" not in each:
                NPC_turn = random.randint(0, len(each) - 1)
                valid = True
        else:
            available = False
            while not available:
                NPC_turn = random.randint(1, 9)
                if (str(board[NPC_turn - 1]) not in "XO"):
                    board[NPC_turn - 1] = player_token
                    available = True
            valid = True


def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token + "? ")
        try:
            player_answer = int(player_answer)
        except:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer - 1]) not in "XO"):
                board[player_answer - 1] = player_token
                valid = True
            else:
                print("Эта клеточка уже занята")
        else:
            print("Некорректный ввод. Введите число от 1 до 9, чтобы сделать ход.")


def main(board):
    counter = 0
    win = False
    first_is = who_is_first()
    while not win:
        draw_board(board)
        if first_is == 'Player':
            if counter%2 == 0:
                take_input("X")
                print('Ход NPC.')
            else:
                take_NPC_turn("O")
        elif first_is == 'NPC':
            if counter%2 == 0:
                take_NPC_turn("X")
            else:
                take_input("O")
                print('Ход NPC.')
            # take_input("O")
        counter += 1
        if counter > 4:
            tmp = bl.check_win(board)
            if tmp:
                print(tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(board)


main(board)