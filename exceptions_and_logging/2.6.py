""" Написать программу для генерации случайных чисел в заданном диапазоне. Если пользователь
ввел недопустимые границы диапазона (например, меньше нуля), программа должна вывести ошибку
и попросить ввести диапазон заново. Информация об ошибках должна быть записана в лог."""

import logging
import random

# set logging
logging.basicConfig(filename='random_numbers.log', level=logging.ERROR, filemode='w',
                    format='%(asctime)s - %(levelname)s - %(message)s')


def random_numbers(min, max):
    if min < 0 or max < 0:
        logging.error("The 'number' is not in the range")
        return None

    if min > max:
        logging.error("Error:The minimum value cannot be greater than the maximum value")
        return None

    # Random number generation
    random_number = random.randint(min, max)
    return random_number


while True:
    try:
        min = int(input())
        max = int(input())
        random_number = random_numbers(min, max)
        if random_number is not None:
            print(f"Random number in range from {min} to {max}: {random_number}")
            break
    except ValueError:
        print("Error: enter an integer")