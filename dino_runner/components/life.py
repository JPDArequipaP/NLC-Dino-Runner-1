from pygame.sprite import Sprite

from dino_runner.utils.constants import HEART


class Life(Sprite):
    def __init__(self, pos_x):
        self.image = HEART
        self.pos_x = pos_x
        self.life_rect = self.image.get_rect()
        self.life_rect.x = self.pos_x
        self.life_rect.y = 60

    def draw(self, screen):
        screen.blit(self.image, self.life_rect)

