import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Suuji")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

circle_radius = 20
circles = []

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                circles.append(pos)
            elif event.button == 3:
                if circles:
                    circles.pop()

    for pos in circles:
        pygame.draw.circle(screen, BLUE, pos, circle_radius)

    pygame.display.flip()

pygame.quit()
sys.exit()

