#!/usr/bin/python
import pygame as pg
import time
import random
from os import path

"""Оконное приложение написанное на языке Python 3.8.2 с использованием фреймворка pygame 2.1.2"""

"""Приложение созданно по прототипу игры змейка.

   Пользователь управляя змейкой должен направлять ее к квадрату с едой. По достижению квадрата колличество очков
   пользователя увеличивается на 1 единицу, а змейка становится длиннее на 1 еденицу.
   
   Игра проигранна будет в том случае, если пользователь столкнется со стеной, либо допустит соприкосновение головы
   змейки с её телом.
   
   Пользователю будет предложенно начать игру заново либо выйти из игры.
   """
pg.init()

"""Установим константы (R, G, B) цветов для последующего использования"""
YELLOW = (255, 255, 102)  # Жёлтый
BLACK = (0, 0, 0)  # Чёрный

"""Установим константы для ширины и высоты игрового поля"""
WIDTH = 600  # Ширина игрового поля
HIGHT = 400  # Высота игрового поля

dis = pg.display.set_mode((WIDTH, HIGHT))
pg.display.set_caption('Snake Game by Valtesar')

clock = pg.time.Clock()

SNAKE_BLOCK = 10  # Размер квадрата змейки в пикселях
SNAKE_SPEED = 15  # Скорость передвижения змейки

font_style = pg.font.SysFont("bahnschrift", 25)
score_font = pg.font.SysFont("comicsansms", 20)
result_score_font = pg.font.SysFont("comicsansms", 35, bold=True)

"""Инициализация спрайтов"""
snake_img = pg.image.load('images/snake_block.png')
food_img = pg.image.load('images/food_block.png')
background_img = pg.image.load('images/background.png')
game_over_img = pg.image.load('images/game_over.png')
game_over_record_img = pg.image.load('images/game_over_record.png')
main_menu_img = pg.image.load('images/main_menu.png')

event_log = ['']


def output_score(score, endgame, high_score):
    """Метод вывода набранных очков в игре"""

    """Принимает в себя аргументы:
     <score> - текущее колличество очков
     <endgame> - закончилась ли игра (True - Да, False - Нет)
     <high_score> - максимальное колличество очков игрока
     Отрисовывает на экране текущее значение очков и максимальное"""

    if not endgame:
        current_score = score_font.render('Score: ' + str(score), True, YELLOW)
        high_score = score_font.render('Record: ' + str(high_score), True, YELLOW)
        dis.blit(high_score, [490, 0])
        dis.blit(current_score, [0, 0])
    elif endgame:
        current_score = result_score_font.render(str(score), True, BLACK)
        high_score = result_score_font.render(str(high_score), True, BLACK)
        dis.blit(high_score, [310, 220])
        dis.blit(current_score, [310, 115])


def output_snake(snake_block, snake_list):
    """Метод отрисовки змейки на графическом экране.
       Получает на вход параметры:
            snake_block -> размер блока тела змейки в пикселях
            snake_list -> список координат всех имеющихся блоков тела змейки"""
    for x in snake_list:
        dis.blit(snake_img, [x[0], x[1], snake_block, snake_block])


def generate_food():
    """Метод генерации случайных координат <x1> <y1> для еды змейки"""

    x1_food = random.randrange(0, WIDTH, 10)
    y1_food = random.randrange(0, HIGHT - 20, 10)
    return x1_food, y1_food


def output_main_menu(high_score):
    """Метод вывода значений на экран главного меню"""
    high_score = result_score_font.render(str(high_score), True, BLACK)
    dis.blit(high_score, [205, 335])


