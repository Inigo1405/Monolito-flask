from repositories.productos_repository import ProductosRepository

class ProductService:
    def __init__(self):
        self.repository = ProductosRepository("database.db")
    
    def get_all_products(self, filters=None):
        return self.repository.get_all_productos(filters)
    
    
    def get_product_by_id(self, product_id):
        return self.repository.get_producto_by_id(product_id)
    

    def create_product(self, name=None, price=None, stock=0, categoria=None, data=None):
        name = data.get('name')
        price = data.get('price')
        stock = data.get('stock', 0)
        categoria = data.get('categoria', None)
        if not name or not price:
            return False
        self.repository.add_producto(name, price, stock, categoria)
        return True

    
    def update_product(self, product_id, name=None, price=None, stock=None, active=None, categoria=None, data=None):
        return self.repository.update_producto(product_id, name, price, stock, active, categoria, data)
    
    
    def delete_product(self, product_id):
        result = self.repository.delete_producto(product_id)
        return result
