from App import *


class ISS(GameObject):
    SIZE = 150

    def __init__(self):
        super().__init__("11 (3)", ISS.SIZE, ((SCREEN_WIDTH-ISS.SIZE)//2, (SCREEN_HEIGHT-ISS.SIZE)//2))
        self.hp = 100




