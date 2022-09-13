import numpy as np
from src.plot import PlotBoard
from src.animation import Animation
from src.iteration import Iteration


class Board:
    def __init__(self, size, init_vector=None, **kwargs):
        if size <  5:
            raise ValueError(f'{size} too small, minimum 5')
        elif type(size) is not int:
            raise ValueError(f'{size} not an integer')
        self.board = self.init_board(size, init_vector)
    
    @staticmethod    
    def init_board(size, init_vector=None):
        board = np.zeros((size, size), dtype=int)
        if init_vector is not None:
            for (i, j) in init_vector:
                board[i,j] = 1
        return board
    
    def plot(self, **kwargs):
        PlotBoard.plot(self.board, **kwargs)
        
    def animate(self, **kwargs):
        Animation.animation(self.board, **kwargs)
    
    def states(self, **kwargs):
        return Iteration.iteration(self.board, **kwargs)
    
    
