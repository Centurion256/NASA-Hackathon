from App import *


class Rubbish(object):

    def __init__(self, model, size, start_point, velocity):
        self.model = model
        self.size = size
        self.coords = start_point
        self.velocity = velocity
        self.surface = pygame.transform.scale(pygame.image.load("Data/spaceship.png"), (self.size, self.size))
        # self.surface = pygame.Surface((self.size, self.size))
        self.surface.set_colorkey(pygame.Color(15, 255, 0))
        # self.surface.fill((15, 255, 0))
        # self.color = pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        # pygame.draw.circle(self.surface, self.color, (self.size//2, self.size//2), self.size//2)

    def move(self):
        if (0 <= self.coords[0] <= SCREEN_WIDTH and
                0 <= self.coords[1] <= SCREEN_HEIGHT):
            self.coords[0] += self.velocity[0]
            self.coords[1] += self.velocity[1]
            return 0
        else:
            return -1

    def random_move(self):
        if random.random() < 0.1:
            self.velocity = (random.randint(-10, 10), random.randint(-10, 10))
        return self.move()

    def render(self, screen):
        screen.blit(self.surface, self.coords)
