import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect


app = Flask(__name__)
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn



@app.route('/')
def base():
    return render_template('index.html')


@app.post('/login')
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username == 'admin' and password == 'password':
        return render_template('form.html', subtitle="Ingresa un producto", name="Username")
    else:
        return render_template('login.html', error="Credenciales inválidas")


@app.route('/form')
def form():
    return render_template('form.html', name="Usuario")


@app.route('/products')
def products():
    conn = get_db_connection()
    products = conn.execute('SELECT * FROM Product').fetchall()
    conn.close()
    return render_template('products.html', products=products)



if __name__ == '__main__':
    app.run(debug=True)
