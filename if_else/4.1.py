"""Даны три целых числа. Найти количество положительных чисел в исходном наборе."""

positive = 0


for _ in range(3):
    n = int(input())
    if n > 0:
        positive += 1
print(f"Количество положительных чисел = {positive}")