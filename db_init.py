import sqlite3

connection = sqlite3.connect('database.db')

with open('./schema.sql') as f:
    connection.executescript(f.read())
    
cur = connection.cursor()


cur.execute("INSERT INTO Product (name_prod, price, stock) VALUES ('Libro', 10.99, 2)")


connection.commit()
connection.close()