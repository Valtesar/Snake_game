import pygame
import controls
from snake import Snake
from food import Food
from settings import *


def run():
    pygame.init()
    snake = Snake(display)
    food = Food(display)
    while True:

        controls.events(snake)
        display.fill(bg_colour)
        food.output_food()
        snake.output_snake()
        snake.update()
        pygame.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    run()
    pygame.mixer.init()

