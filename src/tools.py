import numpy as np


class Tools:
    @staticmethod
    def array_in_liste(vect, liste):
        return True if True in [np.array_equal(vect, item) for item in liste] else False

    @staticmethod
    def augmentation_matrix(matrix, n=3):
        li, co = matrix.shape[0]+2*n, matrix.shape[1]+2*n
        out = np.zeros((li, co))
        out[n:li-n, n:co-n] = matrix
        return out
    
    @staticmethod
    def reduction_matrix(matrix, n=3):
        li, co = matrix.shape[0], matrix.shape[1]
        return matrix[n:li-n, n:co-n]