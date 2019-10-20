import pygame
from App.constants import *


class ISS(object):

    def __init__(self):
        self.hp = 0
        self.size = 250
        self.surface = pygame.transform.scale(pygame.image.load("../Data/ISS.png"), (self.size, self.size))
        self.surface.set_colorkey(pygame.Color(15, 255, 0))

    def render(self, screen):
        screen.blit(self.surface, ((SCREEN_WIDTH-self.size)//2, (SCREEN_HEIGHT-self.size)//2))
