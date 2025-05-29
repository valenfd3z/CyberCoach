from flask import Blueprint, render_template, request, redirect, url_for, current_app, session
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.usuario import Usuario
from app.database import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/registrar', methods=['GET', 'POST'])
def registrar_usuario():
    if request.method == 'POST':
        try:
            # Obtener datos del formulario
            gmail = request.form['email']
            nombre_usuario = request.form['username']
            contrasena = request.form['password']
            confirmar_contrasena = request.form['confirm_password']

            # Validaciones básicas
            if not all([gmail, nombre_usuario, contrasena, confirmar_contrasena]):
                return render_template('registro.html', 
                                    error='Todos los campos son requeridos.',
                                    email=gmail,
                                    username=nombre_usuario)

            # Validar contraseñas
            if contrasena != confirmar_contrasena:
                return render_template('registro.html', 
                                    error='Las contraseñas no coinciden.',
                                    email=gmail,
                                    username=nombre_usuario)

            # Verificar si el usuario ya existe
            usuario_existente_nombre = Usuario.query.filter_by(nombre_usuario=nombre_usuario).first()
            if usuario_existente_nombre:
                return render_template('registro.html', 
                                    error='El nombre de usuario ya existe.',
                                    email=gmail)

            usuario_existente_gmail = Usuario.query.filter_by(gmail=gmail).first()
            if usuario_existente_gmail:
                return render_template('registro.html', 
                                    error='El correo electrónico ya está registrado.',
                                    username=nombre_usuario)

            # Crear nuevo usuario
            contrasena_encriptada = generate_password_hash(contrasena)
            nuevo_usuario = Usuario(gmail=gmail, nombre_usuario=nombre_usuario, contrasena=contrasena_encriptada)
            
            try:
                db.session.add(nuevo_usuario)
                db.session.commit()
                return redirect(url_for('.iniciar_sesion'))
            except Exception as e:
                db.session.rollback()
                print(f"Error al guardar en la base de datos: {str(e)}")
                return render_template('registro.html', 
                                    error='Error al crear la cuenta. Por favor intenta nuevamente.',
                                    email=gmail,
                                    username=nombre_usuario)

        except Exception as e:
            print(f"Error en el registro: {str(e)}")
            return render_template('registro.html', 
                                error='Error en el registro. Por favor intenta nuevamente.',
                                email=request.form.get('email', ''),
                                username=request.form.get('username', ''))

    return render_template('registro.html')

@auth_bp.route('/iniciar_sesion', methods=['GET', 'POST'])
def iniciar_sesion():
    if request.method == 'POST':
        nombre_usuario = request.form['username']
        contrasena = request.form['password']

        usuario = Usuario.query.filter_by(nombre_usuario=nombre_usuario).first()

        if usuario and check_password_hash(usuario.contrasena, contrasena):
            session['user_id'] = usuario.id
            session['nombre_usuario'] = usuario.nombre_usuario
            return redirect(url_for('main.pagina_principal'))
        else:
            return render_template('login.html', error='Credenciales inválidas.')
    return render_template('login.html')

@auth_bp.route('/cerrar_sesion')
def cerrar_sesion():
    session.pop('user_id', None)
    session.pop('nombre_usuario', None)
    return redirect(url_for('main.pagina_principal')) 