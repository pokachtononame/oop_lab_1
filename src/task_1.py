#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Pair:
    def __init__(self, a=0.0, b=0.0):
        if isinstance(a, (float, int)) and isinstance(b, (float, int)):
            self.first = float(a)
            self.second = float(b)
        else:
            raise ValueError('Некорректный тип аргументов')

    def read(self, prompt=None):
        if not isinstance(prompt, str):
            raise ValueError('Приглашение должно быть строкой')
        if prompt is None:
            text = input()
        else:
            text = input(prompt)
        parts = text.split()
        if len(parts) != 2:
            raise ValueError('Ожидается два значения')
        self.first = float(parts[0])
        self.second = float(parts[1])

    def display(self):
        print(f'First: {self.first}, Second: {self.second}')

    def power(self):
        return pow(self.first, self.second)


def make_pair(first, second):
    try:
        return Pair(first, second)
    except ValueError as error:
        print(f'Ошибка создания пары: {error}')
        return None


if __name__ == "__main__":
    p1 = Pair(30, 2.5)
    p2 = make_pair(20.5, 3)
    p3 = Pair()
    p3.read('Введите пару: ')
    p1.display()
    p2.display()
    p3.display()
    print(f'power() для первой переменной: {p1.power():.4f}')
    print(f'power() для второй переменной: {p2.power():.4f}')
    print(f'power() для третьей переменной: {p3.power():.4f}')
    p4 = Pair(0, 0)
    print(f'power() для нулевой степени: {p4.power():.4f}')
