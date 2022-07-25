import pygame
import time
import random
"""Оконное приложение написанное на языке Python 3.8.2 с использованием фреймворка pygame 2.1.2"""

"""Приложение созданно по прототипу игры змейка.

   Пользователь управляя змейкой должен направлять ее к квадрату с едой. По достижению квадрата колличество очков
   пользователя увеличивается на 1 единицу, а змейка становится длиннее на 1 еденицу.
   
   Игра проигранна будет в том случае, если пользователь столкнется со стеной, либо допустит соприкосновение головы
   змейки с её телом.
   
   Пользователю будет предложенно начать игру заново либо выйти из игры.
   """
pygame.init()

"""Установим константы (R, G, B) цветов для последующего использования"""
WHITE = (255, 255, 255)  # Белый
YELLOW = (255, 255, 102)  # Жёлтый
BLACK = (0, 0, 0)  # Чёрный
RED = (213, 50, 80)  # Красный
GREEN = (0, 255, 0)  # Зеленый
BLUE = (50, 153, 213)  # Синий

"""Установим константы для ширины и высоты игрового поля"""
WIDTH = 600  # Ширина игрового поля
HIGHT = 400  # Высота игрового поля

dis = pygame.display.set_mode((WIDTH, HIGHT))
pygame.display.set_caption('Snake Game by Valtesar')

clock = pygame.time.Clock()

SNAKE_BLOCK = 10  # Размер квадрата змейки в пикселях
SNAKE_SPEED = 15  # Скорость передвижения змейки

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 20)

snake_image = pygame.image.load('images/snake_block.png')
food_image = pygame.image.load('images/food_block.png')


def your_score(score):
    """Метод вывода набранных очков в игре"""

    """Принимает в себя аргумент score - колличество очков"""
    """Отрисовывает на экране значение очков в положении [0, 0]"""

    value = score_font.render("Score: " + str(score), True, YELLOW)
    dis.blit(value, [0, 0])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, BLACK, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    """Метод вывода сообщений на экран пользователя"""

    """Принимает в себя аргуемент msg - текст сообщения и color - цвет текста сообщения"""
    """Отрисовывает на экране текст ровно по центру"""

    text = font_style.render(msg, True, color)
    dis.blit(text, [WIDTH / 6, HIGHT / 3])


def generate_food():
    x1_food = round(random.randrange(0, WIDTH - HIGHT) / 10.0) * 10.0
    y1_food = round(random.randrange(0, HIGHT - SNAKE_BLOCK) / 10.0) * 10.0
    return x1_food, y1_food


def game_loop():
    """Основной игровой метод"""

    """По умолчанию параметры конца игры и закрытия окна в положении 0"""
    game_over = False
    game_close = False

    """Стартовое положение змейки на экране относительно координат <x1> <y1>"""
    x1 = WIDTH / 2
    y1 = HIGHT / 2

    """Изменяемые параметры <x1> <y1> в процессе игры"""
    x1_change = 0
    y1_change = 0

    """Создаем список координат тела змейки и значение стартовой длины змейки"""
    snake_list = []
    length_of_snake = 1

    """Отображение еды змейки на игровом поле используя метод рандом.
        Вычисляет случайное значение <x> и случайное значение <y>
        Округляет его до целого числа int"""
    x1_food = generate_food()[0]
    y1_food = generate_food()[1]

    """Запускаем главный бесконечный цикл программы,
       который работает до тех пор пока пользователь не закроет окно игры"""
    while not game_close:

        """Запускаем вложенный бесконечный цикл програамы,
           который работает до тех пор, пока пользователь не проиграет"""
        while game_over:
            dis.fill(BLUE)
            message("GAME OVER! Space - New game Esc - Quit", RED)
            your_score(length_of_snake - 1)
            pygame.display.update()

            """Отслеживаем игровые события. 
               Нажатие клавишы ESC ведет в выходу из игры.
               Нажатие клавишы Space запускает игру заново"""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_close = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = False
                        game_close = True
                    if event.key == pygame.K_SPACE:
                        game_loop()

        """Отслеживаем игровые события.
           Закрытие игрового окна закрывает приложение без ошибок.
           Нажатие клавишы влево - движение змейки влево <<< X, Y
           Нажатие клавишы вправо - движение змейки вправо X >>>, Y 
           Нажатие клавишы вверх - движение змейки вверх X, Y /| 
           Нажатие клавишы вниз - движение змейки вниз X, Y |/ """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_close = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -SNAKE_BLOCK
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = SNAKE_BLOCK

        """Если змейка попытается выйти за границы игрового поля игра будет завершена проигрышем"""
        if x1 >= WIDTH or x1 < 0 or y1 >= HIGHT or y1 < 0:
            game_over = True

        """Получаем текущие координаты змейки с учетом изменний от пользователя (движения)"""
        x1 += x1_change
        y1 += y1_change
        dis.fill(BLUE)

        """Отрисовываем еду на экране по случайно сгенерированным координатам"""
        pygame.draw.rect(dis, GREEN, [x1_food, y1_food, SNAKE_BLOCK, SNAKE_BLOCK])

        """"Создаем голову змейки и заносим её в основоной список тела змейки первым элементом.
           Если длина списка тела змейки больше чем сама змейка, то удаляем первый элемент (голову)"""
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        """Проверяем каждый элемент в теле змейки, 
           и если его координаты равны координатам головы змейки то игра будет завершена проигрышем"""
        for body in snake_list[:-1]:
            if snake_head == body:
                game_over = True

        our_snake(SNAKE_BLOCK, snake_list)
        your_score(length_of_snake - 1)

        pygame.display.update()
        """Если змейка попадает головой на координаты еды, то генерируем новые координаты еды
           и увеличиваем длинну змейки на 1 еденицу"""
        if x1 == x1_food and y1 == y1_food:
            x1_food = generate_food()[0]
            y1_food = generate_food()[1]
            length_of_snake += 1

        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()


game_loop()
