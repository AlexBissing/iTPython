"""Вывести все числа от 1 до 100, которые делятся на 3 без остатка"""

for i in range(1, 100):
    if i % 3 == 0:
        print(i, end=' ')