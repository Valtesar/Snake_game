import pygame
import sys


def events(snake):
    """Обработка нажатий пользователем клавиш управления и выхода из игры"""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                up = 90
                snake.turn(up)
            elif event.key == pygame.K_DOWN:
                image = pygame.transform.rotate(snake.image, 180)
            elif event.key == pygame.K_RIGHT:
                image = pygame.transform.rotate(snake.image, 180)
            elif event.key == pygame.K_LEFT:
                image = pygame.transform.rotate(snake.image, 180)


def turn(snake_look):
    """обработка поворотов змейки"""
    if snake_look == 'LEFT' or 'RIGHT':
        pass
        # Can turn up or down
    elif snake_look == 'UP' or 'DOWN':
        pass
        # Can turn left or right
