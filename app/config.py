# config.py
# Archivo de configuración de la aplicación
# Contiene todas las configuraciones necesarias para la aplicación

import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
# Esto permite mantener las credenciales fuera del código
load_dotenv()

class Config:
    """
    Clase que contiene toda la configuración de la aplicación
    
    Atributos:
        SECRET_KEY: Clave secreta para la aplicación
        DB_CONFIG: Configuración de la base de datos PostgreSQL
        SQLALCHEMY_DATABASE_URI: URI de conexión a la base de datos
        SQLALCHEMY_TRACK_MODIFICATIONS: Configuración de SQLAlchemy
    """
    
    # Clave secreta para la aplicación
    # Se obtiene del archivo .env o usa un valor por defecto
    SECRET_KEY = os.getenv('SECRET_KEY', 'clave-secreta-por-defecto')
    
    # Configuración de la base de datos PostgreSQL
    # Todas las credenciales se obtienen del archivo .env
    DB_CONFIG = {
        'usuario': os.getenv('DB_USUARIO', 'postgres'),
        'contrasena': os.getenv('DB_CONTRASENA', 'awds'),
        'host': os.getenv('DB_HOST', 'localhost'),
        'puerto': os.getenv('DB_PUERTO', '5432'),
        'nombre': os.getenv('DB_NOMBRE', 'cybercoach_db')
    }
    
    # URI de conexión a la base de datos
    # Se construye usando las credenciales de DB_CONFIG
    SQLALCHEMY_DATABASE_URI = (
        f'postgresql://{DB_CONFIG["usuario"]}:{DB_CONFIG["contrasena"]}'
        f'@{DB_CONFIG["host"]}:{DB_CONFIG["puerto"]}/{DB_CONFIG["nombre"]}'
    )
    
    # Configuración de SQLAlchemy
    # Desactiva el tracking de modificaciones para mejorar el rendimiento
    SQLALCHEMY_TRACK_MODIFICATIONS = False