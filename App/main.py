import pygame

pygame.init()

SCREEN_WIDTH = 800

SCREEN_HEIGHT = 600


screen = pygame.display.set_mode([500, 500])


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill((100,100,100))
    pygame.display.flip()




pygame.quit()