from App import pygame

class GameObject:
        def __init__(self, image_name, size, start_point):
            self.size = size
            self.coords = start_point
            self._image_name = "Data/{}.png".format(image_name)
            self.surface = pygame.transform.scale(pygame.image.load(self._image_name), (self.size, self.size))
            # self.surface = pygame.Surface((self.size, self.size))
            self.surface.set_colorkey(pygame.Color(15, 255, 0))
            # self.surface.fill((15, 255, 0))
            # self.color = pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            # pygame.draw.circle(self.surface, self.color, (self.size//2, self.size//2), self.size//2)

        def render(self, screen):
            screen.blit(self.surface, self.coords)

