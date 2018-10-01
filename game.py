# Author: Reilly Bova
# Date:   30 September 2018
# File:   game.py
# About:  Implements a "game" for Spades. Call the constructor, with the winning value,
#         set pins, and then invoke run to simulate a game of Spades.

import getpass
from round import Round
from spades_utils import *

class Game:
    def __init__(self, winning_value):
        self.win = winning_value # Number of points needed to win

        # Initial values
        self.players = ["A1", "B1", "A2", "B2"]
        self.round = 1
        self.scores = [0, 0]
        self.bags = [0, 0]
        self.discarded_bags = [0, 0]

    # Set the 4-digit PIN for each user
    def set_pins(self):
        self.pins = {}
        for player in self.players:
            pin = ''
            while (True):
                msg1 = f"Player {player}, please enter a 4-digit PIN (in the interest of your security, DON'T use a PIN you wouldn't want everyone else knowing after the game is over):\n"
                pin = getpass.getpass(msg1)
                if (not ((len(pin) == 4) and (pin.isnumeric()))):
                    print("Invalid PIN! Try again...")
                else:
                    msg2 = f"If you forget your pin, you will need to quit the game! To confirm, please re-enter your 4-digit PIN:\n"
                    if (pin == getpass.getpass(msg2)):
                        break
                    else:
                        print("PIN mismatch! Try again...")

            self.pins[player] = pin
            wipe_screen()

    # Enforce the 7-bag penalty
    def score_bags(self):
        for i in range(2):
            while (self.bags[i] >= 7):
                self.bags[i] -= 7
                self.discarded_bags[i] += 7
                self.scores[i] -= 100

    # Rotate order of players every round. (First player of a round is the first to bid and lead!)
    def rotate_order(self):
        first = self.players.pop(0)
        self.players.append(first)

    # Return the name of the winning team, or "" if there is no winner
    def winner(self):
        if ((self.scores[0] >= self.win) or (self.scores[1] >= self.win)):
            if (self.scores[0] > self.scores[1]):
                return "A"
            elif (self.scores[1] > self.scores[0]):
                return "B"
            else:
                # Tie breakers
                if (self.bags[0] + self.discarded_bags[0] > self.bags[1] + self.discarded_bags[1]):
                    return "B"
                elif (self.bags[1] + self.discarded_bags[1] > self.bags[0] + self.discarded_bags[0]):
                    return "A"
        return ""

    # Return a formatted string containing info about the game
    def game_header(self):
        return f"Game Score: (A) {self.scores[0]} vs. {self.scores[1]} (B) | Bags: (A) {self.bags[0]} vs. {self.bags[1]} (B) | Goal: {self.win}"

    # Handle the execution/refereeing of a Spades game
    def run(self):
        game_over = False
        while (not game_over):
            # Run a round
            roundResult = Round(self.round, self.players, self.pins, self.game_header())

            # Adjust instance variables as needed based on round results
            self.round += 1
            self.scores[0] += roundResult.scores[0]
            self.scores[1] += roundResult.scores[1]
            self.bags[0] += roundResult.bags[0]
            self.bags[1] += roundResult.bags[1]

            # Setup for next round
            self.score_bags()
            self.rotate_order()
            winner = self.winner()
            game_over = (len(self.winner()) != 0)

            if (not game_over):
                print("Here is the current status of your game:\n")
                print(f"\t{self.game_header()}\n")
                handle_input("Press any key to continue to the next round...", WIPE)

        # End of game message
        handle_input(f"Congrats to Team {winner} on their victory! Here are the final results:\n\n"
                     f"\t{self.game_header()}\n\n"
                     "I hope everyone enjoyed this implementation of Spades! Press any key to end the game...")
