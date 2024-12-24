import sqlite3
from sqlite3 import connect
from excel import reader

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('Рассеянный склероз_ДСМ.xlsx')
cursor = connection.cursor()

# Создаем таблицу Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
Тип товара TEXT,
Полное наименование TEXT,
МНН TEXT,
Лекарственная форма TEXT,
Фирма-производитель TEXT,
Корпорация TEXT,
Фармакотерапевтическая группа TEXT,
Год INTEGER,
Месяц INTEGER,
Объем (цена розн.-уп.розн.), рубли INTEGER,
Объем (розница), упак. INTEGER,
Объем (цена опт.-уп.розн.), рубли INTEGER,
)
''')

# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()
