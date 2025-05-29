# Mi Aplicación Flask

Esta es una aplicación web desarrollada con Flask que incluye autenticación de usuarios, manejo de sesiones y una base de datos SQL.

## Requisitos

- Python 3.8 o superior
- Dependencias listadas en `requirements.txt`

## Instalación

1. Clonar el repositorio:
```bash
git clone [URL_DEL_REPOSITORIO]
cd proyecto
```

2. Crear y activar un entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Configurar variables de entorno:
Crea un archivo `.env` con las siguientes variables:
```
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=tu_clave_secreta
DATABASE_URL=sqlite:///app.db
```

5. Inicializar la base de datos:
```bash
flask db init
flask db migrate
flask db upgrade
```

6. Ejecutar la aplicación:
```bash
flask run
```

## Despliegue en Render

1. Crear una cuenta en Render (https://render.com)
2. Crear un nuevo Web Service
3. Conectar con tu repositorio de GitHub
4. Configurar las variables de entorno en Render:
   - FLASK_APP: app.py
   - FLASK_ENV: production
   - SECRET_KEY: tu_clave_secreta
   - DATABASE_URL: sqlite:///app.db

5. Render se encargará automáticamente de:
   - Instalar las dependencias
   - Configurar el servidor web
   - Ejecutar la aplicación

## Estructura del Proyecto

```
proyecto/
├── app/
│   ├── __init__.py
│   ├── models/
│   ├── routes/
│   └── static/
├── static/
├── templates/
├── app.py
├── requirements.txt
├── run.py
└── .env
```
