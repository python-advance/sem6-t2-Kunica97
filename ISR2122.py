# Задание ИСР 2
#
# 2.1. Разработать функцию, возвращающую элементы
# ряда Фибоначчи по данному максимальному значению.
# 2.2. Создание программы, возвращающей список
# чисел Фибоначчи с помощью итератора.

import itertools

def fib():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

n = int(input())
f = []

for i in itertools.takewhile(lambda x: x < n, fib()):
    print(i)
    f.append(i)

print(f)