from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def pagina_principal():
    return render_template('index.html')

@main_bp.route('/dietas')
def dietas():
    """Página principal de dietas con información general."""
    return render_template('dietas.html') 