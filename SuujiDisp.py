import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Suuji")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

circle_radius = 20

class Container:
    def __init__(self):
        self.value = 0
        self.circles = []

    def inc(self):
        self.value += value
        b1 = self.value % 10
        b10 = self.value // 10

        for pos in circles:
            pygame.draw.circle(screen, BLUE, pos, circle_radius)

    def dec(self):
        pass


    def display(self):
        pygame.draw.circle(screen, BLUE, pos, circle_radius)


running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                cnt.inc()
            elif event.button == 3:
                cnt.dec()

    pygame.display.flip()

pygame.quit()
sys.exit()

