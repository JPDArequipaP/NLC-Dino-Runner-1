import pygame
from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH, BLACK_COLOR

FONT_STYLE = 'freesansbold.ttf'


def get_score_element(points, color=BLACK_COLOR):
    font = pygame.font.Font(FONT_STYLE, 30)
    text = font.render("Points: {}".format(points), True, color)
    text_rect = text.get_rect()
    text_rect.center = (100, 40)
    return text, text_rect


def get_message(message, width=SCREEN_WIDTH // 2, height=SCREEN_HEIGHT // 2, color=BLACK_COLOR):
    font = pygame.font.Font(FONT_STYLE, 30)
    text = font.render(message, True, color)
    text_rect = text.get_rect()
    text_rect.center = (width, height)
    return text, text_rect

