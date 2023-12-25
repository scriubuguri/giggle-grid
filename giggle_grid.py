#!/usr/bin/env python
#this is a tik-tak-toe game

#option for player to play again 
def play_again():
    return input("Do you want to play again? (yes/no): ").lower().startswith('y')

while True:
    #making the board for the game 
    your_board = [" "] * 9

    def print_board():
        print(your_board[0] + " | " + your_board[1] + " | " + your_board[2])
        print("---------")
        print(your_board[3] + " | " + your_board[4] + " | " + your_board[5])
        print("---------")
        print(your_board[6] + " | " + your_board[7] + " | " + your_board[8])

    def choose_marker():
        marker = input("Player 1, choose your marker ('X' or 'O'): ").upper()
        while marker not in ['X', 'O']:
            print("Invalid choice. Please choose 'X' or 'O'.")
            marker = input("Player 1, choose your marker ('X' or 'O'): ").upper()
        return marker

    player1_marker = choose_marker()
    player2_marker = 'X' if player1_marker == 'O' else 'O'

    #defining the fill_board function
    def fill_board(marker, player):
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
            print("Nobody wins!") 


    print_board()
    player_turn = 1
    while True:
        fill_board(player1_marker if player_turn == 1 else player2_marker, player_turn)
        print_board()
        if check_winner():
            print("Congratulations! Player " + str(player_turn) + " wins!")
            break

        player_turn = 3 - player_turn

    #ask if players want to play again
    if not play_again():
        break

