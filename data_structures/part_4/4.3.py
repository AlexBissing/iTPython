lst = ['a', 's', '1', 'a', '32', '23']

lst1 = []
lst2 = []

for i in range(len(lst)):
    if lst[i].isdigit():
        lst1.append(lst[i])
    else:
        lst2.append(lst[i])

print('Цифры:', lst1)
print('Буквы:', lst2)
