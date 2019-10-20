class Laser(GameObject):
    SIZE = 10
    IMAGE = "ball"

    def __init__(self, velocity):
        super.__init__(Laser.IMAGE, Laser.SIZE, (0,0))



    def move(self):
        if (0 <= self.coords[0] <= SCREEN_WIDTH and
            0 <= self.coords[1] <= SCREEN_HEIGHT):
            self.coords[0] += self.velocity[0]
            self.coords[1] += self.velocity[1]
            return 0
        else:
            return -1