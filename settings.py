import pygame


display_width = 1000
display_height = 800
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game by Valtesar')

clock = pygame.time.Clock()

snake_size = 10
snake_speed = 10

# font_style = pygame.font.SysFont("bahnschrift", 25)
# score_font = pygame.font.SysFont("comicsansms", 35)

bg_colour = (0, 0, 0)
font_color = (220, 50, 40)
