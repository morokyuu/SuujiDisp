import pyglet
from pyglet.window import key

window = pyglet.window.Window(800, 600, "Train Driver View - Real Mode", vsync=True)
pyglet.gl.glClearColor(0.4, 0.6, 1.0, 1.0)

# パース設定
center_x = window.width // 2
horizon_y = window.height
ground_y = 0
rail_width_bottom = 260
rail_gap_bottom = 160
num_sleepers = 40

# 操作用スピード（加速・減速可能）
speed = 0.02
speed_min, speed_max = 0.005, 0.1

class Sleeper:
    def __init__(self, z):
        self.z = z

    def update(self, dt):
        self.z -= speed * dt * 60
        if self.z < 0.01:
            self.z = 1.0

    def draw(self):
        y = ground_y + (horizon_y - ground_y) * self.z
        scale = 1.0 - self.z
        width = rail_gap_bottom * scale * 1.2
        height = 8 * scale
        x = center_x - width / 2
        sleeper = pyglet.shapes.Rectangle(x, y, width, height, color=(80, 80, 80))
        sleeper.draw()

# 枕木初期化（均等配置）
sleepers = [Sleeper(z) for z in [i / num_sleepers for i in range(1, num_sleepers)]]

# レール描画（パースライン）
def draw_rails():
    rail_left = pyglet.shapes.Line(
        center_x - rail_gap_bottom / 2, ground_y,
        center_x - 30, horizon_y,
        color=(30, 30, 30)
    )
    rail_right = pyglet.shapes.Line(
        center_x + rail_gap_bottom / 2, ground_y,
        center_x + 30, horizon_y,
        color=(30, 30, 30)
    )
    rail_left.width = 12
    rail_right.width = 12
    rail_left.draw()
    rail_right.draw()

# 線路の外側地面（茶色ブロック）
def draw_ground():
    ground = pyglet.shapes.Rectangle(0, 0, window.width, 120, color=(110, 80, 50))
    ground.draw()

def update(dt):
    for sleeper in sleepers:
        sleeper.update(dt)

@window.event
def on_key_press(symbol, modifiers):
    global speed
    if symbol == key.UP:
        speed = min(speed + 0.005, speed_max)
    elif symbol == key.DOWN:
        speed = max(speed - 0.005, speed_min)

@window.event
def on_draw():
    window.clear()
    draw_ground()
    draw_rails()
    for sleeper in sorted(sleepers, key=lambda s: s.z, reverse=True):
        sleeper.draw()

pyglet.clock.schedule_interval(update, 1 / 60.0)
pyglet.app.run()
