"""Реализуйте программу калькулятор. 
На вход подается три значения: первое число, второе число и операция( *, /, + или -) . 
На выходе должны получить число, после выполнения операции."""

def calculator(a, b, operation):
    match operation:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b
        case '/':
            if b == 0:
                return "Ошибка: деление на ноль"
            else:
                return a / b
        case _:
            return "Ошибка: неизвестная операция"

a, b = int(input()), int(input())
operation = '*'

print(f"{a} {operation} {b} = {calculator(a, b, operation)}")
