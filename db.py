from flask_sqlalchemy import SQLAlchemy
from app import app
db = SQLAlchemy()
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    genero = db.Column(db.String(20), nullable=False)
    colorfavorito = db.Column(db.String(8))

    def __repr__(self):
        return f'<Usuario {self.nombre}>'