#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 22:11:56 2023

@author: rigurn
"""

import numpy as np

# class for Connect 4
class ConnectFour:
    
    def __init__(self):
        self.row = 6
        self.column = 7
        self.state = self.start()
        self.turn = 'R'
    
    # start the game with array of zeros - size based on row & column variables
    def start(self):
        return np.zeros((self.row, self.column))
    
    '''
    output the winner of the game (based on token) by checking the possible winning
    states (horizontal, vertical, diagonal) otherwise 'Tie' if no winner or 
    no output (None) if the game is still ongoing (there are still more 
                                                   possible moves to make)
    '''
    def find_winner(self):
        # check vertical
        for i in range(self.row - 3):
            for j in range(self.column):
                if (self.state[i][j] == self.state[i+1][j]
                    and self.state[i+1][j] == self.state[i+2][j] 
                    and self.state[i+2][j] == self.state[i+3][j] 
                    # not empty
                    and self.state[i+3][j] != 0):
                    
                    return self.state[i][j]
        
        # check horizontal
        for i in range(self.row):
            for j in range(self.column - 3):
                if (self.state[i][j] == self.state[i][j+1]
                    and self.state[i][j+1] == self.state[i][j+2] 
                    and self.state[i][j+2] == self.state[i][j+3] 
                    and self.state[i][j+3] != 0):
                    
                    return self.state[i][j]
        
        # check right to left diagonal
        for i in range(self.row - 3):
            for j in range(self.column - 3):
                if (self.state[i][j] == self.state[i-1][j+1]
                    and self.state[i-1][j+1] == self.state[i-2][j+2] 
                    and self.state[i-2][j+2] == self.state[i-3][j+3] 
                    and self.state[i-3][j+3] != 0):
                    
                    return self.state[i][j]
        
        # check left to right diagonal
        for i in range(3, self.row):
            for j in range(self.column - 3):
                if (self.state[i][j] == self.state[i+1][j+1]
                    and self.state[i+1][j+1] == self.state[i+2][j+2] 
                    and self.state[i+2][j+2] == self.state[i+3][j+3] 
                    and self.state[i+3][j+3] != 0):
                
                    return self.state[i][j]
                
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
        if (x_pos < self.row or x_pos > self.row 
            or y_pos < self.colum or y_pos > self.column):
            valid = False
            
        # move already made in that position
        elif self.state[x_pos][y_pos] != 0:
            valid = False
            
        return valid
    
    # determines if the board is full or if there is still space for more moves
    def full_board(self):
        full = True
        
        for i in range(self.row):
            for j in range(self.column):
                
                # still has empty space then full is false
                if self.state[i][j] == 0:
                    full = False
        return full
        
def main():
    
    c = ConnectFour()
    b = c.start()
    
    print(b)

if __name__ == "__main__":
    main()