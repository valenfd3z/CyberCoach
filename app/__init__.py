# __init__.py
# Archivo de inicialización de la aplicación Flask
# Contiene la configuración y setup inicial de la aplicación

from flask import Flask
from .database import db
from .config import Config
from .routes import init_app as init_routes

def create_app():
    """
    Función que crea y configura la aplicación Flask
    
    Returns:
        Flask: La aplicación configurada y lista para usar
    """
    # Crear la aplicación Flask
    app = Flask(__name__, 
                template_folder='../templates',
                static_folder='../static')
    
    # Cargar la configuración desde el archivo config.py
    app.config.from_object(Config)

    # Inicializar la base de datos
    db.init_app(app)
    
    # Asegurarse de que la base de datos esté inicializada antes de registrar rutas
    with app.app_context():
        db.create_all()
        
    # Registrar los blueprints
    init_routes(app)
    
    # Asegurar que la base de datos esté disponible en todas las rutas
    @app.before_request
    def before_request():
        db.session.begin()

    return app