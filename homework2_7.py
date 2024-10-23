import sqlite3


db_name = '''hw.db'''

def create_table(sql):
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(sql)
    except sqlite3.Error as error:
        print(error)

def insert_products(products):
    sql = '''INSERT INTO products (product_title, price, quantity) 
    VALUES (?, ?, ?)'''
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, products)
    except sqlite3.Error as error:
        print(error)


def change_price_products(products):
    sql = '''UPDATE products SET price = ? WHERE id = ?'''
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, products)
    except sqlite3.Error as error:
        print(error)

def change_quanity_products(products):
    sql = '''UPDATE products SET quanity = ? WHERE id = ?'''
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, products)
    except sqlite3.Error as error:
        print(error)

def delete_products(id):
    sql = '''DELETE FROM products WHERE id = ?'''
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, (id,))
    except sqlite3.Error as error:
        print(error)

def select_all_products():
    sql = '''SELECT * FROM products'''
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as error:
        print(error)

def select_all_products_by_price_and_quantity(price_limit, quantity_limit):
    sql = '''SELECT * FROM products WHERE price < ? AND quantity > ?'''
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, (price_limit, quantity_limit))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as error:
        print(error)

def find_products(product_title):
    sql = '''SELECT * FROM products WHERE product_title LIKE ?'''
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, (product_title,))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as error:
        print(error)


sql_to_create_product_table = '''
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL,
    price FLOAT(10,2) NOT NULL DEFAULT 0,
    quanity INTEGER NOT NULL DEFAULT 0
)
'''



# create_table(sql_to_create_product_table)

# insert_products(('Жидкое мыло', 149, 5))
# insert_products(('Крем для рук', 258.40, 17))
# insert_products(('Порошок для стирки', 1679.90, 10))
# insert_products(('Детское мыло', 78, 24))
# insert_products(('Шампунь для волос', 570.60, 21))
# insert_products(('Средство для мытья посуды', 120.80, 35))
# insert_products(('Крем для лица', 1400, 19))
# insert_products(('Губка для посуды', 25.40, 55))
# insert_products(('Черный чай в пакетиках', 340.60, 50))
# insert_products(('Зеленый чай', 320.60, 37))
# insert_products(('Песочное печенье', 250.70, 46))
# insert_products(('Гель для душа', 430.40, 36))
# insert_products(('Конфеты Twix', 460, 52))
# insert_products(('Картофель', 25.20, 60))
# insert_products(('Свекла', 35.50, 70))

# change_price_products((270, 1))
# change_quanity_products((23, 8))

# delete_products(6)

# select_all_products()

# select_all_products_by_price_and_quantity(100, 5)

find_products('%мыло%')