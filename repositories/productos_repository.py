import sqlite3

class ProductosRepository:
    def __init__(self, db_path):
        self.db_path = db_path


    def get_all_productos(self, filters=None):
        conn = None
        try:
            conn = sqlite3.connect(self.db_path)
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            if not filters:
                cursor.execute("SELECT * FROM Product ORDER BY id DESC")
            else:
                query = "SELECT * FROM Product WHERE "
                filters_clauses = []
                values = []
                
                # Normalizar filtros (manejar tanto lista como valor directo)
                def get_filter_value(key):
                    val = filters.get(key)
                    if isinstance(val, list):
                        return val[0] if val else None
                    return val
                
                if 'name_prod' in filters:
                    val = get_filter_value('name_prod')
                    if val:
                        filters_clauses.append("name_prod LIKE ?")
                        values.append(f"%{val}%")
                
                if 'categoria' in filters:
                    val = get_filter_value('categoria')
                    if val:
                        filters_clauses.append("categoria = ?")
                        values.append(val)
                
                if 'min_price' in filters:
                    val = get_filter_value('min_price')
                    if val is not None:
                        filters_clauses.append("price >= ?")
                        values.append(val)
                
                if 'max_price' in filters:
                    val = get_filter_value('max_price')
                    if val is not None:
                        filters_clauses.append("price <= ?")
                        values.append(val)
                
                if 'active' in filters:
                    val = get_filter_value('active')
                    if val is not None:
                        filters_clauses.append("active = ?")
                        values.append(val)
                
                if 'min_stock' in filters:
                    val = get_filter_value('min_stock')
                    if val is not None:
                        filters_clauses.append("stock >= ?")
                        values.append(val)
                
                if 'max_stock' in filters:
                    val = get_filter_value('max_stock')
                    if val is not None:
                        filters_clauses.append("stock <= ?")
                        values.append(val)
                
                if not filters_clauses:
                    # Si no hay filtros válidos, retornar todos
                    cursor.execute("SELECT * FROM Product ORDER BY id DESC")
                else:
                    query += " AND ".join(filters_clauses) + " ORDER BY id DESC"
                    cursor.execute(query, values)
            
            productos = cursor.fetchall()
            print(f"Productos obtenidos: {len(productos)}")  # Debugging line
            return productos
            
        except Exception as e:
            raise Exception(f"Error al obtener productos: {str(e)}")
        finally:
            if conn:
                conn.close()

    def get_producto_by_id(self, id):
        try:
            conn = sqlite3.connect(self.db_path)
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Product WHERE id = ?", (id,))
            producto = cursor.fetchone()
            if conn:
                conn.close()
            return producto
        except Exception as e:
            return {"error": f"Error al obtener producto: {str(e)}"}


    def add_producto(self, name_prod, price, stock= 0, categoria=None):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Product (name_prod, price, stock, categoria) VALUES (?, ?, ?, ?)", (name_prod, price, stock, categoria))
            conn.commit()
            if conn:
                conn.close()
            return True
        except Exception as e:
            return {"error": f"Error al agregar producto: {str(e)}"}
    

    def update_producto(self, id, name_prod, price, stock, active, categoria=None, data=None):
        try:
            name_prod = data.get('name_prod', name_prod)
            price = data.get('price', price)
            stock = data.get('stock', stock)
            active = data.get('active', active)
            categoria = data.get('categoria', categoria)
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("UPDATE Product SET name_prod = ?, price = ?,"
                           " stock = ?, active = ?, categoria = ? WHERE id = ?", (name_prod, price, stock, active, categoria, id))
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            return {"error": f"Error al actualizar producto: {str(e)}"}


    def delete_producto(self, id):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Product WHERE id = ?", (id,))
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            return {"error": f"Error al eliminar producto: {str(e)}"}
        