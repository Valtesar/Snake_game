import pygame
import controls
from snake import Snake
from food import Food


def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption('Snake')
    bg_colour = (0, 0, 0)
    snake = Snake(screen)
    food = Food(screen)

    while True:

        controls.events(snake)
        screen.fill(bg_colour)
        snake.output_snake()
        snake.move()
        food.output_food()
        pygame.display.flip()


if __name__ == '__main__':
    run()
    pygame.mixer.init()

