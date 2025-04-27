import pygame as pg
import sys
import numpy as np


WHITE = (255, 255, 255)
GRAY = (170, 170, 170)
BLACK = (0, 0, 0)
BLUE = (100, 100, 255)

circle_radius = 20

def Vec2Int(vec):
    return int(vec[0]),int(vec[1])

class Container:
    def __init__(self):
        self.value = 0
        self.b1 = 0
        self.b10 = 0

        self.b1_pos = (70, 50)
        self.b10_pos = (50, 80)
        self.font = pg.font.SysFont('Times New Roman',100)
        self.text = self.font.render(f"{self.value}",True,WHITE)

    def _keta(self,value):
        self.b1 = value % 10
        self.b10 = value // 10

    def inc(self):
        self.value += 1
        self._keta(self.value)

    def dec(self):
        self.value -= 1
        if self.value < 0:
            self.value = 0
            return
        self._keta(self.value)

    def display(self):
        rect_size = (40*10, circle_radius*2)

        x,y = self.b1_pos
        for j in range(self.b1):
            pos = (x+j*40, y)
            pg.draw.circle(screen, BLUE, pos, circle_radius)

        x,y = self.b10_pos
        for i in range(self.b10):
            pos = (x,y+i*50)
            pg.draw.rect(screen, GRAY, pg.Rect(*pos,*rect_size), circle_radius)

            for j in range(10):
                pos = (x+circle_radius+j*40, y+circle_radius+i*50)
                pg.draw.circle(screen, BLUE, pos, circle_radius)

        self.text = self.font.render(f"{self.value}",True,WHITE)
        screen.blit(self.text, (500,200))

def mainlp():
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


if __name__ == '__main__':
    pg.init()

    WIDTH, HEIGHT = 800, 600
    #screen = pg.display.set_mode((WIDTH, HEIGHT), pg.FULLSCREEN)
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption("Suuji")
    mainlp()



