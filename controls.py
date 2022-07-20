import pygame
import sys


def events(snake):
    """Обработка нажатий пользователем клавиш управления и выхода из игры"""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.y_change -= 10
                snake.x_change = 0
            elif event.key == pygame.K_DOWN:
                snake.y_change = 10
                snake.x_change = 0
            elif event.key == pygame.K_RIGHT:
                snake.x_change = 10
                snake.y_change = 0
            elif event.key == pygame.K_LEFT:
                snake.x_change -= 10
                snake.y_change = 0


def turn(snake_look):
    """обработка поворотов змейки"""
    if snake_look == 'LEFT' or 'RIGHT':
        pass
        # Can turn up or down
    elif snake_look == 'UP' or 'DOWN':
        pass
        # Can turn left or right
