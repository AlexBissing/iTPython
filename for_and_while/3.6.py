"""Создайте список с разными значениями, пройдитесь по нему в цикле и выведите на экран. 
(Сделайте тоже самое со словарем и выведите ключ и значение)"""

my_list = [1, 2, 3, 5, 'a', 'b', 'c']

for i in my_list:
    print(i, end=' ')
    
print()

my_dict = {'name' : 'Alex', 'age': '43', 'email': 'avbissing@gmail.com', 'city': 'Moscow'}

for key, value in my_dict.items():
    print(key, value)