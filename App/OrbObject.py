from main import *

class OrbitalObject(pygame.sprite.Sprite):
    def __init__(self, x, y, vx, vy):
        super(OrbitalObject, self).__init__()
        self.surf = pygame.Surface((10, 10))
        self.surf.fill((255,255,255))
        self.rect = self.surf.pygame.Surface.get_rect(center = (x + CENTER_X, y + CENTER_Y))
        self.vx = vx
        self.vy = vy

    def get_x(self):
        return self.rect.x - CENTER_X

    def get_y(self):
        
        return self.rect.y - CENTER_Y
        
    def orbit(self, timestep):
        self.rect.move_ip(round(self.vx*timestep), round(self.vy*timestep))
        self.vx += -(self.rect.x / (self.rect.x**2 + self.rect.y**2)**.5)*timestep
        self.vx += -(self.rect.y / (self.rect.x**2 + self.rect.y**2)**.5)*timestep

    def draw(self, ):
        pass
