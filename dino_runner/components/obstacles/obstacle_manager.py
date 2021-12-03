import random
import pygame

from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD


class ObstacleManager:

    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            self.obstacles.append(random.choice([Cactus(SMALL_CACTUS), Cactus(LARGE_CACTUS), Bird(BIRD)]))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)

            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.shield:
                    if game.life_manager.life_counter() == 1:
                        game.death_count += 1
                        pygame.time.delay(500)
                        game.playing = False
                        break
                    else:
                        game.life_manager.delete_life()
                self.obstacles.remove(obstacle)

            #

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []
