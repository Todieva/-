import sqlite3
from sqlite3 import connect

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('Рассеянный склероз_ДСМ.xlsx')
cursor = connection.cursor()

# Создаем таблицу Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER
)
''')

# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()
