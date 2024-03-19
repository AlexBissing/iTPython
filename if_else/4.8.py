"""Даны два целых числа: D (день) и M (месяц), определяющие правильную дату невисокосного года. 
Вывести значения D и M для даты, следующей за указанной"""

def next_date(d, m):
    match (d, m):
        case (31, 12):
            return 1, 1
        case (31, _) if m in [1, 3, 5, 7, 8, 10, 12]:
            return 1, m + 1
        case (28, 2):
            return 1, m + 1
        case (_, _):
            return d + 1, m

day, month = int(input()), int(input())

print(f"Next day after {day}.{month}: {next_date(day, month)[0]}.{next_date(day, month)[1]}")

