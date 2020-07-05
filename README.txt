Old version written in early 2017 using Python 2.7. New version added 05/06/2020.


The story of there being no comments in the code:
I wrote this code on my laptop and compiled it using py2exe in order to send to my friends. I also moved The compiled version to my main PC. When I upgraded to a new laptop, I formatted the old one without realising there was no backup for this code. I managed to recover it from the executable file using other people's scripts, however py2exe must have removed all of the comments.




How to play:
To start enter the number of players and their names in the console. Everyone's moves are also written in the console once the game starts.

Enter 2 or more players. No more than 18, because there aren't enough cards. There is no input checking so inputing something other than a number for the number of players will crash the program. If player name is "AI" then it will be played by the program.

The game will then start in the main window where each player can take their turn. Rules of the game are written in the last section of this file.

Also cards can only be clicked on the left, so the last card is only clickable for the first 30 pixels or so.

When a game is over, the program restarts.



Known issues of the old version:
- There are some logic issues with burning in certain cases, such as getting another turn when there are no more cards to play or not getting the extra turn from burning. I will have a look at it once my thesis is submitted and hopefully upload a new fixed version.
- Can't close or even move the main window while the console waits for input. This could be fixed by incorporating user input into the window and remove the need of having the console.

New version fixes:
-Burning logic fixed, the game should run without issues now.

Rules of the game:
This game is based on https://en.wikipedia.org/wiki/Shithead_(card_game) with slightly different rules.
There are 54 cards in the deck - standard set and two jokers. Everyone is dealt "hidden cards", "top cards" and "hand cards". Each player gets equal number of cards, and the same amount of hidden, top and hand cards. Calculate 54/(3n) rounded down to the nearest integer determine how many cards n players get in each set. 

For example, 54/9=6, so each player would get 6 hidden cards, 6 top cards and 6 hand cards. As another example, if there are 5 players, there are 9 cards left over. One card is drawn by the player who just had their turn until there are no more cards.

Before the first turn, each player can exchange any of their top cards with any of their hand cards.

The objective of the game is to get rid of all your cards. The first player to play can put any card (or cards) down on the table. If a player has multiple of the same number (or face card) the player may choose to play all of them, just one, or any combination (so if a player has three 5's, they can play one, two or all three).

The game starts clockwise, left of the dealer goes first. The following players must play the same number or higher (subject to special cards, see below) than what is on the table. If a player cannot play a valid card, they need to pick up all the played cards. If a player can play a valid card they have to play.

The cards in play and their power in order:
2 - resets everything back to 2, can be played on anything
3 - is invisible, the next player plays as if the 3 (or multiples of 3) were not there, can be played on anything
4 - no power
5 - no power
6 - no power
7 - the following player has to play a 7 or lower
8 - no power
9 - no power
10 - burn (explained in the next paragraph), can be played on anything.
Jack - no power
Queen - no power
King - no power
Ace - no power
Joker - reverses the order of play, can be played on anything.

Burning - when 4 cards of the same number are played in succession (by any number of players) the cards on the table get put out of play, and the person who burned gets another turn. Playing a single 10 also initiates a burn, as well as two jokers in a row by one or two players (since there are not 4 jokers).

Progression - Everyone has to play from their hand cards first, followed by top cards, followed by hidden cards. When a player plays the last of their hand cards and has the same number card/cards in their top cards, they may choose to play this/these too. Once the player runs out of all top cards, on each subsequent turn this player needs to play one of the hidden cards blindly. The game is over when only one player remains, and that player is declared the shed and goes first in the next game.
