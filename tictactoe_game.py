
# Create a Tic Tac Toe game.

# imported random module.
import random

# Positions on the board is taken in a list format.
list_number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Choice given to players to choose their mark.
letter_values = {1: "X", 2: "O"}

# Print an empty board in the starting of the game using this boards() function.
def boards():
    print("      |      |      ")
    print("      |      |      ")
    print("      |      |      ")
    print("--------------------")
    print("      |      |      ")
    print("      |      |      ")
    print("      |      |      ")
    print("--------------------")
    print("      |      |      ")
    print("      |      |      ")
    print("      |      |      ")

# This function fills in the board with the list values.
def board(board_name):
    print("      |      |      ")
    print(" ", board_name[7], "  |  ", board_name[8], " |  ", board_name[9], "    ")
    print("      |      |      ")
    print("--------------------")
    print("      |      |      ")
    print(" ", board_name[4], "  |  ", board_name[5], " |  ", board_name[6], "    ")
    print("      |      |      ")
    print("--------------------")
    print("      |      |      ")
    print(" ", board_name[1], "  |  ", board_name[2], " |  ", board_name[3], "    ")
    print("      |      |      ")

# Function used for placing the player's mark on the board.
def place_marker(board_n, marker, position):
    board_n[position] = marker

# Initially we take the whole board empty by creating a list of space values.
final_list = [" "]*10

# Function used for asking the player to play again, if interested.
def replay():
    play_again = input("Do you wanna replay? There's always a second chance here!\nYes or No\n").lower()
    if play_again == "yes" or play_again == "y":
        tic_tac_toe()
    else:
        print("No issue! Play some other time.")

# The main function to start the game.
def tic_tac_toe():
    print("Hello players!\nWelcome to TIC TAC TOE!!!")
    print("*******************************************")
    x = input("Do you wanna play tic tac toe game?\nYes/No").lower()
    if x == "yes" or x == "y":
        # prints out an empty board using board() function.
        boards()
        # inputs the players name.
        player1 = input("Please enter Player1 name here:")
        player2 = input("Please enter Player2 name here:")
        
        # input the choice of player's mark.
        choice_player1 = input(player1 + " which character do you want?\nX or O").upper()
        choice_player2 = input(player2 + " which character do you want?\nX or O").upper()

        print(player1, "has ", choice_player1, "as their choice!")
        print(player2, "has ", choice_player2, "as their choice!")
        print("Let's start the game!")
        print("Let the computer decide whose chance will be first!!!")
        # using the random module, we choose which player's chance comes first.
        first_chance = random.randint(1, 2)

        if first_chance == 1:
            print(player1, "your chance is first!")
            print(player2, "your chance is second!")

        elif first_chance == 2:
            print(player2, "your chance is first!")
            print(player1, "your chance is second!")

        while True:
            if first_chance == 1:
                next_chance1 = int(input(player1 + " chance:"))
                next_chance2 = int(input(player2 + " chance:"))

            elif first_chance == 2:
                next_chance2 = int(input(player2 + " chance:"))
                next_chance1 = int(input(player1 + " chance:"))

            final_list.append(choice_player1)
            final_list.append(choice_player2)
            place_marker(final_list, choice_player1, next_chance1)
            place_marker(final_list, choice_player2, next_chance2)

            board(final_list)
            # print('\n' * 100)
            # checking for winning condition.
            if final_list[1] == final_list[2] == final_list[3] == choice_player1 or \
                    final_list[4] == final_list[5] == final_list[6] == choice_player1 or \
                    final_list[7] == final_list[8] == final_list[9] == choice_player1 or \
                    final_list[1] == final_list[4] == final_list[7] == choice_player1 or \
                    final_list[2] == final_list[5] == final_list[8] == choice_player1 or \
                    final_list[3] == final_list[6] == final_list[9] == choice_player1 or \
                    final_list[1] == final_list[5] == final_list[9] == choice_player1 or \
                    final_list[3] == final_list[5] == final_list[7] == choice_player1:
                print("CONGRATULATIONS!!", player1, "has won!!!")
                break
            elif final_list[1] == final_list[2] == final_list[3] == choice_player2 or \
                    final_list[4] == final_list[5] == final_list[6] == choice_player2 or \
                    final_list[7] == final_list[8] == final_list[9] == choice_player2 or \
                    final_list[1] == final_list[4] == final_list[7] == choice_player2 or \
                    final_list[2] == final_list[5] == final_list[8] == choice_player2 or \
                    final_list[3] == final_list[6] == final_list[9] == choice_player2 or \
                    final_list[1] == final_list[5] == final_list[9] == choice_player2 or \
                    final_list[3] == final_list[5] == final_list[7] == choice_player2:
                print("CONGRATULATIONS!!", player2, "has won!!!")
                break
            elif (final_list[1] != " ") and (final_list[2] != " ") and (final_list[3] != " ")\
                    and (final_list[4] != " ") and (final_list[5] != " ") and (final_list[6] != " ")\
                    and (final_list[7] != " ") and (final_list[8] != " ") and (final_list[9] != " "):
                print("All spaces are filled. It's a draw!!!")
                break
            else:
                continue
        for i in range(len(final_list)):
            final_list[i] = " "
        replay()
    elif x == "no":
        print("No issue! Play some other time.")
    

tic_tac_toe()




















