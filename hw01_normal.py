# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.

num = 3384456779
# num=int(input("Input integer: "))
num_str = str(num)
num_max = int(num_str[0])
for i in range(len(num_str) - 1):
    num_tmp = int(num_str[i + 1])
    if num_tmp > num_max:
        num_max = num_tmp
print(num_max)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.

a = input("Input a: ")
b = input("Input b: ")
a, b = b, a
print("a = ", a, ", b = ", b)
print()

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида ax2 + bx + c = 0.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math
# import math
# math.sqrt(4) - вычисляет корень числа 4

import math

print("Вычисление корней квадратного уравнения вида ax2 + bx + c = 0.")
a = float(input("Введите a: "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))
if a == 0:
    if b == 0:
        print("Введены нулевые коэффициенты a и b.")
    else:
        x = -c / b;
        print("x = ", x)
else:
    d = pow(b, 2) - 4 * a * c
    if d == 0:
        x = -b / (2 * a)
        print("x = ", x)
    elif d > 0:
        d = math.sqrt(d)
        x1 = (-b - d) / (2 * a)
        x2 = (-b + d) / (2 * a)
        print("x1 = ", x1, ", x2 = ", x2)
    else:
        print("Корней на множестве действительных чисел нет.")
