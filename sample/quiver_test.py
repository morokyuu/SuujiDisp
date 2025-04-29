import numpy as np
import matplotlib.pyplot as plt

def draw_vectors(mat):
    # mat.shape == (4, N)
    if mat.shape[0] != 4:
        raise ValueError("行列の形は (4, N) にしてください。")

    X = mat[0]  # 始点 x 座標 (N,)
    Y = mat[1]  # 始点 y 座標 (N,)
    U = mat[2]  # ベクトルの x 成分 (N,)
    V = mat[3]  # ベクトルの y 成分 (N,)

    plt.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=1)
    plt.gca().set_aspect('equal')
    plt.grid(True)
    plt.xlim(np.min(X), np.max(X + U) + 1)
    plt.ylim(np.min(Y), np.max(Y + V) + 1)
    plt.show()


N = 10
starts = np.random.rand(2, N) * 10     # 始点 (x, y)
directions = (np.random.rand(2, N) - 0.5) * 4  # ベクトル成分 (dx, dy)

mat = np.vstack([starts, directions])  # (4, N)
draw_vectors(mat)

