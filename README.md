# Monolito-flask
App web monolítica en Flask

Desarrollar una aplicación web monolítica con Flask (frontend integrado con Jinja) que implemente un CRUD completo para la entidad Producto, incluyendo un login ficticio con sesión y persistencia en SQLite.

## Requerimientos mínimos

### Login ficticio (sesión)
- Ruta `/login` (GET/POST) y `/logout`
- Usuario/contraseña: `admin/admin`
- Proteger rutas del CRUD: sin sesión, redirigir a `/login`

### Entidad Producto (SQLite)
| Campo   | Tipo          | Restricción       |
|---------|---------------|-------------------|
| id      | INTEGER       | autoincrement     |
| nombre  | TEXT          | requerido         |
| precio  | REAL          | >= 0              |
| stock   | INTEGER       | >= 0              |
| activo  | BOOLEAN       | true/false        |

### CRUD completo
| Operación | Ruta                        | Método    |
|-----------|-----------------------------|-----------|
| Listar    | `/productos`                | GET       |
| Crear     | `/productos/nuevo`          | GET/POST  |
| Editar    | `/productos/<id>/editar`    | GET/POST  |
| Eliminar  | `/productos/<id>/eliminar`  | POST      |

### Validaciones mínimas
- `nombre` no vacío
- `precio` y `stock` numéricos y no negativos

## Instalación

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Inicializar base de datos
python db_init.py

# Ejecutar aplicación
python app.py
```

## Acceso
- URL: http://localhost:5000
- Usuario: `admin`
- Contraseña: `admin`