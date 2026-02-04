# Monolito-flask
App web monolítica en Flask

Desarrollar una aplicación web monolítica con Flask (frontend integrado con Jinja) que implemente un CRUD completo para la entidad Producto, incluyendo un login  ficticio con sesión y persistencia en SQLite

# Link del repositorio
https://github.com/Inigo1405/Monolito-flask

# Preguntas sobre la arquitectura monolítica
### ¿Qué quedó más acoplado en el monolito?
Todas las operaciones que se ejecutan de autenticación y escritura en la base de datos se ejecutan desde el mismo lugar que los servicios para realizar consultas simples sin la necesidad de permisos, restringiendo la adopción de la aplicación.

### ¿Qué separarías primero si lo migraras a API/microservicio?
Proponemos una separación por responsabilidades de cada uno de los bloques para mantener una mayor limpieza de arquitectura y una futura escalabilidad del sistema, separando el Front-end (UI/UX), el backend y la base de datos (SQLite) en microservicios independientes, lo que haría que el sistema sea menos propenso a caidas totales de este.

### ¿Qué problemas surgen si dos equipos trabajan en paralelo en el mismo monolito?
Surgen problemas en el control de veriones (Git) y en el trabajo colaborativo en el sistema, ya que al estar trabajando equipos en el mismo monolito progresivamente alguno de los equipos presentará problemas de migraciones al no estar a la par del otro y estar modificando el mismo monolito, lo que retrasaría la implementación de nuevas funcionalidades del sistema al estar reparando continuamente el sistema haciendo unicamente retrabajos.

## Acceso al sistema de Productos (Test)
- Nombre de Usuario: `admin`
- Contraseña: `admin`


### Entidad Producto (SQLite)
| Campo   | Tipo          | Restricción       |
|---------|---------------|-------------------|
| id      | INTEGER       | autoincrement     |
| nombre  | TEXT          | not null          |
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


## Instalación e Inicio de Sistema

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
flask run
```