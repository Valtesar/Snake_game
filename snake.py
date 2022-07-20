import pygame
import controls
import time


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

    def move(self, direction='right'):
        """Метод движение змейки"""

        # Snake.turn(self, angle=90)  # Если вызывается метод смены направления, то вызыввает метод поворота спрайта

        if direction == 'up':
            self.rect.y -= 20
        elif direction == 'down':
            self.rect.y += 20
        elif direction == 'right':
            self.rect.x += 20
        elif direction == 'left':
            self.rect.x -= 20

        """"обработка границ экрана движения змейки"""

        if self.rect.left > 700:
            self.rect.right = 0
        elif self.rect.right < 0:
            self.rect.left = 700


    def end_move(self):
        """Метод окончания игры"""
        pass

    def turn(self, angle):
        """Метод поворота змейки"""

        self.image = pygame.transform.rotate(self.image, angle)

    def get_food(self):
        """Метод поглощения еды"""
        pass

    def output_snake(self):
        """Метод отображения змейки"""
        self.background.blit(self.image, self.rect)
