""" Написать программу на Python для решения квадратного уравнения ax^2 + bx + c = 0.
Если дискриминант отрицателен, программа должна выдать ошибку и предложить пользова
телю попробовать еще раз с другими коэффициентами. При выполнении скрипта в лог должна 
записываться информация о успехе или неудаче операции."""

import math
import logging


def solve_quadratic(a, b, c):
    # set the logging level
    logging.basicConfig(level=logging.INFO, filename="solve_quadratic.log", filemode="w",
                        format="%(asctime)s - %(levelname)s - %(message)s")

    # calculate the discriminant
    discriminant = b ** 2 - 4 * a * c

    if discriminant < 0:
        logging.exception("Discriminant is negative") 
        print("Error: The discriminant is less than zero. Enter other coefficients.")
    return None

    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print(f"x1 = {round(x1, 2)}, x2 = {round(x2, 2)}")
    elif discriminant == 0:
        x = -b / (2 * a)
        print(f"x = {round(x, 2)}")
    else:
        print("We have no roots")

a, b, c = float(input("a = ")), float(input("b = ")), float(input("c = "))

solve_quadratic(a, b, c)
