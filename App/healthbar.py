from App import pygame

class Healthbar:
    GAME_HP_BAR_X = 10
    GAME_HP_BAR_Y = 10
    HPBAR_IMAGE_STR = "HP_bar1"
    HPTCK_IMAGE_STR = "HP_tick"

    def __init__(self, iss):
        self.iss = iss
        self._hp_bar_image =pygame.image.load("Data/{}.png".format(Healthbar.HPBAR_IMAGE_STR))
        self._hp_tick_image = pygame.image.load("Data/{}.png".format(Healthbar.HPTCK_IMAGE_STR))


    def render(self, screen):
        screen.blit(self._hp_bar_image, (Healthbar.GAME_HP_BAR_X, Healthbar.GAME_HP_BAR_Y))
        for temp in range(self.iss.hp):
            screen.blit(self._hp_tick_image, (Healthbar.GAME_HP_BAR_X + 4 + 2 * temp, Healthbar.GAME_HP_BAR_X + 6))