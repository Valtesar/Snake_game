import pygame
import controls
from snake import Snake
from food import Food
from settings import *
from menu import message

game_over = False
game_close = False


def run():

    pygame.init()
    snake = Snake(display)
    food = Food(display)

    while not game_over:

        while game_close:
            display.fill(bg_colour)
            message('Game over!\nPress enter for new game\nPress Esc to exit', font_color)
            pygame.display.update()
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

