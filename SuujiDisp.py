import pygame as pg
import sys
import numpy as np

pg.init()

WIDTH, HEIGHT = 800, 600
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Suuji")

WHITE = (255, 255, 255)
GRAY = (170, 170, 170)
BLACK = (0, 0, 0)
BLUE = (100, 100, 255)

circle_radius = 20
#font = pg.font.Font('Times New Roman',30)
font = pg.font.SysFont('Times New Roman',100)

def Vec2Int(vec):
    return int(vec[0]),int(vec[1])

class Container:
    def __init__(self):
        self.value = 0
        self.b1 = 0
        self.b10 = 0

        self.b1_pos = (70, 50)
        self.b10_pos = (50, 80)
        self.text = font.render(f"{self.value}",True,WHITE)

    def inc(self):
        self.value += 1
        self.b1 = self.value % 10
        self.b10 = self.value // 10
        print(f"value={self.value}")
        self.text = font.render(f"{self.value}",True,WHITE)


    def dec(self):
        self.value -= 1
        if self.value < 0:
            self.value = 0
            return
        self.b1 = self.value % 10
        self.b10 = self.value // 10
        print(f"value={self.value}")
        self.text = font.render(f"{self.value}",True,WHITE)

    def _append(self,value):
        if self.value > 0 and (self.value % 10) == 0:
            self.b1.clear()
            x,y = self.b10_pos
            i = self.value // 10
            self.b10.append((x,y+i*50))
        else:
            x,y = self.b1_pos
            j = self.value % 10
            self.b1.append((x+j*40,y))

    def _remove(self,value):
        d1 = self.value % 10
        d10 = self.value // 10
        print(f'{d1},{d10}')
        x,y = self.b1_pos

        ## borrow
        if d1 == 9:
            self.b10.pop()
            for j in range(9):
                self.b1.append((x+j*40,y))
        else:
            self.b1.pop()

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
        screen.blit(self.text, (500,200))

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

