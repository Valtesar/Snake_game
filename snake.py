import pygame
import controls


class Snake():
    """Класс игрового персонажа змейка"""

    def __init__(self, background):
        """Инициализация змейки"""


        """
        Входные параметры: background - фон игры, image - изоображение змейки
        """

        self.background = background
        self.image = pygame.image.load('images/snake_head.png')
        self.rect = self.image.get_rect()
        self.background_rect = background.get_rect()
        self.rect.centerx = self.background_rect.centerx
        self.rect.bottom = self.background_rect.bottom

    def move(self):
        """Метод движение змейки"""
        self.rect.x += 1
        if self.rect.left > 800:
            self.rect.right = 0

    def output_snake(self, turn):
        """Метод отображения змейки"""
        self.background.blit(turn, self.rect)
