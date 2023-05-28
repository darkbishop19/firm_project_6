import sqlite3

# Создаем подключение к базе данных
conn = sqlite3.connect('computer_store.db')
cursor = conn.cursor()


def delete_all_tables():
    cursor.execute('''DROP TABLE client_components''')
    cursor.execute('''DROP TABLE orders''')
    cursor.execute('''DROP TABLE order_components''')
    cursor.execute('''DROP TABLE component_prices''')
    cursor.execute('''DROP TABLE clients''')
    conn.commit()
    conn.close()

# delete_all_tables()

cursor.execute('''DROP TABLE orders''')

#Создаем таблицу для представления данных о комплектующих для клиентов
cursor.execute('''CREATE TABLE IF NOT EXISTS client_components
                (id INTEGER PRIMARY KEY,
                component_name TEXT,
                retail_price REAL)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS wholesaler_components
                  (id INTEGER PRIMARY KEY,
                  component_name TEXT,
                  wholesaler_price REAL,
                  wholesaler_info TEXT)''')

#заказы
cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY,
        client_id INTEGER,
        computer_id INTEGER,
        completion_date DATE,
        price REAL,
        paid INTEGER
    )
""")

#пользователи
cursor.execute("""
    CREATE TABLE IF NOT EXISTS clients (
        client_id INTEGER PRIMARY KEY,
        client_name TEXT
    )
""")

#пк
cursor.execute("""
    CREATE TABLE IF NOT EXISTS computers (
        id INTEGER PRIMARY KEY,
        component_ids TEXT,
        total_price REAL
    )
""")







conn.commit()
conn.close()
