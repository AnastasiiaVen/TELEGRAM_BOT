import random
board = ["X", 2, "O", 4, 5, "X", 7, "X", "O"]

def take_NPC_turn(player_token):
    valid = False
    while not valid:
        NPC_turn = random.randint(1, 9)
        if (str(board[NPC_turn-1]) not in "XO"):
            board[NPC_turn-1] = player_token
            valid = True

print()
print(board)
take_NPC_turn("test")
print(board)
        
