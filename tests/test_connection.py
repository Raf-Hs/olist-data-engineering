#Importar get_engine.
from sqlalchemy import text

from src.database.connection import get_engine

def test_postgres_connection():
    #Obtener el motor.
    engine = get_engine()
    #Abrir una conexión mediante engine.connect().
    with engine.connect() as connection:
        #Ejecutar SELECT version().
        result = connection.execute(text("SELECT version()"))
        #Recuperar el resultado con scalar_one().
        version = result.scalar_one()
        #Comprobar que la respuesta contiene "PostgreSQL".
        assert "PostgreSQL" in version

    #Comando para probar python -m pytest tests/test_connection.py -v