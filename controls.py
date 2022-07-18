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
                snake.move('up')
            elif event.key == pygame.K_DOWN:
                down = -90
                snake.turn('down', down)
                snake.move('down')
            elif event.key == pygame.K_RIGHT:
                right = 90
                snake.turn('right', right)
                snake.move('right')
            elif event.key == pygame.K_LEFT:
                left = 90
                snake.turn('left', left)
                snake.move('left')


def turn(snake_look):
    """обработка поворотов змейки"""
    if snake_look == 'LEFT' or 'RIGHT':
        pass
        # Can turn up or down
    elif snake_look == 'UP' or 'DOWN':
        pass
        # Can turn left or right
