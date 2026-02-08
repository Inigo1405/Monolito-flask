from flask import session, render_template, flash, redirect, Blueprint, request
from functools import wraps

login_bp = Blueprint('auth', __name__,
                     template_folder='templates')

# Login y Logout
@login_bp.route('/')
def base():
    if 'username' in session:
        return redirect('/productos')
    return redirect('/login')


# Decorador para proteger rutas
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            flash('Debes iniciar sesión para acceder a esta página.', 'warning')
            return redirect('/login')
        return f(*args, **kwargs)
    return decorated_function


# Iniciar sesión
@login_bp.get('/login')
def login():
    return render_template('login.html')


@login_bp.post('/login')
def login_post():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == "admin" and password == "admin":
            session['username'] = username
            flash('Inicio de sesión exitoso.', 'success')
            return redirect('/productos')
        else:
            flash('Usuario o contraseña incorrectos.', 'danger')
            return render_template('login.html')
    
    if 'username' in session:
        return redirect('/productos')


# Salir de la sesión
@login_bp.route('/logout', methods=['GET', 'POST'])
def logout():
    session.clear()
    flash('Sesión cerrada correctamente.', 'info')
    return redirect('/login')
