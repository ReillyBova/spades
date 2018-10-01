# Author: Reilly Bova
# Date:   30 September 2018
# File:   card.py
# About:  Implements a playing card

class Card:
    def __init__(self, id):
        self.id = id

        # Identify Suite
        if (id < 13):
            self.suite = '♦'
            self.suiteID = 0
        elif (id < 26):
            self.suite = '♣'
            self.suiteID = 1
        elif (id < 39):
            self.suite = '♥'
            self.suiteID = 2
        else:
            self.suite = '♠'
            self.suiteID = 3

        # Identify Order
        rem = (id % 13) + 2
        self.orderID = rem
        if (rem <= 10):
            self.order = str(rem)
        elif (rem == 11):
            self.order = 'J'
        elif (rem == 12):
            self.order = 'Q'
        elif (rem == 13):
            self.order = 'K'
        elif (rem == 14):
            self.order = 'A'


    # For representation (multi-line, so returning array makes it easier to arrange cards horizontally later)
    def viz(self):
        symbol = self.suite
        ord = self.order[0]
        if (len(self.order) == 2):
            pad = self.order[1]
        else:
            pad = ' '

        # Style influenced by https://codereview.stackexchange.com/questions/82103/ascii-fication-of-playing-cards
        return [ "┌───────┐",
                f"│{ord}{pad}     │",
                f"│   {symbol}   │",
                f"│     {ord}{pad}│",
                 "└───────┘"]
