# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 22:40:53 2025

@author: square
"""

import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-10, 10, 10)
y = 2/3.0 * x
yd = -3/2.0 * x


fig, ax = plt.subplots()

ax.plot(x,y)
ax.plot(x,yd)
ax.set_aspect('equal', adjustable='box')
ax.set_xlim(-15, 15)
ax.set_ylim(-15, 15)
ax.grid(True)

plt.show()