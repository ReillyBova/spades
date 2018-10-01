# Author: Reilly Bova
# Date:   30 September 2018
# File:   spades_utils.py
# About:  A collection of utility functions for my "Spades" python program

import os

# Types of input flow
CONTINUE = 0
WIPE = 1
YORN = 2

# Special inputs
QUIT = 'q'
RULES = 'r'

# Useful stdout strings
# Spades text drawn by online ASCII font art generator: http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Spades
LINE_LEN = 138
DIVIDER = '——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————\n'
HEADER = ("♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠\n"
          "♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠\n"
          "♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠    _________                 .___               ♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠\n"
          "♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠   /   _____/__________     __| _/____   ______  ♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠\n"
          "♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠   \_____  \\\____ \__  \   / __ |/ __ \ /  ___/  ♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠\n"
          "♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠   /        \  |_> > __ \_/ /_/ \  ___/ \___ \   ♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠\n"
          "♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠  /_______  /   __(____  /\____ |\___  >____  >  ♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠\n"
          "♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠          \/|__|       \/      \/    \/     \/   ♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠\n"
          "♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠\n"
          "♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠\n\n")

# Handle quitting mid-game
def kill_game(msg, type):
    # Wipe only if we were otherwise going to
    if (type == WIPE):
        wipe_screen()
    response = None
    while (True):
        response = input("Are you sure you want to quit the game? (y/n)\n>>>").upper()
        if (response == 'YES' or response == 'Y'):
            wipe_screen()
            quit()
        elif (response == 'NO' or response == 'N'):
            if (type == WIPE):
                wipe_screen()
            # "Go back" to the original prompt (and hope the user doesn't descend much further into the call stack)
            return handle_input(msg, type)

# Handle displaying the rules
def show_rules(msg, type):
    # Wipe only if we were otherwise going to
    if (type == WIPE):
        wipe_screen()
    rules = ("Spades is a fun & competitive card game for four (4) players split into two (2) teams. \n\n"
             "(1 — Overview) Spades is played in a series of rounds that continue until a team has won. In a single round, there are three (3) stages: bidding, gameplay, and scoring. Descriptions of these stages follow.\n\n"

             "(2 — Bidding) After cards are dealt (52 / 4 = 13 per player), a round opens with a bidding stage, during which each player (one player at a time) sees their cards, and then states (aka \"bids\") "
             "the minimum number of hands they expect to win in the round given their cards. Each player's bid is then summed with that of their partner to form the team's \"contract\", which is the number of "
             "hands the team must win, combined (i.e. the total number hands that should be won between the two players of each team). If a team wins more hands in a round than stated in their contract, "
             "the team DOES NOT recieve all the points for those extra hands. Similarly, if a team does not win as many hands in a round as stated in their contract, "
             "they stand to lose points. If a player makes a bid without seeing their cards (a \"blind\"), or if a player states they will win zero (0) cards (a \"nil\"), "
             "special scoring rules are applied. For more on scoring, see Section 4 — Scoring.\n\n"

             "(3 — Gameplay) After the bidding stage, gameplay begins. During each hand of a round, players play exactly one (1) of their 13 cards. "
             "In Spades, there are two classes of suites: in the lower class are clubs (♣), hearts (♥), and diamonds (♦); and up above are the \"trump\" spades (♠). "
             "Rounds begin with the player who won the previous round (or, in the case of the round's start, the player who made the first bid). The card put down by "
             "the leading player of a hand is called the \"lead\" card. This lead card may not be a spade unless a spade has already been played in the round (through other means). "
             "Once the lead card is set, play continues around the group (alternating teams), until all three (3) other players have played. At this point, if there were any spades "
             "played in the 4-card hand, the hand is awarded to whichever player played the highest-ordered spade; otherwise, the hand is awarded to whichever player played the "
             "highest-ordered card that matches the suite of the lead card. Note that when playing a card, a player must always match the winning suite (spade or lead) thus-far of a hand; "
             "if a player is not able to do so, they are free to play a card from whichever suite they choose, including a spade (this is how spades are introduced into a round).\n\n"

             "(4 — Scoring) Once all 13 hands have been played, scoring begins. For teams whose contract contains neither blinds (when a player bets before looking at their cards) nor nils (when a player bets they will "
             "win zero (0) hands), they will lose 10 times their contract number (in points) if they won fewer hands than promised in their contract; if they won at least as many hands as stated, they get 10 points per hand up until the "
             "number in the contract, and one (1) point for each extra hand beyond what the contract states. Additionally, for each extra hand, a team recieves a penalty \"bag\". These bags carry over between rounds, "
             "but only every seventh (7th) bag affects the score. Indeed, every seventh (7th) bag a team earns results in a 100 point penalty against them! If a player bets nil, wins no hands, AND their team member wins no hands, "
             "then the player alone (team member is scored seperately) wins 100 points. If a player bets nil and does not meet these requirements, then the team will lose 100 points. Likewise, if a player bets blind "
             "and wins at least as many hands as stated in the contract, then the player alone wins 100 points and no bags are added for excess. If, however, a player bets blind but fails to win the number of hands on "
             "the contract (supplemented by their partner), then they alone lose 100 points. Note that both players on a team may bet blind and/or nil.\n\n"

             "(5 — Winning) Rounds of Spades are repeated until a team accumulates enough points to pass the winning value (set at the start of the game — traditionally 500). In the case that two teams pass this value at the same time, "
             "the team with the most amount of points wins. Total bags, and then extra rounds, are used as tiebreakers.\n\n"

             "Press any key to return to the game...\n"
             ">>>"
             )
    input(rules)
    if (type == WIPE):
        wipe_screen()
    # "Go back" to the original prompt (and hope the user doesn't descend much further into the call stack
    return handle_input(msg, type)

# Handle getting prompt from user (can wipe screen, enfore Y/N answer, and check for special responses)
def handle_input(msg, type=(CONTINUE)):
    response = input(msg + "\n>>>")
    if (response == QUIT):
        return kill_game(msg, type)
    elif (response == RULES):
        return show_rules(msg, type)
    else:
        if (type == WIPE):
            wipe_screen()
        if (type == YORN):
            response = response.upper()
            if (response == 'NO' or response == 'N'):
                return False
            elif (response == 'YES' or response == 'Y'):
                return True
            else:
                return handle_input(msg, type)

        return response

# Wipe terminal screen (hard erase)
# TODO: This is CRAZY SLOW — is there a more efficient way without potentially revealing info written to the terminal previously?
def wipe_screen():
    os.system("reset")
