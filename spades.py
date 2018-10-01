# Author: Reilly Bova
# Date:   30 September 2018
# File:   spades.py
# About:  The main file for my "Spades" python program for the terminal

import os
from game import Game
from spades_utils import *

# Welcome message for the user
def welcome():
    os.system("clear")
    print(HEADER)
    hello_msg = ("Welcome to a game of Spades! This game is for four (4) players! At any time, you may enter 'q' to quit and 'r' to read the rules.\n\n"
                 "Please note that you must press the 'Enter' key after typing your inputs in order to submit it to the game (this requirement prevents accidental input/keystrokes)\n\n"
                 "Press any (other) key to continue! We recommend you read the rules now if you are new to Spades!")
    handle_input(hello_msg, WIPE)

# Handles game setup and invokes play
def run_game():
    # Select the winning value
    winning_value = 1
    while (True):
        winning_value = handle_input("Please enter the number of points required to win (traditionally 500):")
        try:
            winning_value = int(winning_value)
            if (winning_value <= 0):
                print("The winning value should be positive!")
            elif (winning_value > 1000):
                print("The winning value should be less than 1000!")
            elif (winning_value % 50 != 0):
                print("The winning value should be divisible by 50!")
            else:
                break
        except:
            winning_value = 1
            print("The winning value must be a number!")

    wipe_screen()
    spades = Game(winning_value)

    # Set passwords, and start the game
    spades.set_pins()
    begin_msg = handle_input("The game will now start! Press any key to begin...", WIPE)
    spades.run()

# Master method of script
def main():
    welcome()
    run_game()
    quit()

main()
