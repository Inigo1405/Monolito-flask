import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect


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
    
    return render_template('index.html', products=products)


@app.post('/login')
def login():
    return render_template('login.html', subtitle="Login Page")


@app.post('/form')
def form():
    return render_template('form.html', name="Usuario")


@app.post('/products')
def products():
    return render_template('products.html', name="Usuario")



if __name__ == '__main__':
    app.run(debug=True)
