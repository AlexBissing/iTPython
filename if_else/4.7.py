"""Дан номер месяца — целое число в диапазоне 1–12 (1 — январь, 2 — февраль и т. д.). 
Определить количество дней в этом месяце для невисокосного года."""

def days_in_month(month):
    match month:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            return 31
        case 4 | 6 | 9 | 11:
            return 30
        case 2:
            return 28
        case _:
            return "Некорректный номер месяца"

# тест
month = int(input())
print(f"Количество дней в месяце {month}: {days_in_month(month)}")