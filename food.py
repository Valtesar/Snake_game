import pygame


class Food():
    def __init__(self, screen):
        """Инициализация еды"""

        self.screen = screen
        self.image = pygame.image.load('images/food.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.topleft = self.screen_rect.topleft

    def output_food(self):
        """рисование еды"""

        self.screen.blit(self.image, self.rect)
