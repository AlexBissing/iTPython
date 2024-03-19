# Подключаем библиотеку Pandas
import pandas

# Подключаем модуль pathlib и библиотерку Path модуля pathlib
import pathlib
from pathlib import Path

# Получаем строку, содержащую путь к рабочей директории
work_path = pathlib.Path.cwd()

# Сохраним путь к csv файлу в пременной data_path
data_path = Path(work_path, 'bikes.csv')

#Загружаем данные из csv файла в переменную data
data = pandas.read_csv(data_path)

total = data['Rachel1'].sum()

print(total)