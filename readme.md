test
`♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠
 ♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠
♠♠♠    _________                 .___               ♠♠♠
♠♠♠   /   _____/__________     __| _/____   ______  ♠♠♠
♠♠♠   \_____  \\____ \__  \   / __ |/ __ \ /  ___/  ♠♠♠
♠♠♠   /        \  |_> > __ \_/ /_/ \  ___/ \___ \   ♠♠♠
♠♠♠  /_______  /   __(____  /\____ |\___  >____  >  ♠♠♠
♠♠♠          \/|__|       \/      \/    \/     \/   ♠♠♠
 ♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠
  ♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠`

I. Running the program
|
|  In order to run spades, change your local directory to /Spades/, and then
|  simply run spades.py using python3 in your terminal
|
|  `$ python3 spades.py`

II. Rules
|
|  Spades is a fun & competitive card game for four (4) players split into two
|  (2) teams.
|
|  (1 — Overview) Spades is played in a series of rounds that continue until a
|  team has won. In a single round, there are three (3) stages: bidding,
|  gameplay, and scoring. Descriptions of these stages follow.
|
|  (2 — Bidding) After cards are dealt (52 / 4 = 13 per player), a round opens
|  with a bidding stage, during which each player (one player at a time) sees
|  their cards, and then states (aka "bids") the minimum number of hands they
|  expect to win in the round given their cards. Each player's bid is then
|  summed with that of their partner to form the team's "contract", which is the
|  number of hands the team must win, combined (i.e. the total number hands that
|  should be won between the two players of each team). If a team wins more
|  hands in a round than stated in their contract, the team DOES NOT recieve all
|  the points for those extra hands. Similarly, if a team does not win as many
|  hands in a round as stated in their contract, they stand to lose points.
|  If a player makes a bid without seeing their cards (a "blind"), or if a
|  player states they will win zero (0) cards (a "nil"), special scoring rules
|  are applied. For more on scoring, see Section 4 — Scoring.
|
|  (3 — Gameplay) After the bidding stage, gameplay begins. During each hand of
|  a round, players play exactly one (1) of their 13 cards. In Spades, there are
|  two (2) classes of suites: in the lower class are clubs (♣), hearts (♥), and
|  diamonds (♦); and up above are the "trump" spades (♠). Rounds begin with the
|  player who won the previous round (or, in the case of the round's start, the
|  player who made the first bid). The card put down by the leading player of a
|  hand is called the \"lead\" card. This lead card may not be a spade unless a
|  spade has already been played in the round (through other means). Once the
|  lead card is set, play continues around the group (alternating teams), until
|  all three (3) other players have played. At this point, if there were any
|  spades played in the 4-card hand, the hand is awarded to whichever player
|  played the highest-ordered spade; otherwise, the hand is awarded to whichever
|  player played the highest-ordered card that matches the suite of the lead
|  card. Note that when playing a card, a player must always match the winning
|  suite (spade or lead) thus-far of a hand; if a player is not able to do so,
|  they are free to play a card from whichever suite they choose, including a
|  spade (this is how spades are introduced into a round).
|
|  (4 — Scoring) Once all 13 hands have been played, scoring begins. For teams
|  whose contract contains neither blinds (when a player bets before looking at
|  their cards) nor nils (when a player bets they will win zero (0) hands),
|  they will lose 10 times their contract number (in points) if they won fewer
|  hands than promised in their contract; if they won at least as many hands as
|  stated, they get 10 points per hand up until the number in the contract, and
|  one (1) point for each extra hand beyond what the contract states.
|  Additionally, for each extra hand, a team receives a penalty "bag". These
|  bags carry over between rounds, but only every seventh (7th) bag affects the
|  score. Indeed, every seventh (7th) bag a team earns results in a 100 point
|  penalty against them! If a player bets nil, wins no hands, AND their team
|  member wins no hands, then the player alone (team member is scored
|  separately) wins 100 points. If a player bets nil and does not meet these
|  requirements, then the team will lose 100 points. Likewise, if a player bets
|  blind and wins at least as many hands as stated in the contract, then the
|  player alone wins 100 points and no bags are added for excess. If, however,
|  a player bets blind but fails to win the number of hands on the contract
|  (supplemented by their partner), then they alone lose 100 points. Note that
|  both players on a team may bet blind and/or nil.
|
|  (5 — Winning) Rounds of Spades are repeated until a team accumulates enough
|  points to pass the winning value (set at the start of the game —
|  traditionally 500). In the case that two teams pass this value at the same
|  time, the team with the most amount of points wins. Total bags, and then
|  extra rounds, are used as tiebreakers.

III. Tests
|
|  There is currently no testing suite for the game, however the game was
|  heavily play-tested in production. A developing a comprehensive test suite
|  is one of the next steps for this program.
|
|  Please inform the program author at rbova@princeton.edu if you find any bugs!

IV. Design Decisions
|
|  This implementation of Spades was designed with modularity in mind.
|  Specifically, it abstracts the core "elements" of Spades (the game, each
|  round, each card, and bidding contracts) that are used frequently (and often
|  in similar ways) into their own objects. This allowed for very clean code
|  with clear logic flow.
|
|  No data structures or algorithms are implemented directly by this program,
|  however, it does leverage the built-in data structures of python3 quite
|  heavily. It is for this reason, in addition to semantic readability and OOP
|  support, that python3 was chosen. Cases where the built-in data structure
|  were especially useful include membership comprehension for lists, the
|  ability to efficiently append elements to a lists, and easy lookup of keys in
|  a dictionary.
|
|  Note that even though the code is not maximally efficient throughout, faster
|  data structures and algorithms would not be useful since the program is
|  currently (and heavily) bottle-necked by I/O speed (erasing a screen causes
|  significant delay). Additionally, the program will never use more than 52
|  cards, so there are no scalability concerns.

V. TODO
|
|  1) Find faster I/O solution for wiping screen
|  2) Develop testing suite that exploits modularity of codebase
|  3) Enjoy the game

VI. Credits
|
|  Author:  Reilly Bova
|  Date:    30 September 2018
|  Purpose: Kleiner-Perkins Engineering Fellows Program application supplement
|
|  External Libraries: None
|  Other credits:
|   > Spades ASCII art sourced from http://patorjk.com/software/taag/
