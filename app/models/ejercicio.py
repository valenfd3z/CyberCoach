# ejercicio.py
# Modelos relacionados con los ejercicios y su relación con las rutinas
# Este módulo define las entidades principales de la aplicación relacionadas con ejercicios

from ..database import db

# Modelo de Ejercicio
# ========================================
# Representa un ejercicio individual en la base de datos
# Cada ejercicio tiene un video asociado y está relacionado con un músculo específico
class Ejercicio(db.Model):
    """
    Modelo que representa un ejercicio individual
    
    Atributos:
        id (Integer): Identificador único del ejercicio (PK)
        nombre (String): Nombre del ejercicio (obligatorio)
        video_url (String): URL del video demostrativo del ejercicio
        musculo (String): Músculo que trabaja el ejercicio (obligatorio)
        
    Notas:
        - El nombre es único por musculo
        - La URL del video es opcional
        - El musculo debe ser uno de los valores permitidos en la aplicación
    """
    
    # Identificador único del ejercicio
    # Usado como clave primaria en la base de datos
    id = db.Column(db.Integer, primary_key=True)
    
    # Nombre del ejercicio
    # Campo obligatorio, máximo 255 caracteres
    nombre = db.Column(db.String(255), nullable=False)
    
    # URL del video demostrativo
    # Campo opcional, máximo 255 caracteres
    # Se usa para mostrar videos de demostración en la interfaz
    video_url = db.Column(db.String(255))
    
    # Músculo que trabaja el ejercicio
    # Campo obligatorio, máximo 120 caracteres
    # Define el grupo muscular al que pertenece el ejercicio
    musculo = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<Ejercicio {self.nombre}>'

# Modelo de EjercicioEnRutina
# ========================================
# Representa la relación many-to-many entre ejercicios y rutinas
class EjercicioEnRutina(db.Model):
    """
    Modelo que representa la relación entre un ejercicio y una rutina
    
    Atributos:
        id (Integer): Identificador único de la relación (PK)
        rutina_id (Integer): Identificador de la rutina (FK)
        nombre_ejercicio (String): Nombre del ejercicio
        series (Integer): Cantidad de series para el ejercicio
        repeticiones (Integer): Cantidad de repeticiones por serie
        
    Notas:
        - Una rutina puede tener múltiples ejercicios
        - Un ejercicio puede estar en múltiples rutinas
        - Las series y repeticiones son específicas por rutina
    """
    __tablename__ = 'ejercicio_en_rutina'
    
    # Identificador único de la relación
    id = db.Column(db.Integer, primary_key=True)
    
    # Identificador de la rutina a la que pertenece

    
    # Nombre del ejercicio
    nombre_ejercicio = db.Column(db.String(100), nullable=False)
    
    # Cantidad de series para el ejercicio
    series = db.Column(db.Integer)
    
    # Cantidad de repeticiones por serie
    repeticiones = db.Column(db.Integer)

    def __repr__(self):
        return f'<EjercicioEnRutina {self.nombre_ejercicio}>'