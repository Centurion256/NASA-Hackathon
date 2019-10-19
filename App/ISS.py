import pygame
from App.constants import *


class ISS(object):

    def __init__(self):
        self.hp = 0
        self.size = 150
        self.surface = pygame.Surface((self.size, self.size))
        self.surface.set_colorkey(pygame.Color(15, 255, 0))
        self.surface.fill((100, 100, 100))

    def render(self, screen):
        screen.blit(self.surface, ((SCREEN_WIDTH-self.size)//2, (SCREEN_HEIGHT-self.size)//2))
