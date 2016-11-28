__author__ = "Ассонов Максим"

# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список, элементами которого будут
# квадратные корни элементов исходного списка, но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

import math;


def prepare_list(lst):
    res = []
    for i in lst:
        if i >= 0:
            j = math.sqrt(i)
            if int(j) == j: res.append(int(j))
    return res


# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

def prepare_date(date_):
    def make_dates():
        res = ("первое, второе, третье, четвертое, пятое, шестое, седьмое, восьмое, девятое, десятое, " + \
               "одиннадцатое, двенадцатое, тринадцатое, четырнадцатое, пятнадцатое, шестнадцатое, семнадцатое, " + \
               "восемнадцатое, девятнадцатое, двадцатое").split(", ")
        for i in range(9):
            res.append("двадцать " + res[i])
        res.append("тридцатое")
        for i in range(3):
            res.append("тридцать " + res[i])
        return res

    MONTHS = "января, февраля, марта, апреля, мая, июня, июля, августа, сентября, октября, ноября, декабря".split(", ")
    DATES = make_dates()
    d = date_.split(".")
    return "{} {} {} года".format(DATES[int(d[0]) - 1], MONTHS[int(d[1]) - 1], d[2])


# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами в диапазоне от -100 до 100
# В списке должно быть n - элементов
# Подсказка: для получения случайного числа изпользуйте функцию randint() модуля random

import random


def get_random_list(n):
    return [random.randint(-100, 100) for i in range(n)]


# Задача-4: Дан список, заполненный произвольными целыми числами
# Получите новый список, элементами которого будут только уникальные элементы исходного
# Например, lst = [1,2,4,5,6,2,5,2], нужно получить lst2 = [1,4,6]

def get_unique(lst):
    res=[]
    counts = {}
    keys = []
    for i in lst:
        if i in keys:
            counts[i] += 1
        else:
            keys.append(i)
            counts[i] = 1
    for i in counts:
        if counts[i] == 1: res.append(i)
    return res


# tests

def test(got, expected):
    prefix = "OK" if got == expected else "X"
    print("{0} - Получено: {1} | Ожидалось: {2}".format(prefix, repr(got), repr(expected)))


print("Задача 1")
test(prepare_list([2, -5, 8, 9, -25, 25, 4]), [3, 5, 2])

print("\nЗадача 2")
test(prepare_date("02.11.2013"), "второе ноября 2013 года")
test(prepare_date("32.07.2018"), "тридцать второе июля 2018 года")

print("\nЗадача 3")
print(get_random_list(10))

print("\nЗадача 4")
test(get_unique([1, 2, 4, 5, 6, 2, 5, 2]), [1, 4, 6])
test(get_unique([1, 2, 4, 5, 6, 2, 5, 2, 8, 10, 8]), [1, 4, 6, 10])
