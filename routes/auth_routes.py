from flask import Flask, render_template, url_for, flash, redirect

# Login y Logout
@app.route('/')
def base():
    if 'username' in session:
        return redirect(url_for('productos_listar'))
    return redirect(url_for('login'))


# Decorador para proteger rutas
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            flash('Debes iniciar sesión para acceder a esta página.', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == USUARIO and password == PASSWORD:
            session['username'] = username
            flash('Inicio de sesión exitoso.', 'success')
            return redirect(url_for('productos_listar'))
        else:
            flash('Usuario o contraseña incorrectos.', 'danger')
            return render_template('login.html')
    
    if 'username' in session:
        return redirect(url_for('productos_listar'))
    
    return render_template('login.html')


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.clear()
    flash('Sesión cerrada correctamente.', 'info')
    return redirect(url_for('login'))