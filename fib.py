import itertools

def isr (n):
    '''
    2.1. Разработать функцию, возвращающую элементы
    ряда Фибоначчи по данному максимальному значению.
    2.2. Создание программы, возвращающей список
    чисел Фибоначчи с помощью итератора.
    '''
    def fib_isr():
        a, b = 1, 1
        while True:
            yield a
            a, b = b, a + b

    f = []

    for i in itertools.takewhile(lambda x: x < n, fib_isr()):
        f.append(i)
    return f

def vsr (n):
    '''
    Задание ВСР 2
    2.1. Разработать функцию, возвращающую список чисел ряда Фибоначчи
    с использованием бесконечных итераторов (модуль itertools).
    '''
    def fib_vsr(n):
        a, b = 1, 1
        f = [a]
        while b < n:
            f.append(b)
            a, b = b, a + b
        return f

    f = []

    for i in itertools.takewhile(lambda x: x < n, fib_vsr(n)):
        f.append(i)
    return f

print(isr(40))
print(vsr(60))

if __name__ == "__main__":
    test = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    isr_list = isr(7)
    vsr_list = vsr(4)
    for i in range(0, len(isr_list) - 1):
        assert(isr_list[i] == test[i])
    for i in range(0, len(vsr_list) - 1):
        assert(vsr_list[i] == test[i])
