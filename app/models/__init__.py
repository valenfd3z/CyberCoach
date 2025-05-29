from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .usuario import Usuario
from .rutina import Rutina
from .ejercicio import Ejercicio, EjercicioEnRutina 