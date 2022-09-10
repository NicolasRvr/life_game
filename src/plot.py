import matplotlib.pyplot as plt
import numpy as np
import os

class PlotBoard:
    @staticmethod
    def grid(size):
        x, y = np.meshgrid(np.arange(-0.5, size, 0.5)[::2], np.arange(-0.5, size))
        fig, ax = plt.subplots(figsize=(10, 10), dpi=50)
        ax.plot(x, -y, c='k', lw=0.5,)
        ax.plot(y, -x, c='k', lw=0.5)
        ax.axis('off')
        return fig, ax

    @classmethod
    def plot(cls, board, save_fig=False ,title=None, loc='data'):
        size = board.shape[0]
        fig, ax = cls.grid(size)
        for i in range(size):
            for j in range(size):
                if board[i, j] == 1:
                    ax.add_patch(plt.Rectangle(((j-0.5), -(i-0.5)), 1, -1, facecolor='pink', edgecolor='black'))
        plt.tight_layout()
        if title is not None:
            plt.title(title)
        if save_fig:
            path = os.path.join(loc, f'{title}.png')
            plt.savefig(path)
        return None