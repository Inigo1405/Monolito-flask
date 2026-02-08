from flask import session, render_template, flash, redirect, Blueprint, request
from routes.auth_routes import login_required
from repositories.productos_repository import ProductosRepository

productos_bp = Blueprint('products', __name__,
                     template_folder='templates')

ProductosRepository = ProductosRepository("database.db")

# LISTAR PRODUCTOS
@productos_bp.get('/productos')
@login_required
def productos_listar():
    productos = ProductosRepository.get_all_productos()
    return render_template('products.html', 
                           productos=productos,
                           nombre=session['username'], 
                           page='products')


@productos_bp.get('/productos/nuevo')
@login_required
def productos_crear():
    return render_template('form.html', 
                            subtitulo="Nuevo Producto", 
                            nombre=session['username'], 
                            page='form',
                            producto=None,
                            form_data=None)


# CREAR PRODUCTO
@productos_bp.post('/productos/nuevo')
@login_required
def productos_crear_post():
    name_prod = request.form.get('name_prod')
    price = request.form.get('price')
    stock = request.form.get('stock', 0)
    ProductosRepository.add_producto(name_prod, price, stock)
    flash('Producto creado exitosamente.', 'success')
    return redirect('/productos')


# EDITAR PRODUCTO
@productos_bp.get('/productos/editar/<int:id>')
@login_required
def productos_editar_get(id):
    producto = ProductosRepository.get_producto_by_id(id)
    if not producto:
        flash(f'Producto con ID {id} no encontrado.', 'danger')
        return redirect('/productos')
    return render_template('form.html', 
                            subtitulo="Editar Producto", 
                            nombre=session['username'], 
                            page='form',
                            producto=producto,
                            form_data=None)

# EDITAR PRODUCTO
@productos_bp.post('/productos/editar/<int:id>')
@login_required
def productos_editar_post(id):
    name_prod = request.form.get('name_prod')
    price = request.form.get('price')
    stock = request.form.get('stock')
    active = request.form.get('active') == 'on'
    ProductosRepository.update_producto(id, name_prod, price, stock, active)
    flash(f'Producto con ID {id} actualizado exitosamente.', 'success')
    return redirect('/productos')
    

# ELIMINAR PRODUCTO
@productos_bp.post('/productos/eliminar/<int:id>')
@login_required
def productos_eliminar(id):
    ProductosRepository.delete_producto(id)
    flash(f'Producto con ID {id} eliminado exitosamente.', 'success')
    return redirect('/productos')
