from flask import Flask, render_template, request, session
import sqlite3

app = Flask(__name__)
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

app.secret_key = 'rbrt156we3f'

@app.route('/')
def base():
    return render_template('login.html', subtitulo="Iniciar Sesión")

@app.post('/login')
def login():
    session['username'] = request.form['username']
    session['password'] = request.form['password']
    if session['username'] == 'admin' and session['password'] == 'password':
        return render_template('form.html', subtitulo="Formulario de Producto", nombre=session['username'], page='form')
    else:
        return render_template('login.html', subtitulo="Iniciar Sesión")
        
@app.post('/logout')
def logout():
    session.clear()
    return render_template('login.html', subtitulo="Iniciar Sesión")

@app.get('/form')
def form():
    try:
        if session['username']:
            return render_template('form.html', subtitulo="Formulario de Producto", nombre=session['username'], page='form')
    except:
        return render_template('login.html', subtitulo="Iniciar Sesión")

@app.post('/form')
def form_post():
    product_name = request.form.get('product_name')
    conn = get_db_connection()
    conn.execute('INSERT INTO Product (name_prod) VALUES (?)', (product_name,))
    conn.commit()
    conn.close()
    return render_template('products.html', subtitulo="Listado de Productos", nombre=session['username'], page='products')

@app.get('/products')
def products():
    conn = get_db_connection()
    products = conn.execute('Select * from Product').fetchall()
    conn.commit()
    conn.close()
    return render_template('products.html',products=products, subtitulo="Listado de Productos", nombre=session['username'], page='products')

#Mandar rutas inventadas
@app.errorhandler(404)
def no_route(e):
    return render_template('login.html', subtitulo="Iniciar Sesión"), 404

if __name__ == '__main__':
    app.run(debug=True)
