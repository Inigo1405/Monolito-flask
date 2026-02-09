import sqlite3

class ProductosRepository:
    def __init__(self, db_path):
        self.db_path = db_path

    def get_all_productos(self):
        try:
            conn = sqlite3.connect(self.db_path)
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Product ORDER BY id DESC")
            productos = cursor.fetchall()
            conn.close()
            return productos
        except Exception as e:
            return {"error": f"Error al obtener productos: {str(e)}"}

    def get_producto_by_id(self, id):
        try:
            conn = sqlite3.connect(self.db_path)
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Product WHERE id = ?", (id,))
            producto = cursor.fetchone()
            conn.close()
            return producto
        except Exception as e:
            return {"error": f"Error al obtener producto: {str(e)}"}

    def add_producto(self, name_prod, price, stock= 0):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Product (name_prod, price, stock) VALUES (?, ?, ?)", (name_prod, price, stock))
            conn.commit()
            conn.close()
        except Exception as e:
            return {"error": f"Error al agregar producto: {str(e)}"}
    
    def update_producto(self, id, name_prod, price, stock, active):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("UPDATE Product SET name_prod = ?, price = ?,"
                           " stock = ?, active = ?  WHERE id = ?", (name_prod, price, stock, active, id))
            conn.commit()
            conn.close()
        except Exception as e:
            return {"error": f"Error al actualizar producto: {str(e)}"}
        
    def delete_producto(self, id):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Product WHERE id = ?", (id,))
            conn.commit()
            conn.close()
        except Exception as e:
            return {"error": f"Error al eliminar producto: {str(e)}"}