# cs4100_final_project

tictactoe.py :
Implementation of TicTacToe where the user can play against an AI agent. User will be player X and go first. The current state of the board will be printed (starts empty - all positions = '_'). The algorithm will recommend a move to the user (though this doesn't have to be followed) and the time it took to find this will be displayed. The user will enter their x (row) and y (column) coordinates for their move. If it is a valid move the board state will be updated and it will become the AI's turn otherwise it will ask the user to input another move. The AI will go and update the board as well as display how long it took to make a move. This will continue until a player wins or the game ends in a tie.

connect4.py :
Extends on TicTacToe to show how the game design would be altered to create Connect4. Due to the similar nature of the games the minimax algorithm created can be applied to this game as well. This file shows the game creation code that would allow for this generalization.
