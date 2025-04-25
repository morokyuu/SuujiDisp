# -*- coding: utf-8 -*-
"""
Created on Sun Apr 20 21:54:09 2025

@author: square
"""

import numpy as np
import matplotlib.pyplot as plt
import random




# NUM = 10
# x = np.linspace(0, 200, NUM)
# y = np.array([random.uniform(-5,5) for _ in range(NUM)])

NUM = 10
x = np.linspace(0, 200, NUM)
y = np.array([random.uniform(-5,5) for _ in range(NUM)])



fig, ax = plt.subplots()

ax.plot(x,y)
ax.plot(x,yd)
ax.set_aspect('equal', adjustable='box')
ax.set_xlim(-15, 15)
ax.set_ylim(-15, 15)
ax.grid(True)

plt.show()

