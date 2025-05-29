from flask import Blueprint, render_template

rutinas_bp = Blueprint('rutinas', __name__, url_prefix='/rutinas')

@rutinas_bp.route('/')
def rutinas():
    """Página principal de rutinas con información general."""
    return render_template('rutinas.html')