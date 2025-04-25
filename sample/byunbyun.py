import pyglet
import random
import math

window = pyglet.window.Window(800, 600, "Tile Rush!", resizable=False)
center_x, center_y = window.width // 2, window.height // 2

batch = pyglet.graphics.Batch()

# タイルの設定
TILE_SIZE = 20
TILE_SPEED = 300  # pixels per second

tiles = []

class Tile:
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.sprite = pyglet.shapes.Rectangle(x, y, TILE_SIZE, TILE_SIZE, color=(255, 100, 100), batch=batch)
        self.dx = dx
        self.dy = dy

    def update(self, dt):
        self.x += self.dx * dt
        self.y += self.dy * dt
        self.sprite.x = self.x
        self.sprite.y = self.y

def spawn_tile():
    # ランダムな辺から出現させる
    side = random.choice(['top', 'bottom', 'left', 'right'])
    if side == 'top':
        x = random.randint(0, window.width)
        y = window.height + TILE_SIZE
    elif side == 'bottom':
        x = random.randint(0, window.width)
        y = -TILE_SIZE
    elif side == 'left':
        x = -TILE_SIZE
        y = random.randint(0, window.height)
    elif side == 'right':
        x = window.width + TILE_SIZE
        y = random.randint(0, window.height)

    # 中心への方向ベクトルを計算
    angle = math.atan2(center_y - y, center_x - x)
    dx = math.cos(angle) * TILE_SPEED
    dy = math.sin(angle) * TILE_SPEED

    tile = Tile(x, y, dx, dy)
    tiles.append(tile)

@window.event
def on_draw():
    window.clear()
    batch.draw()

def update(dt):
    for tile in tiles:
        tile.update(dt)
    # タイルを一定間隔で生成
    spawn_tile()

# 毎秒60フレームで更新
pyglet.clock.schedule_interval(update, 1/60.0)
pyglet.app.run()
