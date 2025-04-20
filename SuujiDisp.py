import pyglet
from basket import Basket
import time
import threading
import numpy as np
import random

tiles = []

window = pyglet.window.Window(800, 600, "Suuji no gakushu!", resizable=False)
center_x, center_y = window.width // 2, window.height // 2

batch = pyglet.graphics.Batch()



class Tile:
    def __init__(self, x, y, s):
        self.TILE_SIZE = 20
        self.pos = np.array([x,y,s])
        self.sprite = pyglet.shapes.Rectangle(x, y, self.TILE_SIZE * s, self.TILE_SIZE * s, color=(255, 100, 100), batch=batch)
    
    def update(self, delta):
        self.pos += delta



## main

def spawn_tile(dt):
    x = random.randrange(0,800)
    y = random.randrange(0,600)
    tiles.append(Tile(x,y,1))


@window.event
def on_draw():
    window.clear()
    batch.draw()

@window.event
def on_mouse_press(x,y,button,modifiers):
    print(f'{x},{y}')
    tiles.append(Tile(x,y,1))

def update(dt):
#    for tile in tiles:
#        tile.update(dt)
#    spawn_tile()
    pass

def on_close():
    print("finished")

pyglet.clock.schedule_interval(update, 1/10.0)
#pyglet.clock.schedule_interval(spawn_tile, 1/2.0)
pyglet.app.run()
    


