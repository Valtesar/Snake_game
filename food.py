import pygame
import random
from settings import *


class Food:
    def __init__(self, screen):
        """Инициализация еды"""

        self.screen = screen
        self.image = pygame.image.load('images/food.png')
        self.rect = self.image.get_rect()
        self.foodx = round(random.randrange(0, display_width - snake_size) / 10.0) * 10.0
        self.foody = round(random.randrange(0, display_height - snake_size) / 10.0) * 10.0

    def output_food(self):
        """рисование еды"""

        self.screen.blit(self.image, self.rect)
