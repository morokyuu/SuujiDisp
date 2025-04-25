import pyglet
import random
import math

window = pyglet.window.Window(800, 600, "Tile Rush 2.0!", resizable=False)
center_x, center_y = window.width // 2, window.height // 2

batch = pyglet.graphics.Batch()

# 定数
TILE_START_SIZE = 40
TILE_MIN_SIZE = 5
TILE_MIN_SPEED = 150
TILE_MAX_SPEED = 350
TILE_COLOR_START = (255, 100, 100)
TILE_COLOR_END = (180, 0, 0)
REMOVE_DISTANCE = 10  # 中心から何px以内に来たら消すか

tiles = []

class Tile:
    def __init__(self, x, y, dx, dy, speed):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.speed = speed
        self.distance_start = self.distance_to_center()
        self.size = TILE_START_SIZE
        self.sprite = pyglet.shapes.Rectangle(self.x, self.y, self.size, self.size, color=TILE_COLOR_START, batch=batch)

    def distance_to_center(self):
        return math.hypot(center_x - self.x, center_y - self.y)

    def update(self, dt):
        self.x += self.dx * dt
        self.y += self.dy * dt

        dist_now = self.distance_to_center()
        t = max(0.0, min(1.0, dist_now / self.distance_start))

        # サイズ縮小
        size = TILE_MIN_SIZE + (TILE_START_SIZE - TILE_MIN_SIZE) * t
        self.sprite.width = self.sprite.height = size
        self.size = size

        # 色変化（線形補間）
        r = int(TILE_COLOR_END[0] + (TILE_COLOR_START[0] - TILE_COLOR_END[0]) * t)
        g = int(TILE_COLOR_END[1] + (TILE_COLOR_START[1] - TILE_COLOR_END[1]) * t)
        b = int(TILE_COLOR_END[2] + (TILE_COLOR_START[2] - TILE_COLOR_END[2]) * t)
        self.sprite.color = (r, g, b)

        # スプライト位置調整（サイズが変わるので中心に揃える）
        self.sprite.x = self.x - size / 2
        self.sprite.y = self.y - size / 2

        # 中心に近づいたら削除
        return dist_now > REMOVE_DISTANCE

def spawn_tile():
    side = random.choice(['top', 'bottom', 'left', 'right'])
    if side == 'top':
        x = random.randint(0, window.width)
        y = window.height + TILE_START_SIZE
    elif side == 'bottom':
        x = random.randint(0, window.width)
        y = -TILE_START_SIZE
    elif side == 'left':
        x = -TILE_START_SIZE
        y = random.randint(0, window.height)
    elif side == 'right':
        x = window.width + TILE_START_SIZE
        y = random.randint(0, window.height)

    # 中心へ向かうベクトルとスピード
    angle = math.atan2(center_y - y, center_x - x)
    speed = random.uniform(TILE_MIN_SPEED, TILE_MAX_SPEED)
    dx = math.cos(angle) * speed
    dy = math.sin(angle) * speed

    tile = Tile(x, y, dx, dy, speed)
    tiles.append(tile)

@window.event
def on_draw():
    window.clear()
    batch.draw()

def update(dt):
    # タイル更新 & 消去処理
    global tiles
    tiles = [tile for tile in tiles if tile.update(dt)]
    # タイルを定期的に生成
    spawn_tile()

pyglet.clock.schedule_interval(update, 1/60.0)
pyglet.app.run()
