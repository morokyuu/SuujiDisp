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

def scale(ratio):
    return np.array([
        [ratio,0,0],
        [0,ratio,0],
        [0,0,1]
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

def draw_vectors(ax, mat):
    if mat.shape[0] != 3:
        raise ValueError("matrix must be (3, N)")
    N = mat.shape[1]
    X = np.zeros((1,N))
    Y = np.zeros((1,N))
    U = mat[0]  # x(N,)
    V = mat[1]  # y(N,)
    ax.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=1)


class BaseCord:
    def __init__(self, max_disp):
        self.n = np.array([[1,0,1]]).transpose()
        self.scale = 1.0
        # self.cont_size = 1.7
        # self.CONT_PITCH = self.cont_size * 1.3
        self.max_disp = max_disp
        
        self.cont = [] # np.shape()
        #self.cx = np.array([[1,0,1]]).transpose()
        
    def add(self,cont):
        self.cont.append(cont)
    
    def rescale(self,width):
        max_x,max_y = self.max_disp
        if width > max_x:
            self.scale = max_x / width
            print(self.scale)
        for i,c in enumerate(self.cont):
            self.cont[i] = scale(self.scale) @ c
        
    def disp(self,ax):
        for c in self.cont:
            draw_vectors(ax,c)
            #plot_vector(ax, c)

class ArrayPlt:
    def __init__(self,pitch):
        self._N = 1
        self.pitch = pitch
        self._set_one()

    def _set_one(self):
        v = np.zeros((3,1)); v[2,0] = 1
        self.v = v
        self._width = 0

    def _revise_vec(self):
        self._width = self.pitch*self._N
        halfw = self._width/2.0
        x = np.linspace(-halfw,halfw,self._N)
        self.v = np.vstack([x,np.zeros((1,self._N)),np.ones((1,self._N))])

    @property
    def width(self):
        return self._width
    
    @property
    def N(self):
        return self._N

    @N.setter
    def N(self,n):
        if n == 0:
            raise "N must not be zero"
        elif n==1:
            self._set_one()
        self._N = n
        self._revise_vec()



ww,hh = 6,6
bc = BaseCord((ww,hh))

fig, ax = plt.subplots()

# unit vector
plot_vector(ax, bc.n)


drawBox(ax, ww, hh, -ww/2.0,-hh/2.0)


bc.add(np.array([[-2, 2],
                 [-2,-2],
                 [ 1, 1]
                 ]))


ap = ArrayPlt(0.7)
ap.N = 10
print(ap.v)
bc.add(tr(0,1.5) @ ap.v)

bc.rescale(ap.width)
#bc.put(ap.width)

bc.disp(ax)

PLOT_RANGE = 5
ax.set_aspect('equal', adjustable='box')
ax.set_xlim(-PLOT_RANGE, PLOT_RANGE)
ax.set_ylim(-PLOT_RANGE, PLOT_RANGE)
ax.grid(True)

plt.show()
