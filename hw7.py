import sqlite3


# Создание базы данных и подключение к ней
def create_database():
    conn = sqlite3.connect('hw.db')
    c = conn.cursor()

    # Создание таблицы products
    c.execute('''CREATE TABLE IF NOT EXISTS products
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 product_title TEXT NOT NULL,
                 price REAL NOT NULL DEFAULT 0.0,
                 quantity INTEGER NOT NULL DEFAULT 0)''')

    conn.commit()
    conn.close()


# Добавление товара в таблицу
def add_product(product_title, price, quantity):
    conn = sqlite3.connect('hw.db')
    c = conn.cursor()

    c.execute('''INSERT INTO products (product_title, price, quantity)
                 VALUES (?, ?, ?)''', (product_title, price, quantity))

    conn.commit()
    conn.close()


# Функция для добавления 15 различных товаров
def add_multiple_products():
    products = [
        ("Product 1", 10.99, 20),
        ("Product 2", 5.49, 15),
        ("Product 3", 8.75, 30),
        ("Product 4", 15.25, 10),
        ("Product 5", 7.99, 25),
        ("Product 6", 12.50, 12),
        ("Product 7", 9.99, 18),
        ("Product 8", 6.25, 22),
        ("Product 9", 11.75, 8),
        ("Product 10", 14.99, 14),
        ("Product 11", 3.50, 30),
        ("Product 12", 16.25, 6),
        ("Product 13", 9.99, 20),
        ("Product 14", 4.75, 15),
        ("Product 15", 17.50, 10)
    ]

    for product in products:
        add_product(*product)


# Функция для изменения количества товара по id
def update_quantity(product_id, new_quantity):
    conn = sqlite3.connect('hw.db')
    c = conn.cursor()

    c.execute('''UPDATE products
                 SET quantity = ?
                 WHERE id = ?''', (new_quantity, product_id))

    conn.commit()
    conn.close()


# Функция для изменения цены товара по id
def update_price(product_id, new_price):
    conn = sqlite3.connect('hw.db')
    c = conn.cursor()

    c.execute('''UPDATE products
                 SET price = ?
                 WHERE id = ?''', (new_price, product_id))

    conn.commit()
    conn.close()


# Функция для удаления товара по id
def delete_product(product_id):
    conn = sqlite3.connect('hw.db')
    c = conn.cursor()

    c.execute('''DELETE FROM products
                 WHERE id = ?''', (product_id,))

    conn.commit()
    conn.close()


# Функция для выборки всех товаров из БД и их печати
def print_all_products():
    conn = sqlite3.connect('hw.db')
    c = conn.cursor()

    c.execute('''SELECT * FROM products''')
    products = c.fetchall()

    for product in products:
        print(product)

    conn.close()


# Функция для выборки товаров, дешевле лимита и с количеством больше лимита
def print_products_below_limit(price_limit, quantity_limit):
    conn = sqlite3.connect('hw.db')
    c = conn.cursor()

    c.execute('''SELECT * FROM products
                 WHERE price < ? AND quantity > ?''', (price_limit, quantity_limit))
    products = c.fetchall()

    for product in products:
        print(product)

    conn.close()


# Функция для поиска товаров по названию
def search_products_by_title(title):
    conn = sqlite3.connect('hw.db')
    c = conn.cursor()

    c.execute('''SELECT * FROM products
                 WHERE product_title LIKE ?''', ('%' + title + '%',))
    products = c.fetchall()

    for product in products:
        print(product)

    conn.close()


# Тестирование всех функций
def test_functions():
    create_database()
    add_multiple_products()

    print("All products:")
    print_all_products()

    print("\nProducts below limit:")
    print_products_below_limit(100, 5)

    print("\nSearch products by title:")
    search_products_by_title("Product")

    update_quantity(1, 25)
    update_price(2, 6.99)
    delete_product(3)

    print("\nAll products after updates and deletion:")
    print_all_products()


# Запуск тестов
test_functions()
