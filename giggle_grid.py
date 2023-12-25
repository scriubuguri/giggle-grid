#!/usr/bin/env python
#this is a grid of giggles aka tik-tak-toe game

#making the board for the game and the players 
your_board = [" "] * 9


def print_board():
    print(your_board[0] + " | " + your_board[1] + " | " + your_board[2])
    print("---------")
    print(your_board[3] + " | " + your_board[4] + " | " + your_board[5])
    print("---------")
    print(your_board[6] + " | " + your_board[7] + " | " + your_board[8])


#defining the fill_board function
def fill_board(marker):
    if marker == "X":
        player = 1
    elif marker == "O":
        player = 2
    print("Your turn player " + str(player))

    choice = int(input("Choose a number between 0 and 8 for your position: "))
    if your_board[choice] == " ":
        your_board[choice] = marker
    else:
        print("That space is already taken. Please choose another space.")


#defining the check_winner function
def check_winner():
    if your_board[0] == your_board[1] == your_board[2] != " ":
        print(your_board[0] + " wins!")
        return True
    elif your_board[3] == your_board[4] == your_board[5] != " ":
        print(your_board[3] + " wins!")
        return True
    elif your_board[6] == your_board[7] == your_board[8] != " ":
        print(your_board[6] + " wins!")
        return True
    elif your_board[0] == your_board[3] == your_board[6] != " ":
        print(your_board[0] + " wins!")
        return True
    elif your_board[1] == your_board[4] == your_board[7] != " ":
        print(your_board[1] + " wins!")
        return True
    elif your_board[2] == your_board[5] == your_board[8] != " ":
        print(your_board[2] + " wins!")
        return True
    elif your_board[0] == your_board[4] == your_board[8] != " ":
        print(your_board[0] + " wins!")
        return True
    elif your_board[2] == your_board[4] == your_board[6] != " ":
        print(your_board[2] + " wins!")
        return True
    else:
        return False 


print_board()
while True:
    fill_board("X")
    print_board()
    if check_winner():
        break
    fill_board("O")
    print_board()
    if check_winner():
        break
   

