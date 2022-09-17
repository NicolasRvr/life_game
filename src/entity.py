import numpy as np


class Entity:
    @staticmethod
    def integration(entity):        
        return [(i, j) for i in range(entity.shape[0]) for j in range(entity.shape[1]) if entity[i , j] == 1]
    
    def glider(sens=True, direction=True, tanspose=True):
        glider = np.zeros((3, 3))
        dir = 0 if direction else -1
        glider[-1, :] = 1
        glider[1 , dir] = 1
        glider[0 , 1] = 1
        glider = glider if sens else glider[::-1]
        glider = glider if tanspose else glider.T
        return Entity.integration(glider)
    
    def gvaisseau(direction=True, tanspose=True):
        vaisseau = np.zeros((5, 5))
        vaisseau[-1, 1:] = 1
        vaisseau[2:, -1] = 1
        vaisseau[1, 3] = 1
        vaisseau[3, 0] = 1
        vaisseau = vaisseau if direction else vaisseau[::-1]
        vaisseau = vaisseau if tanspose else vaisseau.T
        return Entity.integration(vaisseau)
    
    def canon(direction=True, tanspose=True):
        canon = np.zeros((9, 36))
        canon[4:6,0:2] = 1
        canon[2:4, -2:] = 1
        canon[4:7, 10] = 1
        canon[3, 11] = 1
        canon[-2, 11] = 1
        canon[2, 12:14] = 1
        canon[-1, 12:14] = 1
        canon[5, 14] = 1
        canon[3, 15] = 1
        canon[7, 15] = 1
        canon[4:7, 16] = 1
        canon[5, 17] = 1
        canon[2:5,20:22] = 1
        canon[2:5,20:22] = 1
        canon[1,22] = 1
        canon[5,22] = 1
        canon[0:2, 24] = 1
        canon[5:7, 24] = 1
        canon = canon if direction else canon[::-1]
        canon = canon if tanspose else canon.T
        return Entity.integration(canon)