# Monolito-flask
App web monolítica en Flask

# Link del repositorio
https://github.com/Inigo1405/Monolito-flask

# Preguntas sobre la arquitectura monolítica
¿Qué quedó más acoplado en el monolito?
Todas las operaciones que se ejecutan de autenticación y escritura en la base de datos se ejecutan desde el mismo lugar que los servicios para realizar consultas simples sin la necesidad de permisos, restringiendo la adopción de la aplicación.

¿Qué separarías primero si lo migraras a API/microservicio?
Proponemos que se separe la interfaz del usuario del backend y base de datos ya que no deberíamos de permitir al usuario interferir con la lógica de negocio.

¿Qué problemas surgen si dos equipos trabajan en paralelo en el mismo monolito?
El problema principal que se presenta sean personas o agentes de IA es la cola de espera a que cada miembro termine una función, por la arquitectura monolítica todos implementan sus funciones en el mismo servicio. 

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