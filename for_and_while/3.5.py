"""Напишите программу для вывода таблицы умножения от 0 до 9. 
Используйте вложенный цикл for, print и range"""

for i in range(0, 9):
    for j in range(0, 9):
        print(f'{i} * {j + 1} = {i * (j + 1)}')