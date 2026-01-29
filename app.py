import sqlite3
from functools import wraps
from flask import Flask, render_template, request, session, url_for, flash, redirect


app = Flask(__name__)
app.secret_key = 'rbrt156we3f'

# Credenciales de login chafas
USUARIO = 'admin'
PASSWORD = 'password'


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


# Decorador para proteger rutas
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            flash('Debes iniciar sesión para acceder a esta página.', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


# =Login y Logout

@app.route('/')
def base():
    if 'username' in session:
        return redirect(url_for('productos_listar'))
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        
        if username == USUARIO and password == PASSWORD:
            session['username'] = username
            flash('Inicio de sesión exitoso.', 'success')
            return redirect(url_for('productos_listar'))
        else:
            flash('Usuario o contraseña incorrectos.', 'danger')
            return render_template('login.html', subtitulo="Iniciar Sesión")
    
    if 'username' in session:
        return redirect(url_for('productos_listar'))
    
    return render_template('login.html', subtitulo="Iniciar Sesión")


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.clear()
    flash('Sesión cerrada correctamente.', 'info')
    return redirect(url_for('login'))


# Crud de Productos

# LISTAR - /productos
@app.route('/productos')
@login_required
def productos_listar():
    conn = get_db_connection()
    productos = conn.execute('SELECT * FROM Product ORDER BY id DESC').fetchall()
    conn.close()
    return render_template('products.html', 
                           productos=productos, 
                           subtitulo="Listado de Productos", 
                           nombre=session['username'], 
                           page='products')


# CREAR - /productos/nuevo
@app.route('/productos/nuevo', methods=['GET', 'POST'])
@login_required
def productos_crear():
    if request.method == 'POST':
        nombre = request.form.get('nombre', '').strip()
        precio = request.form.get('precio', '')
        stock = request.form.get('stock', '')
        activo = request.form.get('activo') == 'on'
        
        # Validaciones
        errores = []
        
        if not nombre:
            errores.append('El nombre es requerido.')
        
        try:
            precio = float(precio)
            if precio < 0:
                errores.append('El precio debe ser mayor o igual a 0.')
        except ValueError:
            errores.append('El precio debe ser un número válido.')
        
        try:
            stock = int(stock)
            if stock < 0:
                errores.append('El stock debe ser mayor o igual a 0.')
        except ValueError:
            errores.append('El stock debe ser un número entero válido.')
        
        if errores:
            for error in errores:
                flash(error, 'danger')
            return render_template('form.html', 
                                   subtitulo="Nuevo Producto", 
                                   nombre=session['username'], 
                                   page='form',
                                   producto=None,
                                   form_data={'nombre': request.form.get('nombre', ''),
                                              'precio': request.form.get('precio', ''),
                                              'stock': request.form.get('stock', ''),
                                              'activo': activo})
        
        # Insertar en base de datos
        conn = get_db_connection()
        conn.execute(
            'INSERT INTO Product (name_prod, price, stock, active) VALUES (?, ?, ?, ?)',
            (nombre, precio, stock, 1 if activo else 0)
        )
        conn.commit()
        conn.close()
        
        flash('Producto creado exitosamente.', 'success')
        return redirect(url_for('productos_listar'))
    
    return render_template('form.html', 
                           subtitulo="Nuevo Producto", 
                           nombre=session['username'], 
                           page='form',
                           producto=None,
                           form_data=None)


# EDITAR - /productos/<id>/editar
@app.route('/productos/<int:id>/editar', methods=['GET', 'POST'])
@login_required
def productos_editar(id):
    conn = get_db_connection()
    producto = conn.execute('SELECT * FROM Product WHERE id = ?', (id,)).fetchone()
    
    if producto is None:
        conn.close()
        flash('Producto no encontrado.', 'danger')
        return redirect(url_for('productos_listar'))
    
    if request.method == 'POST':
        nombre = request.form.get('nombre', '').strip()
        precio = request.form.get('precio', '')
        stock = request.form.get('stock', '')
        activo = request.form.get('activo') == 'on'
        
        # Validaciones
        errores = []
        
        if not nombre:
            errores.append('El nombre es requerido.')
        
        try:
            precio = float(precio)
            if precio < 0:
                errores.append('El precio debe ser mayor o igual a 0.')
        except ValueError:
            errores.append('El precio debe ser un número válido.')
        
        try:
            stock = int(stock)
            if stock < 0:
                errores.append('El stock debe ser mayor o igual a 0.')
        except ValueError:
            errores.append('El stock debe ser un número entero válido.')
        
        if errores:
            for error in errores:
                flash(error, 'danger')
            conn.close()
            return render_template('form.html', 
                                   subtitulo="Editar Producto", 
                                   nombre=session['username'], 
                                   page='form',
                                   producto=producto,
                                   form_data={'nombre': request.form.get('nombre', ''),
                                              'precio': request.form.get('precio', ''),
                                              'stock': request.form.get('stock', ''),
                                              'activo': activo})
        
        # Actualizar en base de datos
        conn.execute(
            'UPDATE Product SET name_prod = ?, price = ?, stock = ?, active = ? WHERE id = ?',
            (nombre, precio, stock, 1 if activo else 0, id)
        )
        conn.commit()
        conn.close()
        
        flash('Producto actualizado exitosamente.', 'success')
        return redirect(url_for('productos_listar'))
    
    conn.close()
    return render_template('form.html', 
                           subtitulo="Editar Producto", 
                           nombre=session['username'], 
                           page='form',
                           producto=producto,
                           form_data=None)


# ELIMINAR - /productos/<id>/eliminar
@app.route('/productos/<int:id>/eliminar', methods=['POST'])
@login_required
def productos_eliminar(id):
    conn = get_db_connection()
    producto = conn.execute('SELECT * FROM Product WHERE id = ?', (id,)).fetchone()
    
    if producto is None:
        conn.close()
        flash('Producto no encontrado.', 'danger')
        return redirect(url_for('productos_listar'))
    
    conn.execute('DELETE FROM Product WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    
    flash('Producto eliminado exitosamente.', 'success')
    return redirect(url_for('productos_listar'))

@app.route('/form')
@login_required
def form():
    return redirect(url_for('productos_crear'))


@app.route('/products')
@login_required
def products():
    return redirect(url_for('productos_listar'))

# Manejo de errores

@app.errorhandler(404)
def no_route(e):
    flash('Página no encontrada.', 'warning')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
