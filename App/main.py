from __init__ import *
from OrbObject import OrbitalObject

pygame.init()

SCREEN_WIDTH = 800

SCREEN_HEIGHT = 00

CENTER_X = 700
CENTER_Y = 700


screen = pygame.display.set_mode([1000, 1000])
scrap = OrbitalObject(0, 10, 50, 0)
screen.fill((0,0,0))

pygame.draw.circle(screen, (0, 0, 255), (CENTER_X-50, CENTER_Y), 50)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    scrap.orbit(.1)
    screen.blit(scrap.surf, scrap.rect)
    pygame.display.flip()
    



pygame.quit()