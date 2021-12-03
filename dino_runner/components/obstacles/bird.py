import random, pygame


from dino_runner.components.obstacles.obstacle import Obstacle


class Bird(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 1)
        super().__init__(image, self.type)
        self.rect.y = 250
        self.step_index = 0

    def draw(self, screen):
        if self.step_index < 5:
            screen.blit(self.image[0], self.rect)
        else:
            screen.blit(self.image[1], self.rect)
        self.step_index += 1
        if self.step_index > 10:
            self.step_index = 0
