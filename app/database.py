from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Función para inicializar la base de datos
# ========================================
def init_db(app):
    """
    Inicializa la base de datos con la aplicación Flask
    
    Args:
        app (Flask): La aplicación Flask a la que conectar la base de datos
    """
    db.init_app(app)
    return db
