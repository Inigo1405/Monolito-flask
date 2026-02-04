from flask import Flask, render_template, url_for, flash, redirect

@app.route('/form')
@login_required
def form():
    return redirect(url_for('productos_crear'))

# CREAR PRODUCTO
@app.get('/productos/nuevo')
@login_required
def productos_crear():
    return render_template('form.html', 
                            subtitulo="Nuevo Producto", 
                            nombre=session['username'], 
                            page='form',
                            producto=None,
                            form_data=None)

@app.route('/products')
@login_required
def products():
    return redirect(url_for('productos_listar'))

# LISTAR
@app.route('/productos')
@login_required
def productos_listar():
    conn = get_db_connection()
    productos = conn.execute('SELECT * FROM Product ORDER BY id DESC').fetchall()
    conn.close()
    return render_template('products.html', 
                           productos=productos,
                           nombre=session['username'], 
                           page='products')
