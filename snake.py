import pygame
import time


class Snake:
    """Класс игрового персонажа змейка"""

    def __init__(self, background):
        """Инициализация змейки"""

        """
        Входные параметры: background - фон игры, image - изоображение змейки
        """

        self.background = background
        self.image_head = pygame.image.load('images/snake_head.png')
        self.rect = self.image_head.get_rect()
        self.background_rect = background.get_rect()
        self.rect.centerx = self.background_rect.centerx
        self.rect.bottom = self.background_rect.bottom
        self.rect.x = 300
        self.rect.y = 300
        self.x_change = 0
        self.y_change = 0

    def update(self):
        """Метод движение змейки"""

        # Snake.turn(self, angle=90)  # Если вызывается метод смены направления, то вызыввает метод поворота спрайта

        """"обработка границ экрана движения змейки"""
        if self.rect.x > 700:
            self.rect.x = 0
        elif self.rect.x < 0:
            self.rect.x = 700

        if self.rect.bottom < 0:
            self.rect.top = 800
        elif self.rect.top > 800:
            self.rect.bottom = 0

    def move(self, x=0, y=0):
        while x != 0 and y != 0:
            self.rect.x += x
            self.rect.y += y


    def end_move(self):
        """Метод окончания игры"""
        pass

    def turn(self, angle):
        """Метод поворота змейки"""

        self.image_head = pygame.transform.rotate(self.image_head, angle)

    def get_food(self):
        """Метод поглощения еды"""
        pass

    def output_snake(self):
        """Метод отображения змейки"""
        self.rect.x += self.x_change
        self.rect.y += self.y_change
        self.background.blit(self.image_head, [self.rect.x, self.rect.y, 10, 10])
