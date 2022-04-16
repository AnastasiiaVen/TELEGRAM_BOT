import random
board = ["X", "X", 3, "O", "X", "O", "O", "O", "X"]




def take_NPC_turn(player_token):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    valid = False
    while not valid:
        for each in win_coord:
            if "XO" not in each:
                NPC_turn = random.randint(0, len(each) - 1)
                valid = True
        else:
            avalible = False
            while not avalible:   
                NPC_turn = random.randint(1, 9)
                if (str(board[NPC_turn-1]) not in "XO"):
                    board[NPC_turn-1] = player_token
                    avalible = True
            valid = True


        

print()
print(board)
take_NPC_turn("test")
print(board)
        
