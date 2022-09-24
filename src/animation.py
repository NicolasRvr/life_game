import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

from src.iteration import Iteration

class Animation:
    @staticmethod
    def animation(board, name=None, n_max=30, **kwargs):
        name = f"life_game" if name is None else name

        etats = Iteration.iteration(board, n_max)
        def init_board():
            ax.plot(y, -x, c='k', lw=0.5)
            ax.plot(z, -k, c='k', lw=0.5)
            ax.axis('off')
            plt.axis('equal')

        def plot_board(state):
            size = state[0].shape
            li, co = *size,
            for i in range(li):
                for j in range(co):
                    if state[0][i, j] == 1:
                        ax.add_patch(plt.Rectangle(((j-0.5), -(i-0.5)), 1, -1, facecolor='pink', edgecolor='black'))
            plt.title(f"State {state[1]}", loc='center')
            plt.axis('equal')
            plt.tight_layout()

        size = board.shape
        li, co = *size,
        x, y = np.meshgrid(np.arange(-0.5, li, 0.5)[::2], np.arange(-0.5, co, 0.5)[::2])
        z, k = np.meshgrid(np.arange(-0.5, co, 0.5)[::2], np.arange(-0.5, li, 0.5)[::2])
        fig, ax = plt.subplots(dpi=100)
        init_board()

        def update(state):
            ax.clear()
            init_board()
            plot_board(state)

        ani = FuncAnimation(fig, update, frames=etats, repeat=False, interval=0.01, **kwargs)
        ani.save(f'{name}.gif', writer=PillowWriter(fps=120), **kwargs)
        plt.close()


