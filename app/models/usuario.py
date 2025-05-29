from app.database import db

# Modelo de Usuario que representa a los usuarios de la aplicación
class Usuario(db.Model):
    __tablename__ = 'usuario'
    
    id = db.Column(db.Integer, primary_key=True)
    gmail = db.Column(db.String(255), unique=True, nullable=False)
    nombre_usuario = db.Column(db.String(120), unique=True, nullable=False)
    contrasena = db.Column(db.String(255), nullable=False)

    def __init__(self, gmail, nombre_usuario, contrasena):
        self.gmail = gmail
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena

    def __repr__(self):
        return f'<Usuario {self.nombre_usuario}>'