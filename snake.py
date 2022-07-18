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

    def auto_move(self):
        """Метод движение змейки"""
        self.rect.x += 1
        if self.rect.left > 800:
            self.rect.right = 0

    def end_move(self):
        """Метод окончания игры"""
        pass

    def turn(self, direction):
        """Метод поворота змейки"""
        self.image = pygame.transform.rotate(self.image, direction)

    def get_food(self):
        """Метод поглощения еды"""
        pass

    def output_snake(self):
        """Метод отображения змейки"""
        self.background.blit(self.image, self.rect)
