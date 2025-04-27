# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

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

def drawCircle(ax, x, y, r, color='black'):
    ax.add_patch(patches.Circle((x,y), radius=r, fill=False, color=color))
        
def drawLine(ax,x0,y0,x1,y1,color='blue'):
    ax.plot(np.array([x0,x1]),np.array([y0,y1]),color=color)

def drawBox(ax,w,h, x0=0, y0=0,color='brown'):
    x = [x0, x0 + w, x0 + w, x0, x0]
    y = [y0, y0, y0 + h, y0 + h, y0]
    ax.plot(x,y,color=color)
    

def drawPolyline(ax,poly,color='blue'):
    poly = poly.T
    poly = np.vstack((poly,poly[0,:]))
    for i in range(poly.shape[0]-1):
        drawLine(ax,poly[i,0],poly[i,1],poly[i+1,0],poly[i+1,1],color=color)



def plot_vector(ax, vec, color='r'):
    ax.quiver(0, 0, vec[0, 0], vec[1, 0], angles='xy', scale_units='xy', scale=1, color=color)

class BaseCord:
    def __init__(self):
        self.n = np.array([[1,0,1]]).transpose()
        self.cont_size = 1.7
        self.CONT_PITCH = self.cont_size * 1.3
        self.disp_width = 0
        self.disp_height = 0
        
        #self.cx = np.array([[1,0,1]]).transpose()
        
    def put(self,value):
        self.disp_width = value
    
bc = BaseCord()

fig, ax = plt.subplots()

# unit vector
plot_vector(ax, bc.n)

#disp area
drawBox(ax, bc.disp_width, bc.disp_height, -bc.disp_width/2.0,-bc.disp_height/2.0)

bc.put(1.5)


PLOT_RANGE = 5
ax.set_aspect('equal', adjustable='box')
ax.set_xlim(-PLOT_RANGE, PLOT_RANGE)
ax.set_ylim(-PLOT_RANGE, PLOT_RANGE)
ax.grid(True)

plt.show()