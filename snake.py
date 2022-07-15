import pygame


class Snake():
    def __init__(self, screen):
        """Инициализация змейки"""

        self.screen = screen
        self.image = pygame.image.load('images/snake_head.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def move(self):
        """движение змейки"""
        self.rect.x += 1
        if self.rect.left > 800:
            self.rect.right = 0

    def output_snake(self):
        """рисование змейки"""

        self.screen.blit(self.image, self.rect)
