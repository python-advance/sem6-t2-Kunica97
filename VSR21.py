# Задание ВСР 2
#
# 2.1. Разработать функцию, возвращающую список чисел ряда Фибоначчи
# с использованием бесконечных итераторов (модуль itertools).

import itertools

def fib(n):
    a, b = 1, 1
    f = [a]
    while b < n:
        f.append(b)
        a, b = b, a + b
    return f
n = int(input())


for i in itertools.takewhile(lambda x: x < n, fib(n)):
    print(i)