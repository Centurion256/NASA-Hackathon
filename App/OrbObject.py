from __init__ import *
class OrbitalObject(pygame.sprite.Sprite):
    def __init__(self, x, y, vx, vy):
        super(OrbitalObject, self).__init__()
        self.surf = pygame.Surface((10, 10))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect(center = (x + CENTER_X, y + CENTER_Y))
        self.vx = vx
        self.vy = vy
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        
        return self.y
        
    def orbit(self, timestep):
        self.x += self.vx*timestep
        self.y += self.vy*timestep
        self.rect.move_ip(round(self.x + CENTER_X)-self.rect.x, round(self.y + CENTER_Y)-self.rect.y)
        self.vx += -GRAV_CONST*(self.get_x() / (self.get_x()**2 + self.get_y()**2)**.5)*timestep
        self.vy += -GRAV_CONST*(self.get_y() /  (self.get_x()**2 + self.get_y()**2)**.5)*timestep

    def draw(self, ):
        pass
