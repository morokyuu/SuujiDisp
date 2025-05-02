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
        self.b100 = 0

        self.b1_pos = (70, 50)
        self.b10_pos = (50, 80)
        #self.font = pg.font.SysFont('Times New Roman',100)
        self.font = pg.font.Font("C:/Windows/Fonts/meiryo.ttc", 200)
        self.yomifont = pg.font.Font("C:/Windows/Fonts/meiryo.ttc", 50)
        self.text = self.font.render(f"{self.value}",True,WHITE)

    def _keta(self,value):
        self.b1 = value % 10
        self.b10 = value // 10 % 10
        self.b100 = value // 100 % 10

    def inc(self):
        self.value += 1
        if self.value > 100:
            self.value = 100
        self._keta(self.value)

    def dec(self):
        self.value -= 1
        if self.value < 0:
            self.value = 0
            return
        self._keta(self.value)

    def _yomigana(self):
        kk1 = ["ぜろ", "いち", "に", "さん", "し", "ご", "ろく", "しち", "はち", "きゅう"]
        kk10 = ["", "じゅう", "にじゅう", "さんじゅう", "よんじゅう", "ごじゅう", "ろくじゅう", "しちじゅう", "はちじゅう", "きゅうじゅう"]
        kk100 = ["", "ひやく"]
        #print(f"{self.b100},{self.b10},{self.b1}")

        if self.b100 == 1 and self.b10 == 0 and self.b1 == 0:
            k100,k10,k1 = kk100[1],"",""
        elif self.b100 == 0 and self.b10 > 0 and self.b1 == 0:
            k100,k10,k1 = "",kk10[self.b10],""
        else:
            k100,k10,k1 = "",kk10[self.b10],kk1[self.b1]

        return k100,k10,k1

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

        if self.b100:
            x,y = self.b10_pos
            for i in range(10):
                pos = (x,y+i*50)
                pg.draw.rect(screen, GRAY, pg.Rect(*pos,*rect_size), circle_radius)

                for j in range(10):
                    pos = (x+circle_radius+j*40, y+circle_radius+i*50)
                    pg.draw.circle(screen, BLUE, pos, circle_radius)

        # suuji
        self.text = self.font.render(f"{self.value}",True,WHITE)
        screen.blit(self.text, (430,170))

        # yomigana
        k100,k10,k1 = self._yomigana()
        yomi_1 = self.yomifont.render(f"{k1}",True,WHITE)
        screen.blit(yomi_1, (650,400))
        yomi_10 = self.yomifont.render(f"{k10}",True,WHITE)
        screen.blit(yomi_10, (350,400))
        yomi_100 = self.yomifont.render(f"{k100}",True,WHITE)
        screen.blit(yomi_100, (280,400))
        
#        w,h = self.yomifont.size(f"{k10}")
#        print(w)

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
    screen = pg.display.set_mode((WIDTH, HEIGHT), pg.FULLSCREEN)
    #screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption("Suuji")
    mainlp()



