# FastAPI HubSpot-ClickUp Sync

Este proyecto es una API REST construida con FastAPI que permite crear contactos en HubSpot y sincronizarlos con ClickUp. También registra cada llamada a la API en una base de datos PostgreSQL externa.

## Funcionalidades

- Crear contactos en HubSpot a través de un endpoint de la API.
- Sincronizar contactos de HubSpot con ClickUp a través de un endpoint de la API.
- Registrar cada llamada a la API en una base de datos PostgreSQL externa.

## Requisitos

- Python 3.7 o superior
- FastAPI
- Uvicorn
- SQLAlchemy
- Psycopg2-binary
- HubSpot API Client Library
- ClickUp Python

## Instalación

1. Clona este repositorio o descarga el código fuente en tu máquina local.

2. Crea un entorno virtual de Python (opcional, pero recomendado): `python -m venv venv` Activa el entorno virtual:
- Windows: `venv\Scripts\activate`
- Linux/MacOS: `source venv/bin/activate`
3. Instala las dependencias del proyecto: `pip install -r requirements.txt`


4. Configura tus credenciales de HubSpot, ClickUp y PostgreSQL en un archivo `.env`.

5. Inicia el servidor de desarrollo de FastAPI: `uvicorn main:app --reload`

## Uso

Puedes probar los endpoints de la API utilizando una herramienta como [Postman](https://www.postman.com/) o [Insomnia](https://insomnia.rest/) o utilizando `curl` desde la línea de comandos:

- Crear un contacto en HubSpot:
`curl -X POST "http://127.0.0.1:8000/create_hubspot_contact" -H "Content-Type: application/json" -d '{"email": "test@orbidi.com", "firstname": "Test", "lastname": "Orbidi", "phone": "(322) 123-4567", "website": "orbidi.com"}'`


- Sincronizar contactos entre HubSpot y ClickUp: `curl -X POST "http://127.0.0.1:8000/sync_contacts"`


Visita `http://127.0.0.1:8000/docs` en tu navegador para ver la documentación interactiva de la API generada por FastAPI.

## Estructura del proyecto

- `app/`
- `__init__.py`
- `config.py`: Configuraciones de la aplicación (claves API, conexión a la base de datos, etc.)
- `models.py`: Modelos de SQLAlchemy para la base de datos PostgreSQL.
- `schemas.py`: Esquemas de Pydantic para validación de datos y documentación de la API.
- `sessions.py`: Funciones de CRUD para interactuar con la base de datos.
- `api.py`: Funciones para interactuar con las API de HubSpot y ClickUp.
- `database.py`: Configuración de la base de datos y conexión usando SQLAlchemy.
- `main.py`: Archivo principal de la aplicación que contiene la configuración de FastAPI, rutas y funciones de API.
- `requirements.txt`: Archivo con las dependencias del proyecto para facilitar la instalación.
- `.gitignore`: Archivo que especifica los archivos y carpetas que deben ser ignorados por Git.
- `README.md`: Este archivo que contiene información sobre el proyecto e instrucciones de instalación y uso.




