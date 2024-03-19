file = open("/home/ajax/Documents/file.txt", mode='r+', encoding='utf-8')
file.write("Я опять поменял текст и понял наконец как все работает")

file.close()

file = open("/home/ajax/Documents/file.txt", mode='r+', encoding='utf-8')
print(file.read())
