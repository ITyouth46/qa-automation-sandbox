import sqlite3

# Создаем файл базы данных (или подключаемся к нему, если он уже есть)
conn = sqlite3.connect('shop.db')
cursor = conn.cursor()

# Пишем SQL-запрос для создания таблицы пользователей
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        role TEXT NOT NULL
    )
''')

# Очищаем таблицу перед запуском и добавляем нашего тестового пользователя
cursor.execute('DELETE FROM users')
cursor.execute('INSERT INTO users (username, role) VALUES ("standard_user", "customer")')

# Сохранями изменения и закрываем базу
conn.commit()
conn.close()

print("База данных shop.db успешно создана, тестовый пользователь добавлен!")