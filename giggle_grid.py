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

print_board()
