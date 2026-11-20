import os
from dotenv import load_dotenv
from sqlalchemy import URL, create_engine

def get_engine():
    #Cargar las variables de entorno con load_dotenv().
    load_dotenv()
    #Obtener las credenciales con os.getenv().
    username = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    host = os.getenv("POSTGRES_HOST")
    port = os.getenv("POSTGRES_PORT")
    database = os.getenv("POSTGRES_DB")

    #Validación después de obtener las credenciales
    required_variables = {
    "POSTGRES_USER": username,
    "POSTGRES_PASSWORD": password,
    "POSTGRES_HOST": host,
    "POSTGRES_PORT": port,
    "POSTGRES_DB": database
    }

    missing = [
        name for name, value in required_variables.items()
        if not value
    ]

    if missing:
        raise ValueError(
            f"Missing environment variables: {', '.join(missing)}"
        )
    #Construir la URL de conexión utilizando URL.create().
    connection_url = URL.create(
        drivername="postgresql+psycopg",
        username=username,
        password=password,
        host=host,
        port=port,
        database=database
    )

    #Crear el motor con create_engine().
    engine = create_engine(connection_url)
    #Devolver el objeto Engine.
    return engine