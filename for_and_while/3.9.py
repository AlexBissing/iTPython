"""Найти все простые числа от 2 до 50"""

def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

prime_numbers = [num for num in range(2, 50) if is_prime(num)]
print(prime_numbers)
