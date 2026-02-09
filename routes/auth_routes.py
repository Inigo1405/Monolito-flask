from flask import session, render_template, flash, redirect, Blueprint, request
from functools import wraps

from services.auth_service import Authentication

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
    auth = Authentication()
    
    username = request.form.get('username')
    password = request.form.get('password')
    
    if auth.login(username, password):
        flash('Inicio de sesión exitoso.', 'success')
        return redirect('/productos')
    else:
        flash('Usuario o contraseña incorrectos.', 'danger')
        return render_template('login.html')
    

# Salir de la sesión
@login_bp.route('/logout', methods=['GET', 'POST'])
def logout():
    auth = Authentication()
    auth.logout()
    flash('Sesión cerrada correctamente.', 'info')
    return redirect('/login')
