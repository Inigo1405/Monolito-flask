import os

class config():
    def __init__(self):
        self.SECRET_KEY = ''
        self.DB_PATH = ''
        self.DEBUG = False
        self.TESTING = False
        self.mode = 'production'

    def load_from_env(self):
        self.SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key-here-change-in-production')
        self.DB_PATH = os.getenv('DB_PATH', 'productos.db')

    def set_development_config(self):
        self.DEBUG = True
        self.TESTING = True

    def set_production_config(self):
        self.DEBUG = False
        self.TESTING = False
        
    def apply_config(self, mode):
        if mode == 'development':
            self.set_development_config()
            self.load_from_env()
        elif mode == 'production':
            self.set_production_config()
            self.load_from_env()
