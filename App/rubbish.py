from App import *


class Rubbish(GameObject):

    def __init__(self, image_name, size, start_point, velocity):
        image_name = "scrap_{}".format(random.randint(1, 7))
        
        super().__init__(image_name, size, start_point)
        self.velocity = velocity


    def move(self):
        if (0 <= self.coords[0] <= SCREEN_WIDTH and
                0 <= self.coords[1] <= SCREEN_HEIGHT):
            self.coords[0] += self.velocity[0]
            self.coords[1] += self.velocity[1]
            # self.coords[0] = self.coords[0]%SCREEN_WIDTH
            # self.coords[1] = self.coords[1]%SCREEN_WIDTH

            return 0
        else:
            return -1

    def random_move(self):
        if random.random() < 0.1:
            self.velocity = (random.randint(-5, 5), random.randint(-5, 5))
        return self.move()

    def ISS_colision(self, iss):
        if (iss.coords[0] <= self.coords[0] <= iss.coords[0] + iss.size and
                iss.coords[1] <= self.coords[1] <= iss.coords[1] + iss.size):
            return -1
        else:
            return 0

    def reset(self):
        self.coords = random.choice([[random.randint(0, SCREEN_WIDTH),0], [random.randint(0, SCREEN_WIDTH), SCREEN_HEIGHT], 
                                      [0, random.randint(0, SCREEN_HEIGHT)], [SCREEN_WIDTH, random.randint(0, SCREEN_HEIGHT)]])

    def mouse_collision(self, mouse_pos):
        if (self.coords[0] <= mouse_pos[0] <= self.coords[0] + self.size) and\
                (self.coords[1] <= mouse_pos[1] <= self.coords[1] + self.size):
            print("Collide")
            self.velocity = (random.randint(-5, 5), random.randint(-5, 5))
