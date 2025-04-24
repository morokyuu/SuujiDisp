import pygame as pg
import sys

pg.init()

WIDTH, HEIGHT = 800, 600
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Suuji")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

circle_radius = 20

class Container:
    def __init__(self):
        self.value = 0
        self.b1 = []
        self.b10 = []

        self.b1_pos = (30, 30)
        self.b10_pos = (30, 100)

    def inc(self):
        print(f"value={self.value}")
        self.value += 1
        self._append(1)

    def dec(self):
        pass


    def _append(self,value):
#        if self.value > 0 and (self.value % 10) == 0:

        if value == 1:
            x,y = self.b1_pos
            self.b1.append((x,y))
            self.b1_pos = (x + 40, y)

    def display(self):
        for pos in self.b1:
            pg.draw.circle(screen, BLUE, pos, circle_radius)


cnt = Container()
running = True
while running:
    screen.fill(BLACK)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False

        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                cnt.inc()
            elif event.button == 3:
                cnt.dec()

    cnt.display()
    pg.display.flip()

pg.quit()
sys.exit()

