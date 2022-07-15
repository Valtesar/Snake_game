import pygame
import sys


def events(snake):
    """обработка событий"""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pygame.transform.rotate(snake.image, 180)
            elif event.key == pygame.K_DOWN:
                pygame.transform.rotate(snake.image, 180)
            elif event.key == pygame.K_RIGHT:
                pygame.transform.rotate(snake.image, 180)
            elif event.key == pygame.K_LEFT:
                pygame.transform.rotate(snake.image, 180)


def turn(snake_look):
    """обработка поворотов змейки"""
    if snake_look == 'LEFT' or 'RIGHT':
        # Can turn up or down
    elif snake_look == 'UP' or 'DOWN':
        # Can turn left or right
