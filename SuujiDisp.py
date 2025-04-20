import pyglet
from Basket import Basket


window = pyglet.window.Window(800, 600, "Tile Rush!", resizable=False)
center_x, center_y = window.width // 2, window.height // 2

batch = pyglet.graphics.Batch()



class Display:
    def __init__(self, bsk:Basket):
        self.value = 0
    

@window.event
def on_draw():
    window.clear()
    batch.draw()

def update(dt):
    for tile in tiles:
        tile.update(dt)
    spawn_tile()

pyglet.clock.schedule_interval(update, 1/60.0)
pyglet.app.run()
    


