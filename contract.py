# Author: Reilly Bova
# Date:   30 September 2018
# File:   contract.py
# About:  Implements a "contract" from Spades. It holds the bids of each player,
#         produces string representations of them, and scores the results of a round

class Contract:
    def __init__(self):
        self.sum = 0
        self.bids = [0, 0]
        self.bidStrings = ["YTB", "YTB"]
        self.blinds = [False, False]

    # Add the bid of player <number> to the contract.
    def add_bid(self, number, bid, blind):
        self.sum += bid
        self.bids[number - 1] = bid
        self.blinds[number - 1] = blind
        self.bidStrings[number - 1] = str(bid)
        if (blind):
            self.bidStrings[number - 1] += 'b'

    # Score the contract at the end of a round
    def eval(self, win1, win2):
        score = 0
        bags = 0
        wins = [win1, win2]

        overflow = (win1 + win2) - self.sum
        for i, bid in enumerate(self.bids):
            # Nil case
            if (bid == 0):
                if (overflow > 0 or (wins[i] != 0)):
                    # Lost nil
                    score -= 100
                    if (self.blinds[i]):
                        # Lost nil AND blind
                        score -= 100
                else:
                    # Met nil
                    score += 100
                    if (self.blinds[i]):
                        # Met nil AND blind
                        score += 100
            # General win case
            elif (overflow >= 0):
                if (self.blinds[i]):
                    # Blinds are PERSONAL!
                    if (wins[i] - bid < 0):
                        score -= 100
                    else:
                        score += 100
                else:
                    # Award points for bid
                    score += bid * 10
            else:
                # Doc as many points as is appropriate
                if (self.blinds[i]):
                    score -= 100
                else:
                    score -= bid * 10

        # Handle Bags
        if (overflow > 0):
            for i, bid in enumerate(self.bids):
                diff = wins[i] - bid
                if (diff > 0):
                    # One bag/point per extra hand
                    score += diff
                    # Blinds don't get bags
                    if (not self.blinds[i]):
                        bags += diff
        return score, bags

    # String representation of contract
    def to_string(self, win1, win2):
        return (f"{{{win1}/{self.bidStrings[0]}, {win2}/{self.bidStrings[1]}}}")
