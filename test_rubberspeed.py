import math

l = float(input("Введите длину резинки в мм: "))
t = float(input("Введите время измерения в секундах: "))
w = float(input("Введите кол-во оборотов: "))

l1 = 2 * math.pi * l
lw = l1 * w
s = lw / t

sk = s / 1000000 * 3600

print("Скорость крайней точки резинки составляет {} мм/сек или {} км/ч".format(s,sk))