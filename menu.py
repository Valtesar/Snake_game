import pygame
from main import game_close, game_over, run


def message(text, colour):
    pass


def game_over_events():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = True
                game_close = False
            if event.key == pygame.K_KP_ENTER:
                run()
