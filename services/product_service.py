from repositories.productos_repository import ProductosRepository

class ProductService:
    def __init__(self):
        self.repository = ProductosRepository("database.db")
    
    def get_all_products(self):
        return self.repository.get_all_productos()
    
    def get_product_by_id(self, product_id):
        return self.repository.get_producto_by_id(product_id)
    
    def create_product(self, name, price, stock=0):
        # Aquí puedes agregar validaciones
        if not name or not price:
            return False
        self.repository.add_producto(name, price, stock)
        return True
    
    def update_product(self, product_id, name, price, stock, active):
        return self.repository.update_producto(product_id, name, price, stock, active)
    
    def delete_product(self, product_id):
        return self.repository.delete_producto(product_id)