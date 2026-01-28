from flask import Flask, render_template, request, session
import sqlite3

app = Flask(__name__)
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def base():
    return render_template('login.html', subtitulo="Iniciar Sesión")

@app.post('/login')
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username == 'admin' and password == 'password':
        return render_template('form.html', subtitulo="Ingresa un producto", name="Username")
    else:
        return render_template('login.html', error="Credenciales inválidas")

@app.get('/form')
def form():
    return render_template('form.html', name="Usuario")

@app.post('/form')
def form_post():
    product_name = request.form.get('product_name')
    conn = get_db_connection()
    conn.execute('INSERT INTO Product (name_prod) VALUES (?)', (product_name,))
    conn.commit()
    conn.close()
    return render_template('products.html', name="Usuario")

@app.get('/products')
def products():

    conn = get_db_connection()
    products = conn.execute('Select * from Product')
    conn.commit()
    conn.close()
    return render_template('products.html',products=products, subtitulo="Listado de Productos" )

if __name__ == '__main__':
    app.run(debug=True)
