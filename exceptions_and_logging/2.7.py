""" Написать программу для нахождения среднего арифметического числа. Если при вводе списка 
чисел была допущена ошибка (например, был передан не список, а строка), программ должна корректно
обработать эту ошибку и выдать соответствующее сообщение. Информация об ошибка должна быть записана в лог."""

import logging

logging.basicConfig(filename='average_number.log', level=logging.ERROR, filemode='w',
                    format='%(asctime)s - %(levelname)s - %(message)s')

def average_number(numbers = []):
    for i in numbers:
        if not isinstance(i, int):
            logging.error("Error: The user entered a string enstead of a number")
            print("Error: it's not a number, it's a string")
            return None
    return sum(numbers) / len(numbers)

print(average_number([1, 2, 3, 4, 5, 6, 7, 8, 'a', 'b']))        