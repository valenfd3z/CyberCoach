# run.py
# Archivo de ejecución principal de la aplicación

from app import create_app

# Crear la aplicación Flask
app = create_app()

if __name__ == '__main__':
    # Ejecutar la aplicación en modo desarrollo
    # El modo debug=True permite:
    # - Recargar automáticamente al modificar el código
    # - Mostrar mensajes de error detallados
    # - Debugging interactivo
    app.run(debug=True)