import pyglet
import random
import math

window = pyglet.window.Window(800, 600, "Tile Rush Spiral FX!", resizable=False)
center_x, center_y = window.width // 2, window.height // 2

batch = pyglet.graphics.Batch()

TILE_START_SIZE = 40
TILE_MIN_SIZE = 5
TILE_MIN_SPEED = 150
TILE_MAX_SPEED = 300
REMOVE_DISTANCE = 10
SPIRAL_ROTATE_SPEED = 4.3  # ラジアン毎秒

tiles = []

def random_vibrant_color():
    return tuple(random.randint(128, 255) for _ in range(3))

class Tile:
    def __init__(self, x, y, angle, speed, color, sparkle=False):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = speed
        self.color = color
        self.sparkle = sparkle
        self.distance_start = self.distance_to_center()
        self.size = TILE_START_SIZE
        self.sprite = pyglet.shapes.Rectangle(x, y, self.size, self.size, color=color, batch=batch)
        self.sprite.opacity = 255

    def distance_to_center(self):
        return math.hypot(center_x - self.x, center_y - self.y)

    def update(self, dt):
        # スパイラル角度更新
        self.angle += SPIRAL_ROTATE_SPEED * dt

        # 中心へ向かって進む（角度付き）
        dist = self.distance_to_center()
        if dist == 0: dist = 0.01  # ZeroDivision 回避

        dx = math.cos(self.angle) * self.speed * dt
        dy = math.sin(self.angle) * self.speed * dt
        dir_to_center_x = center_x - self.x
        dir_to_center_y = center_y - self.y
        factor = self.speed * dt / dist

        self.x += dir_to_center_x * factor + dx * 0.3
        self.y += dir_to_center_y * factor + dy * 0.3

        dist_now = self.distance_to_center()
        t = max(0.0, min(1.0, dist_now / self.distance_start))

        # サイズ・色・位置調整
        size = TILE_MIN_SIZE + (TILE_START_SIZE - TILE_MIN_SIZE) * t
        self.sprite.width = self.sprite.height = size
        self.sprite.x = self.x - size / 2
        self.sprite.y = self.y - size / 2

        # 光らせる（たまにピカッと）
        if self.sparkle and random.random() < 0.1:
            self.sprite.opacity = 255
        else:
            self.sprite.opacity = int(100 + 155 * t)

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

    angle = math.atan2(center_y - y, center_x - x)
    speed = random.uniform(TILE_MIN_SPEED, TILE_MAX_SPEED)
    color = random_vibrant_color()
    sparkle = random.random() < 0.8  # 80%くらい光る

    tile = Tile(x, y, angle, speed, color, sparkle)
    tiles.append(tile)

@window.event
def on_draw():
    window.clear()
    batch.draw()

def update(dt):
    global tiles
    tiles = [tile for tile in tiles if tile.update(dt)]
    spawn_tile()

pyglet.clock.schedule_interval(update, 1/60.0)
pyglet.app.run()
