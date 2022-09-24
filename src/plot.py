import matplotlib.pyplot as plt
import numpy as np
import os

class PlotBoard:
    @staticmethod
    def grid(size):
        li, co = *size,
        x, y = np.meshgrid(np.arange(-0.5, li, 0.5)[::2], np.arange(-0.5, co, 0.5)[::2])
        z, k = np.meshgrid(np.arange(-0.5, co, 0.5)[::2], np.arange(-0.5, li, 0.5)[::2])
        fig, ax = plt.subplots(dpi=100, layout="constrained")
        ax.plot(y, -x, c='k', lw=0.5)
        ax.plot(z, -k, c='k', lw=0.5)
        return fig, ax

    @classmethod
    def plot(cls, board, save_fig=False ,title=None, loc='data'):
        size = board.shape
        fig, ax = cls.grid(size)
        for i in range(size[0]):
            for j in range(size[1]):
                if board[i, j] == 1:
                    ax.add_patch(plt.Rectangle(((j-0.5), -(i-0.5)), 1, -1, facecolor='pink', edgecolor='black'))
        ax.axis('off')
        plt.axis('equal')
        if title is not None:
            plt.title(title)
        if save_fig:
            path = os.path.join(loc, f'{title}.png')
            plt.savefig(path)
        return None