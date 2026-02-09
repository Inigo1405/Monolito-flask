from flask import Blueprint, request, jsonify
from services.product_service import ProductService

api_products_bp = Blueprint('products_api', __name__,
                     template_folder='templates', url_prefix='/api')

product_service = ProductService()

# LISTAR PRODUCTOS
@api_products_bp.get('/productos')
def _api_productos_listar():
    try:
        filters = request.get_json() or {}
        productos = product_service.get_all_products(filters)
        print(productos)  # Debugging line
        if not productos:
            return jsonify({'status': 'No se encontraron productos', 'productos': productos}), 404
        return jsonify({'status': 'Productos encontrados', 'productos': [dict(producto) for producto in productos]}), 200
    except Exception as e:
        return jsonify({'status': 'Error al listar los productos', 'error': str(e)}), 500


# OBTENER PRODUCTO POR ID
@api_products_bp.get('/productos/<int:id>')
def _api_productos_obtener(id):
    try:
        producto = product_service.get_product_by_id(id)
        if not producto:
            return jsonify({'status': 'Producto no encontrado'}), 404
        return jsonify({'status': 'Producto encontrado', 'producto': dict(producto)}), 200
    except Exception as e:
        return jsonify({'status': 'Error al obtener el producto', 'error': str(e)}), 500


# CREAR PRODUCTO
@api_products_bp.post('/productos')
def _api_productos_crear():
    try:
        body = request.get_json()
        if product_service.create_product(body):
            return jsonify({'status': 'Producto creado exitosamente'}), 201
        else:
            return jsonify({'status': 'Error al crear el producto'}), 400
    except Exception as e:
        return jsonify({'status': 'Error al crear el producto', 'error': str(e)}), 500

# EDITAR PRODUCTO
@api_products_bp.patch('/productos/<int:id>')
def _api_productos_editar(id):
    try:
        body = request.get_json()
        result = product_service.update_product(id, body)
        if result:
            return jsonify({'status': 'Producto actualizado exitosamente'}), 200
        else:
            return jsonify({'status': 'Error al actualizar el producto'}), 400
    except Exception as e:
        return jsonify({'status': 'Error al actualizar el producto', 'error': str(e)}), 500
    

# ELIMINAR PRODUCTO
@api_products_bp.delete('/productos/<int:id>')
def _api_productos_eliminar(id):
    try:
        result = product_service.delete_product(id)
        if result:
            return jsonify({'status': 'Producto eliminado exitosamente'}), 200
        else:
            return jsonify({'status': 'Error al eliminar el producto'}), 400
    except Exception as e:
        return jsonify({'status': 'Error al eliminar el producto', 'error': str(e)}), 500
