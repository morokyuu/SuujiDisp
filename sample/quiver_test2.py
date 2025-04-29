import numpy as np
import matplotlib.pyplot as plt

def draw_vectors(mat):
    # mat.shape == (3, N)
    if mat.shape[0] != 3:
        raise ValueError("行列の形は (3, N) にしてください。")

    X = np.zeros((1,N))
    Y = np.zeros((1,N))
    U = mat[0]  # ベクトルの x 成分 (N,)
    V = mat[1]  # ベクトルの y 成分 (N,)

    plt.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=1)
    plt.gca().set_aspect('equal')
    plt.grid(True)
    plt.xlim(-5, 5)
    plt.ylim(-5, 5)
    plt.show()


N = 10
directions = (np.random.rand(2, N) - 0.5) * 4  # ベクトル成分 (dx, dy)

mat = np.vstack([directions, np.ones((1,N))])  # (4, N)
draw_vectors(mat)