def game_loop():
    """Основной игровой метод"""

    """По умолчанию параметры конца игры и закрытия окна в положении 0, а старта игры в 1"""
    game_over = False
    game_close = False
    game_start = True

    """Стартовое положение змейки на экране относительно координат <x1_snake> <y1_snake>"""
    x1_snake = WIDTH / 2
    y1_snake = HIGHT / 2

    """Изменяемые параметры <x1_snake> <y1_snake> в процессе игры"""
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

    """Пытаемся прочитать файл high_sore.txt, если файл отсутствует,
       то создаем файл с таким именем и записываем туда значение <0>"""
    if not path.exists('high_score.txt'):
        with open('high_score.txt', 'w') as w:
            w.write('0')
    with open('high_score.txt', 'r') as s:
        high_score = s.read()

    """Запускаем главный бесконечный цикл программы,
       который работает до тех пор пока пользователь не закроет окно игры"""
    while not game_close:
        """Запускаем вложенный бесконечный цикл программы,
           который работает до тех пор пока пользователь не нажмет ENTER или не закроет окно игры"""
        while game_start:
            dis.blit(main_menu_img, [0, 0])
            output_main_menu(high_score)
            pg.display.update()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    game_close = True
                    game_start = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        game_start = False

        """Запускаем вложенный бесконечный цикл программы,
           который работает до тех пор, пока пользователь не проиграет"""
        while game_over:
            dis.blit(game_over_img, [0, 0])
            output_score(length_of_snake - 1, True, high_score)
            pg.display.update()

            with open('high_score.txt', 'w') as scores:
                scores.write(str(high_score))

            """Отслеживаем игровые события. 
               Нажатие клавишы ESC ведет в выходу из игры.
               Нажатие клавишы Space запускает игру заново"""
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    game_close = True
                    game_over = False
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        game_over = False
                        game_close = True
                    if event.key == pg.K_SPACE:
                        game_loop()

        """Отслеживаем игровые события.
           Закрытие игрового окна закрывает приложение без ошибок.
           Нажатие клавишы влево - движение змейки влево  - X, Y
           Нажатие клавишы вправо - движение змейки вправо X +, Y 
           Нажатие клавишы вверх - движение змейки вверх X, Y + 
           Нажатие клавишы вниз - движение змейки вниз X, - Y"""

        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_close = True
            if event.type == pg.KEYDOWN:
                """Обработка события нажатия клавишы влево"""
                if event.key == pg.K_LEFT:
                    snake_direction = 'left'
                    if not event_log.__contains__('right'):
                        x1_change = -SNAKE_BLOCK
                        y1_change = 0
                        event_log.append(snake_direction)
                        event_log.pop(0)

                elif event.key == pg.K_RIGHT:
                    """Обработка события нажатия клавишы вправо"""
                    snake_direction = 'right'
                    if not event_log.__contains__('left'):
                        x1_change = SNAKE_BLOCK
                        y1_change = 0
                        event_log.append(snake_direction)
                        event_log.pop(0)

                elif event.key == pg.K_UP:
                    """Обработка события нажатия клавишы вверх"""
                    snake_direction = 'up'
                    if not event_log.__contains__('down'):
                        x1_change = 0
                        y1_change = -SNAKE_BLOCK
                        event_log.append(snake_direction)
                        event_log.pop(0)

                elif event.key == pg.K_DOWN:
                    """Обработка события нажатия клавишы вниз"""
                    snake_direction = 'down'
                    if not event_log.__contains__('up'):
                        x1_change = 0
                        y1_change = SNAKE_BLOCK
                        event_log.append(snake_direction)
                        event_log.pop(0)

        """Если змейка попытается выйти за границы игрового поля игра будет завершена проигрышем"""
        if x1_snake >= WIDTH or x1_snake < 0 or y1_snake >= HIGHT or y1_snake < 0:
            game_over = True

        """Получаем текущие координаты змейки с учетом изменний от пользователя (движения)"""
        x1_snake += x1_change
        y1_snake += y1_change
        dis.blit(background_img, [0, 0])

        """Отрисовываем еду на экране по случайно сгенерированным координатам"""
        dis.blit(food_img, [x1_food, y1_food])

        """"Создаем голову змейки и заносим её в основоной список тела змейки первым элементом.
           Если длина списка тела змейки больше чем сама змейка, то удаляем первый элемент (голову)"""
        snake_head = [x1_snake, y1_snake]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        """Проверяем каждый элемент в теле змейки, 
           и если его координаты равны координатам головы змейки то игра будет завершена проигрышем"""
        for body in snake_list[:-1]:
            if snake_head == body:
                game_over = True

        """Если змейка попадает головой на координаты еды, то генерируем новые координаты еды
           и увеличиваем длинну змейки на 1 еденицу"""
        if x1_snake == x1_food and y1_snake == y1_food:
            x1_food = generate_food()[0]
            y1_food = generate_food()[1]
            length_of_snake += 1

        """Если длина змейки больше чем рекорд, то новое значение рекорда = длине змейки"""
        if length_of_snake - 1 > int(high_score):
            high_score = length_of_snake - 1

        output_snake(SNAKE_BLOCK, snake_list)
        output_score(length_of_snake - 1, False, high_score)
        pg.display.update()
        clock.tick(SNAKE_SPEED)
    quit()
    pg.quit()


if __name__ == '__main__':
    game_loop()
