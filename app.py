#Importar las librerías necesarias
from flask import Flask
from routes.auth_routes import login_bp
from routes.products_routes import productos_bp
from routes.api_productos import api_products_bp
from config import config


# Establecer la configuración de la aplicación
config = config()
config.apply_config('development')


# Crear la aplicación Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = config.SECRET_KEY


# Registrar los blueprints
app.register_blueprint(login_bp)
app.register_blueprint(productos_bp)
app.register_blueprint(api_products_bp)


if __name__ == '__main__':
    app.run(debug=config.DEBUG)
