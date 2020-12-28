# Console based Othello game clone using python
[Othello] (also known as 'Reversi') is a board game invented during the Victorian era.
It is a very dynamic board game; the board position can change dramatically with each move.

Othello is a 2-player game using an eight-by-eight square grid with pieces that have two distinctly colored sides. Pieces typically appear disc-like, with a light and a dark face, each side representing one player. The goal for each player is to make pieces of their colour constitute a majority of the pieces on the board at the end of the game, by turning over as many of their opponent's pieces as possible.

<img src="https://i5.walmartimages.com/asr/7fc52dcc-ab97-422c-946c-840ad445806f_1.6595418ecb08ec1446fdedcbea4272cf.jpeg" height="250" width="250">

### Rules:
In this python code, **X** and **O** represent the 2 different sides of coins. Disc with O side facing up, when flipped, shows X side up.\
The game starts with four discs placed at the center of the board, two of them with X side and the other two with O side up.

Players get turns alternately to make their move.\
A move consists of placing one piece on an **empty square**.\
You can choose your square by entering the corresponding row and column numbers.\
Choosing a square that is already occupied is an **invalid** move and you will be prompted to enter a valid move again.

On your turn, you place one piece on the board with your color facing up. You must place the piece so that an opponent's piece, or a row of opponent's pieces, is flanked by your pieces. All of the opponent's pieces between your pieces are then turned over to become your color.   
It can happen that a piece is played so that pieces or rows of pieces in more than one direction are trapped between the new piece played and other pieces of the same colour. In this case, all the pieces in all viable directions are turned over.   
You can capture **vertical, horizontal, and diagonal rows** of pieces. Also, you can capture **more than one row** at once.

### Aim of the game:
The objective of the game is to own more pieces than your opponent when the game is over. The game is over when the board is full.
The player who has the **most discs** on the board at the end of the game wins.

#### For additional information and rules, refer the following links:
[Othello overview]

[Othello/Reversi rules]

[//]: # 

  [Othello]: <https://en.wikipedia.org/wiki/Reversi#Othello>
   [Othello overview]: <https://board-games-galore.fandom.com/wiki/Othello>
   [Othello/Reversi rules]: <https://documentation.help/Reversi-Rules/rules.htm>
