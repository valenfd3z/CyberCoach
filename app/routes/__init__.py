from .main import main_bp
from .auth import auth_bp
from .rutinas import rutinas_bp
from .ejercicios import ejercicios_bp

def init_app(app):
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(rutinas_bp)
    app.register_blueprint(ejercicios_bp) 