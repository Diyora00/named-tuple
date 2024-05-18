import requests
import psycopg2
from collections import namedtuple
import colorama

conn = psycopg2.connect(dbname="n47",
                        user="postgres",
                        password="123",
                        host="localhost",
                        port=5432)
cur = conn.cursor()


def table_products():
    create_table_query = """CREATE TABLE IF NOT EXISTS products (
                            id SERIAL PRIMARY KEY,
                            title VARCHAR(255),
                            description TEXT,
                            price INT,
                            discountPercentage FLOAT,
                            rating FLOAT,
                            stock INT,
                            brand VARCHAR(255),
                            category VARCHAR(255),
                            thumbnail TEXT,
                            images TEXT);"""
    cur.execute(create_table_query)
    conn.commit()


def in_data_table():
    url = 'https://dummyjson.com/products/'
    r = requests.get(url)
    in_data = """INSERT INTO products (title, description, price, discountPercentage,
                 rating, stock, brand,category, thumbnail, images)
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    for p in r.json()["products"]:
        cur.execute(in_data, (p["title"], p["description"], p["price"], p["discountPercentage"],
                              p["rating"], p["stock"], p["brand"], p["category"], p["thumbnail"], p["images"]))
        conn.commit()


# named tuple

# Product = namedtuple('Product', 'id title color category image')
Product = namedtuple('Product', ['id', 'title', 'color', 'category', 'image'])
print(issubclass(Product, tuple))  # True
print(Product._fields)  # ('id', 'title', 'color', 'category', 'image')
print(Product)  # <class '__main__.Product'>
ball = Product(1, 'ball', 'black', 'toys', 'https//:ball')
print(ball)  # Product(id=1, title='ball', color='black', category='toys', image='https//:ball')
# vase = Product(**{'id': 2, 'title': 'vase', 'color': 'pink', 'category': 'home decor', 'image': 'https//:vase'})
d = {'id': 2, 'title': 'vase', 'color': 'pink', 'category': 'home decor', 'image': 'https//:vase'}
vase = Product(**d)
print(vase)
print(vase.id)
print(vase.color)
print(vase.category)
Person = namedtuple('Person', ['name', 'age', 'gender'], defaults=['John', 18])
sally = Person('Sally', '25', 'Male')
print(sally)
