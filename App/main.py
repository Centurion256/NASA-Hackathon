import pygame
from OrbObject import OrbObject

pygame.init()

SCREEN_WIDTH = 800

SCREEN_HEIGHT = 00

CENTER_X = 400
CENTER_Y = 400


screen = pygame.display.set_mode([500, 500])
scrap = OrbObject(0, 10, 100, 0)
screen.fill((0,0,0))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    scrap.orbit(.01)
    screen.blit(scrap.surf, scrap.rect)
    screen.flip()
    



pygame.quit()