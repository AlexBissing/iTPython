"""Найти факториалы чисел от 1 до 5 (включительно)."""

res = 1
for i in range(1, 6):
    res *= i
    print(res)