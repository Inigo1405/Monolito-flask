import sqlite3
from flask import Flask, render_template# from db import db


app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn



@app.route('/')
def base():
    conn = get_db_connection()
    products = conn.execute('SELECT * FROM Product').fetchall()
    conn.close()
    print(products)
    
    return render_template('index.html', products=products)

@app.post('/login')
def login():
    return render_template('login.html')

@app.post('/crud')
def home():
    return render_template('form.html')


if __name__ == '__name__':
    app.run(debug = True)
