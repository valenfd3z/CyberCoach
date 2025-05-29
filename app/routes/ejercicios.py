from flask import Blueprint, render_template
from ..models import Ejercicio

ejercicios_bp = Blueprint('ejercicios', __name__, url_prefix='/ejercicios')

@ejercicios_bp.route('/')
def pagina_ejercicios():
    ejercicios_db = Ejercicio.query.all()
    ejercicios_organizados = {}
    for ejercicio in ejercicios_db:
        if ejercicio.musculo not in ejercicios_organizados:
            ejercicios_organizados[ejercicio.musculo] = []
        ejercicios_organizados[ejercicio.musculo].append({
            'nombre': ejercicio.nombre,
            'video_url': ejercicio.video_url
        })
    return render_template('ejercicios.html', ejercicios=ejercicios_organizados)