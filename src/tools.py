import numpy as np


class Tools:
    @staticmethod
    def array_in_liste(vect, liste):
        for item in liste:
            if np.all(item == vect):
                return True
            else:
                return False

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