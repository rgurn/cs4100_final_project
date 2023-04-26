#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 00:33:48 2023

@author: rigurn
"""

# import time to compare how long algorithms take
import time

# class for TicTacToe
class TicTacToe:
    
    def __init__(self):
        self.start()
    
    ''' start the game by creating an empty board using '_'
     '_' is a representation of no move being made in that spot yet
     I chose this to easier integrate printable graphics to view the 
     game in the terminal'''
    def start(self):
        self.state = [['_', '_', '_'],
                      ['_', '_', '_'],
                      ['_', '_', '_']]
        
        # X will always start the game (user)
        self.turn = 'X'
        
    # print out current board
    def create_board(self):
        # for each row in board
        for i in range(3):
            # print each character in column ending with space in between
            for j in range(3):
                print('{}'.format(self.state[i][j]), end = ' ')
            # new line between each row
            print('\n')
    
    # determines if the board is full or if there is still space for more moves
    def full_board(self):
        full = True
        
        for i in range(3):
            for j in range(3):
                
                # still has empty space then full is false
                if self.state[i][j] == '_':
                    full = False
        return full
        
        # check if the board still has open spaces to play
            
    '''
    output the winner of the game (X or O) by checking the possible winning
    states (horizontal, vertical, diagonal) otherwise 'Tie' if no winner or 
    no output (None) if the game is still ongoing (there are still more 
                                                   possible moves to make)
    '''
    def find_winner(self):
        
        # horizontal check
        for i in range(3):
            if self.state[i] == ['X', 'X', 'X']:
                return 'X'
            elif self.state[i] == ['O', 'O', 'O']:
                return 'O'
            
        # vertical check
        for i in range(3):
            if (self.state[0][i] == self.state[1][i] and
                self.state[1][i] == self.state[2][i] and
                self.state[0][i] != '_'):
                return self.state[0][i] # the winner
            
        # left to right diagonal check
        if (self.state[0][0] != '_' and
            self.state[0][0] == self.state[1][1] and
            self.state[1][1] == self.state[2][2]):
            return self.state[0][0]
        
        # right to left diagonal check
        if (self.state[0][2] == self.state[1][1] and
            self.state[1][1] == self.state[2][0] and
            self.state[0][2] != '_'):
            return self.state[0][2]
        
        # if board full but no winner -- Tie
        if self.full_board():
            # tie
            return 'Tie'
        # otherwise game is still ongoing bc more moves possible so no output
        else:
            return None
    
    # is the given positions for a move valid 
    # (within the board and on an empty space)
    def valid_move(self, x_pos, y_pos):
        valid = True
        
        # off the board
        if x_pos < 0 or x_pos > 2 or y_pos < 0 or y_pos > 2:
            valid = False
            
        # move already made in that position
        elif self.state[x_pos][y_pos] != '_':
            valid = False
            
        return valid
    
    
    '''
    minimax algorithm
    '''
    
    # max player is user (player X)
    def max_value(self):
        
        '''
        values:
            -10 = loss
            0 = tie
            10 = win
        '''
        
        # worst case
        v = -100
        
        end = self.find_winner()
        x_pos = None
        y_pos = None
        
        # check if game is over (if winner returned in end)
        if end == 'X':
            return (10, 0, 0)
        elif end == 'O':
            return (-10, 0, 0)
        elif end == 'Tie':
            return (0,0,0)
        
        # loop through board
        for i in range(3):
            for j in range(3):
                # check if empty
                if self.state[i][j] == '_':
                    self.state[i][j] = 'X'
                    
                    (mini, min_i, min_j) = self.min_value()
                    
                    # maximize v
                    if mini > v:
                        v = mini
                        x_pos = i
                        y_pos = j
                        
                    self.state[i][j] = '_'
                
        return (v, x_pos, y_pos)
    
    # min player is AI agent (player O)
    def min_value(self):
        
        '''
        values:
            -10 = win
            0 = tie
            10 = loss
        '''
        
        # worst case
        v = 100
        
        end = self.find_winner()
        x_pos = None
        y_pos = None
        
        # check if game is over (if winner returned in end)
        if end == 'X':
            return (10, 0, 0)
        elif end == 'O':
            return (-10, 0, 0)
        elif end == 'Tie':
            return (0,0,0)
        
        # loop through board
        for i in range(3):
            for j in range(3):
                # check if empty
                if self.state[i][j] == '_':
                    self.state[i][j] = 'O'
                    
                    (maxi, max_i, max_j) = self.max_value()
                    
                    # minimize v
                    if maxi < v:
                        v = maxi
                        x_pos = i
                        y_pos = j
                    self.state[i][j] = '_'
                
        return (v, x_pos, y_pos)
    
    # play the game with minimax algorithm
    def game(self):
        self.start()
        while True:
            self.create_board()
            end = self.find_winner()
            
            # check if game is over (if winner returned in end)
            if end == 'X':
                print('Game over! Player X won!')
                break
            elif end == 'O':
                print('Game over! Player O won!')
                break
            elif end == 'Tie':
                print('Game ended in a tie!')
                break
            
            # Player X's turn
            if self.turn == 'X':
                while True:               
                    # time how long it will take to run algorithm
                    start = time.time()
                    
                    # find recommended move for user
                    (maxi, x_pos, y_pos) = self.max_value()
                    print('\nRecommended that you choose (X, Y) as: ', x_pos, y_pos)
                    finish = time.time()
                    elapsed_seconds = (finish - start) #/ 10**9
                    print("Time: ", elapsed_seconds)
                    
                    # get x,y move from user
                    input_x = int(input("\nEnter the X coordinate: "))
                    input_y = int(input("Enter the Y coordinate: "))
                    
                    # if given move is valid change position to X
                    if self.valid_move(input_x, input_y):
                        self.state[input_x][input_y] = 'X'
                        
                        # now update to player O's turn
                        self.turn = 'O'
                        break
                    # otherwise ask for new move input
                    else:
                        print("\nPlease enter a valid move")
            
            # O's turn
            else:
                print("\nAI's turn:")
                # time algorithm
                start = time.time()
                
                (mini, x_pos, y_pos) = self.min_value()
                
                finish = time.time()
                elapsed_seconds = (finish - start) #/ 10**9
                print("Time: ", elapsed_seconds)
                
                # update position with O & go back to X's turn
                self.state[x_pos][y_pos] = 'O'
                self.turn = 'X'
    
    
    '''
    alpha beta pruning
    '''
    
    # max player is user - player X
    def max_val_alpbeta(self, alpha, beta):
        '''
        values:
            -10 = loss
            0 = tie
            10 = win
        '''
        
        # worst case
        v = -100
        
        end = self.find_winner()
        x_pos = None
        y_pos = None
        
        # check if game is over (if winner returned in end)
        if end == 'X':
            return (10, 0, 0)
        elif end == 'O':
            return (-10, 0, 0)
        elif end == 'Tie':
            return (0,0,0)
        
        # loop through board
        for i in range(3):
            for j in range(3):
                # check if empty
                if self.state[i][j] == '_':
                    self.state[i][j] = 'X'
                    
                    (mini, min_i, min_j) = self.min_val_alpbeta(alpha, beta)
                    
                    # maximize v
                    if mini > v:
                        v = mini
                        x_pos = i
                        y_pos = j
                    
                    self.state[i][j] = '_'
                    
                    # if v > beta return 
                    if v > beta:
                        return (v, x_pos, y_pos)
                    
                    # update alpha
                    alpha = max(alpha, v)
                
        return (v, x_pos, y_pos)
    
    
    def min_val_alpbeta(self, alpha, beta):
        '''
        values:
            -10 = win
            0 = tie
            10 = loss
        '''
        
        # worst case
        v = 100
        
        end = self.find_winner()
        x_pos = None
        y_pos = None
        
        # check if game is over (if winner returned in end)
        if end == 'X':
            return (10, 0, 0)
        elif end == 'O':
            return (-10, 0, 0)
        elif end == 'Tie':
            return (0,0,0)
        
        # loop through board
        for i in range(3):
            for j in range(3):
                # check if empty
                if self.state[i][j] == '_':
                    self.state[i][j] = 'O'
                    
                    (maxi, max_i, max_j) = self.max_val_alpbeta(alpha, beta)
                    
                    # minimize v
                    if maxi < v:
                        v = maxi
                        x_pos = i
                        y_pos = j
                        
                    self.state[i][j] = '_'
                    
                    # if v < alpha return
                    if v < alpha:
                        return (v, x_pos, y_pos)
                    
                    # update beta
                    beta = min(beta, v)
                
        return (v, x_pos, y_pos)
    
    # play the game using minimax algorithm with alpha-beta pruning
    def game_prune(self):
        self.start()
        while True:
            self.create_board()
            end = self.find_winner()
            
            # check if game is over (if winner returned in end)
            if end == 'X':
                print('Game over! Player X won!')
                break
            elif end == 'O':
                print('Game over! Player O won!')
                break
            elif end == 'Tie':
                print('Game ended in a tie!')
                break
            
            # Player X's turn
            if self.turn == 'X':
                while True:               
                    # time how long it will take to run algorithm
                    start = time.time()
                    
                    # find recommended move for user
                    (maxi, x_pos, y_pos) = self.max_val_alpbeta(-100, 100)
                    print('\nRecommended that you choose (X, Y) as: ', x_pos, y_pos)
                    finish = time.time()
                    elapsed_seconds = (finish - start) #/ 10**9
                    print("Time: ", elapsed_seconds)
                    
                    # get x,y move from user
                    input_x = int(input("\nEnter the X coordinate: "))
                    input_y = int(input("Enter the Y coordinate: "))
                    
                    # if given move is valid change position to X
                    if self.valid_move(input_x, input_y):
                        self.state[input_x][input_y] = 'X'
                        
                        # now update to player O's turn
                        self.turn = 'O'
                        break
                    # otherwise ask for new move input
                    else:
                        print("\nPlease enter a valid move")
            
            # O's turn
            else:
                print("\nAI's turn:")
                # time algorithm
                start = time.time()
                
                (mini, x_pos, y_pos) = self.min_val_alpbeta(-100, 100)
                
                finish = time.time()
                elapsed_seconds = (finish - start) #/ 10**9
                print("Time: ", elapsed_seconds)
                
                # update position with O & go back to X's turn
                self.state[x_pos][y_pos] = 'O'
                self.turn = 'X'

    
'''TESTS'''
import unittest

# tests for TicTacToe functions
class TestGame(unittest.TestCase):
    
    # valid_move should output false if a move has already been made in that position
    def test_invalid_move(self):
        t = TicTacToe()
        
        t.state = [['X', '_', '_'],
                   ['_', '_', '_'],
                   ['_', '_', '_']]
        
        self.assertFalse(t.valid_move(0,0))
        
    # valid_move should output false if a inputed x,y outside of grid
    def test_invalid_move_out_bounds(self):
        t = TicTacToe()
        
        t.state = [['X', '_', '_'],
                   ['_', '_', '_'],
                   ['_', '_', '_']]
        
        self.assertFalse(t.valid_move(5,1))
   
    # valid_move outputs True if inputted x,y in grid & no move made there yet
    def test_valid_move(self):
        t = TicTacToe()
        
        t.state = [['X', '_', '_'],
                   ['_', '_', '_'],
                   ['_', '_', '_']]
        
        self.assertTrue(t.valid_move(1,0))
    
    # full_board outputs true if all positions have moves
    def test_full_board(self):
        t = TicTacToe()
        
        t.state = [['X', 'O', 'X'],
                   ['O', 'O', 'X'],
                   ['X', 'X', 'O']]
        
        self.assertTrue(t.full_board())
        
    # full_board outputs false if at least one empty postion
    def test_full_board_false(self):
        t = TicTacToe()
        
        t.state = [['X', 'O', 'X'],
                   ['_', 'O', 'X'],
                   ['X', 'X', 'O']]
        
        self.assertFalse(t.full_board())
        
    # find_winner -- horizontal X win
    def test_find_winner_horizontal_x(self):
        t = TicTacToe()
        
        t.state = [['X', 'X', 'X'],
                   ['_', 'O', 'X'],
                   ['X', 'O', 'O']]
        
        self.assertEqual(t.find_winner(), 'X', "Player X should win")
        
    # find_winner -- horizontal O win
    def test_find_winner_horizontal_o(self):
        t = TicTacToe()
        
        t.state = [['X', 'O', 'X'],
                   ['_', 'X', 'X'],
                   ['O', 'O', 'O']]
        
        self.assertEqual(t.find_winner(), 'O', "Player O should win")
        
    # find_winner -- vertical O win
    def test_find_winner_vertical_o(self):
        t = TicTacToe()
        
        t.state = [['X', 'O', 'X'],
                   ['_', 'O', 'X'],
                   ['X', 'O', 'O']]
        
        self.assertEqual(t.find_winner(), 'O', "Player O should win")
        
    # find_winner -- vertical X win
    def test_find_winner_vertical_x(self):
        t = TicTacToe()
        
        t.state = [['X', 'O', 'O'],
                   ['X', 'O', 'X'],
                   ['X', 'X', 'O']]
        
        self.assertEqual(t.find_winner(), 'X', "Player X should win")
        
    # find_winner -- left diagonal O win
    def test_find_winner_left_diagonal(self):
        t = TicTacToe()
        
        t.state = [['O', 'O', 'X'],
                   ['_', 'O', 'X'],
                   ['X', 'O', 'O']]
        
        self.assertEqual(t.find_winner(), 'O', "Player O should win")
        
    # find_winner -- right diagonal X win
    def test_find_winner_right_diagonal(self):
        t = TicTacToe()
        
        t.state = [['O', 'O', 'X'],
                   ['X', 'X', 'O'],
                   ['X', 'X', 'O']]
        
        self.assertEqual(t.find_winner(), 'X', "Player X should win")
        
    # find_winner -- tie
    def test_find_winner_tie(self):
        t = TicTacToe()
        
        t.state = [['O', 'O', 'X'],
                   ['X', 'X', 'O'],
                   ['O', 'X', 'O']]
        
        self.assertEqual(t.find_winner(), 'Tie', "Game should end in tie")
    
    # find_winner -- game still ongoing so return None
    def test_find_winner_still_ongoing(self):
        t = TicTacToe()
        
        t.state = [['O', 'O', 'X'],
                   ['X', 'X', 'O'],
                   ['_', 'X', 'O']]
        
        self.assertEqual(t.find_winner(), None, "Game still has more possible moves")

def main():
    
    t = TicTacToe()
    #t.game()
    t.game_prune()
    
    # uncomment to show tests passing 
    # (can run with game just messes up printing of board in last round)
    
    #unittest.main()

if __name__ == "__main__":
    main()