import numpy as np
from src.plot import PlotBoard
from src.animation import Animation
from src.iteration import Iteration


class Board:
    def __init__(self, size, init_vector=None, offset=None, **kwargs):
        # if size <  5:
        #     raise ValueError(f'{size} too small, minimum 5')
        # if type(size) is not int:
        #     raise ValueError(f'{size} not an integer')
        init_vector = init_vector if offset is None else Board.set_offset(init_vector, offset)
        self.board = self.init_board(size, init_vector, **kwargs)
    
    @staticmethod    
    def init_board(size, init_vector=None, offset=None, **kwargs):
        if type(size) == int:
            li, col = size, size
        elif type(size) in [tuple, list]:
            li, col = *size,
        board = np.zeros((li, col), dtype=int)
        #
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
    
    @staticmethod
    def set_offset(init_vector, offset=(0, 0), **kwargs):
        i, j = *offset,
        return [(pos[0] + i, pos[1] + j) for pos in init_vector]


    
    
