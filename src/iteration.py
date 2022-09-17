import numpy as np
from src.tools import Tools


class Rules:        
    @staticmethod
    def rules(sub_matrix):
        current_state = sub_matrix[1, 1]
        voisins = np.sum(sub_matrix) - current_state
        if current_state :
            if voisins in [2, 3]:
                return current_state
            else :
                return 0
        elif not current_state:
            if voisins == 3:
                return 1
            else :
                return current_state

class State:
    def __init__(self, init_board):
        self.board = self.inc_board(init_board)
    # pour gagner du temps voir si une vectorisation n'est pas possible
    @staticmethod
    def inc_board(init_board):
        inc_board = np.zeros(init_board.shape, dtype=int)
        for i in range(1, init_board.shape[0]-1):
            for j in range(1, init_board.shape[1]-1):
                sub_matrix = init_board[i-1 : i+2, j-1 : j+2]
                inc_board[i, j] = Rules.rules(sub_matrix)
        return inc_board

class Iteration:
    @staticmethod
    def iteration(init_board, n_max = 10, n_augmentation=10):
        board = Tools.augmentation_matrix(init_board, n_augmentation)
        res = [(init_board, 0)]
        for n in range(1, n_max):
            board = State(board).board
            res.append((Tools.reduction_matrix(board, n_augmentation), n))
            if np.sum(Tools.reduction_matrix(board, n_augmentation)) == 0 :
                break
            if Tools.array_in_liste(board, (item[0] for item in res)):
                break
        return res