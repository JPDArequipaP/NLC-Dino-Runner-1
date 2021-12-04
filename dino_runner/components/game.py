import pygame

from dino_runner.components.life_manager import LifeManager
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.text_utils import get_score_element, get_message
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, WHITE_COLOR, BLACK_COLOR, GAME_OVER_IMG, RESET_IMG, DINO_START, RED_COLOR, BROWN_COLOR
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.power_ups.power_up_manager import PowerUpManager



class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.points = 0
        self.running = True
        self.death_count = 0
        self.powerup_manager = PowerUpManager()
        self.life_manager = LifeManager()
        self.dark = False

    def run(self):
        self.game_speed = 20
        self.points = 0
        self.create_components()
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def create_components(self):
        self.obstacle_manager.reset_obstacles()
        self.powerup_manager.reset_power_ups(self.points, self.player)
        self.life_manager.new_lifes()

    def execute(self):
        while self.running:
            if not self.playing:
                self.show_menu()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self, self.screen)
        self.powerup_manager.update(self.points, self.game_speed, self.player)

    def draw(self):
        self.clock.tick(FPS)
        self.dark_mode()
        self.score()
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.powerup_manager.draw(self.screen)
        self.life_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def dark_mode(self):
        if self.points % 200 == 0:
            if (self.points / 200) % 2 == 0:
                self.dark = False
            else:
                self.dark = True
        if self.dark:
            self.screen.fill(BLACK_COLOR)
        else:
            self.screen.fill(WHITE_COLOR)

    def score(self):
        self.points += 1
        if self.points % 100 == 0:
            self.game_speed += 1
        score, score_rect = self.change_score_color()
        self.screen.blit(score, score_rect)
        self.player.check_invincibility(self.screen, self.dark)

    def change_score_color(self):
        if self.dark:
            return get_score_element(self.points, color=WHITE_COLOR)
        else:
            return get_score_element(self.points)

    def show_menu(self):
        pygame.time.delay(600)
        self.running = True
        self.screen.fill(WHITE_COLOR)

        self.print_menu_elements(self.death_count)

        # The view of the game is updated
        pygame.display.update()

        self.handle_key_events_on_menu()

    def print_menu_elements(self, death_count=0):

        #They are optional for message's paramethers
        half_screen_width = SCREEN_WIDTH // 2
        half_screen_height = SCREEN_HEIGHT // 2

        if death_count == 0:
            text, text_rect = get_message('Press any key to Start the game')
            self.screen.blit(DINO_START, (half_screen_width - 50 , half_screen_height - 200))

        else:
            self.screen.blit(GAME_OVER_IMG, (half_screen_width - 200, half_screen_height - 220))
            self.screen.blit(RESET_IMG, (half_screen_width - 40, half_screen_height -150))
            text, text_rect = get_message('Press any key to Restart the game')
            death, death_rect = get_message('Death count: {}'.format(death_count), half_screen_width+20, half_screen_height+45, color=RED_COLOR)
            self.screen.blit(death, death_rect)
            score, score_rect = get_message("FINAL SCORE: " + str(self.points), half_screen_width+20, half_screen_height+80, color=BROWN_COLOR)
            self.screen.blit(score, score_rect)

        self.screen.blit(text, text_rect)

    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
                pygame.display.quit()
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                self.run()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed




