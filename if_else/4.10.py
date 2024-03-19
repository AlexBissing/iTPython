"""Дано целое число в диапазоне 100–999. 
Вывести строку-описание данного числа, например: 
256 — «двести пятьдесят шесть», 814 — «восемьсот четырнадцать»."""

def describe_number(n):
    units = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    tens = ["", "", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
    hundreds = ["", "сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]

    hundreds_digit = n // 100
    tens_digit = (n // 10) % 10
    units_digit = n % 10

    match (hundreds_digit, tens_digit, units_digit):
        case (0, 0, 0):
            return ""
        case (0, 0, units_digit):
            return units[units_digit]
        case (0, tens_digit, 0):
            return tens[tens_digit]
        case (0, 1, units_digit):
            return units[units_digit]
        case (hundreds_digit, 0, 0):
            return hundreds[hundreds_digit]
        case (hundreds_digit, tens_digit, 0):
            return f"{hundreds[hundreds_digit]} {tens[tens_digit]}"
        case (hundreds_digit, 1, units_digit):
            return f"{hundreds[hundreds_digit]} {units[units_digit]}"
        case (hundreds_digit, tens_digit, units_digit):
            return f"{hundreds[hundreds_digit]} {tens[tens_digit]} {units[units_digit]}"

# тест
number = int(input())
print(f"{number} — {describe_number(number)}")