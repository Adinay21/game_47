import sqlite3


db_name = '''test.db'''

def create_table(sql):
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(sql)
    except sqlite3.Error as error:
        print(error)

def insert_store(store):
    sql = '''INSERT INTO store (store_id, title) 
    VALUES (?, ?)'''
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, store)
    except sqlite3.Error as error:
        print(error)

def insert_products(products):
    sql = '''INSERT INTO products (title, categore_code, unit_price, stock_quantity, store_id) 
    VALUES (?, ?, ?, ?, ?)'''
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, products)
    except sqlite3.Error as error:
        print(error)





sql_to_create_categories_table = '''
CREATE TABLE categories (
    code VARCHAR(2) PRIMARY KEY,
    title VARCHAR(150) NOT NULL
)
'''


sql_to_create_products_table = '''
CREATE TABLE products (
    id INTEGER PRIMARY KEY autoincrement,
    title VARCHAR(250) NOT NULL,
    categore_code varchar(2) REFERENCES categories (code) not null,
    unit_price float NOT NULL,
    stock_quantity INTEGER not null,
    store_id INTEGER REFERENCES stores (store_id) not null
)
'''



# create_table(sql_to_create_categories_table)
# create_table(sql_to_create_products_table)

# insert_store((1, 'Asia'))
# insert_store((2, 'Globus'))
# insert_store((3, 'Spar'))

# insert_products(('Chocolate', 'FD', 10, 130, 1))
# insert_products(('T-Shirt', 'CL', 159, 37, 2))
# insert_products(('Iphone', 'EL', 1400, 20, 1))

import sqlite3


conn = sqlite3.connect('test.db')
cursor = conn.cursor()


def get_stores():
    cursor.execute("SELECT store_id, title FROM store")
    return cursor.fetchall()


def get_products_by_store(store_id):
    query = """
        SELECT p.title, c.title, p.unit_price, p.stock_quantity
        FROM products p
        JOIN categories c ON p.categore_code = c.code
        WHERE p.store_id = ?
    """
    cursor.execute(query, (store_id,))
    return cursor.fetchall()


def main():
    while True:
        print(
            "Вы можете отобразить список продуктов по выбранному id магазина из перечня магазинов ниже,"
            " для выхода из программы введите цифру 0:")


        stores = get_stores()
        for store in stores:
            print(f"{store[0]}. {store[1]}")


        user_input = input("Введите ID магазина: ")


        if user_input == '0':
            print("Выход из программы.")
            break


        if not user_input.isdigit():
            print("Введите корректное число.")
            continue

        store_id = int(user_input)


        products = get_products_by_store(store_id)
        if products:
            for product in products:
                print(f"Название продукта: {product[0]}")
                print(f"Категория: {product[1]}")
                print(f"Цена: {product[2]}")
                print(f"Количество на складе: {product[3]}")
                print("-----------")
        else:
            print("В данном магазине нет доступных продуктов.")


if __name__ == "__main__":
    main()


conn.close()