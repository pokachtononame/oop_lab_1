#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class ModelWindow:
    screenX = 1600
    screenY = 900
    ALLOWED_COLORS = ['Красный', 'Зеленый', 'Синий', 'Белый', 'Черный']
    def __init__(self, title, color='Белый', startx=0, starty=0, width=100, height=100, visible=True, borderless=False):
        if isinstance(title, str):
            self.title = title
        else:
            raise ValueError('Заголовок должен быть строкой')

        if isinstance(startx, int) and isinstance(starty, int):
            self.x = startx
            self.y = starty
        else:
            raise ValueError('Координаты должны быть целыми числами')

        if isinstance(width, int) and isinstance(height, int) and width > 0 and height > 0:
            self.width = width
            self.height = height
        else:
            raise ValueError('Размеры должны быть целыми положительными числами')

        if color in self.ALLOWED_COLORS:
            self.color = color
        else:
            raise ValueError(f'Значение не в списке цветов')

        self.visible = bool(visible)
        self.borderless = bool(borderless)


    def change_color(self, new_color):
        if new_color not in self.ALLOWED_COLORS:
            raise ValueError('Значение не в списке цветов')
        self.color = new_color


    def display(self):
        print(f'\nСостояние окна {self.title}')
        print(f'Координаты (X, Y): ({self.x}, {self.y})')
        print(f'Размеры (Ш x В): {self.width} x {self.height}')
        print(f'Цвет окна: {self.color}')
        print(f'Видимость: {'Видимое' if self.visible else 'Невидимое'}')
        print(f'Рамка: {'Без рамки' if self.borderless else 'С рамкой'}')


    def read(self):
        self.title = input('Введите заголовок окна: ')

        while True:
            try:
                self.x = int(input('Введите координату X: '))
                self.y = int(input('Введите координату Y: '))
                break
            except ValueError:
                print('Координаты должны быть целыми числами. Попробуйте снова.')

        while True:
            try:
                w = int(input('Введите ширину окна: '))
                h = int(input('Введите высоту окна: '))
                if w <= 0 or h <= 0:
                    print('Ширина и высота должны быть больше нуля')
                    continue
                self.width = w
                self.height = h
                break
            except ValueError:
                print('Размеры должны быть целыми числами. Попробуйте снова.')

        while True:
            c = input(f'Введите цвет {self.ALLOWED_COLORS}: ').strip()
            if c in self.ALLOWED_COLORS:
                self.color = c
                break
            print('Такого цвета нет в списке. Попробуйте снова.')

        vis = input('Окно видимое? (да/нет): ').lower().strip()
        self.visible = (vis == 'да')

        bord = input('Окно без рамки? (да/нет): ').lower().strip()
        self.borderless = (bord == 'да')


    def shift(self, x, y):
        if isinstance(x, int) and isinstance(y, int):
            if self.x + x < 0 or self.x + x + self.width > self.screenX:
                print('Выход за границы экрана по X')
                return

            if self.y + y < 0 or self.y + y + self.height > self.screenY:
                print('Выход за границы экрана по Y')
                return

            self.x = self.x + x
            self.y = self.y + y
        else:
            raise ValueError('Смещения по координатам должны быть целыми числами')

    def resize(self, width, height):
        if isinstance(width, int) and isinstance(height, int):

            if width <= 0 or height <= 0:
                print('Размеры должны быть больше нуля')
                return

            if self.x + width > self.screenX:
                print('Выход за границы экрана по X')
                return

            if self.y + height > self.screenY:
                print('Выход за границы экрана по Y')
                return

            self.width = width
            self.height = height
        else:
            raise ValueError('Размеры окон должны быть целыми числами')

    def set_visible(self, status):
        self.visible = bool(status)

    def set_borderless(self, status):
        self.borderless = bool(status)

    def is_visible(self):
        return self.visible

    def is_borderless(self):
        return self.borderless


if __name__ == "__main__":
    my_window = ModelWindow(title="Telegram", color="Синий", startx=100, starty=100, width=400, height=300)
    my_window.display()

    my_window.shift(200, 50)
    my_window.shift(1000, 0)
    my_window.display()

    my_window.resize(800, 600)
    my_window.resize(800, 800)
    my_window.display()

    print(f"Сейчас окно видимое? {my_window.is_visible()}")
    my_window.set_visible(False)
    my_window.set_borderless(True)
    my_window.change_color("Красный")
    my_window.display()

    my_window.read()
    my_window.display()