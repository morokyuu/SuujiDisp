# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def rotZ(th):
    return np.array([
        [ np.cos(th), np.sin(th), 0.0],
        [-np.sin(th), np.cos(th), 0.0],
        [          0,          0, 1.0]
        ])

def tr(x,y):
    return np.array([
        [        1.0,          0,   x],
        [          0,        1.0,   y],
        [          0,          0, 1.0]
        ])


def plot_vector(ax, vec, color='r'):
    ax.quiver(0, 0, vec[0, 0], vec[1, 0], angles='xy', scale_units='xy', scale=1, color=color)

class BaseCord:
    def __init__(self):
        self.nx = np.array([[1,0,1]]).transpose()
        self.ny = np.array([[0,1,1]]).transpose()
        

bc = BaseCord()

fig, ax = plt.subplots()


plot_vector(ax, bc.nx)
plot_vector(ax, bc.ny, color='b')

PLOT_RANGE = 5
ax.set_aspect('equal', adjustable='box')
ax.set_xlim(-PLOT_RANGE, PLOT_RANGE)
ax.set_ylim(-PLOT_RANGE, PLOT_RANGE)
ax.grid(True)

plt.show()