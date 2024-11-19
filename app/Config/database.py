# Importando Libreria mysql.connector para conectar Python con MySQL
import mysql.connector
from contextlib import contextmanager

def obtener_conexion():
    try:
        conexionBD = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='bd_sistema_colegio_python_flask'
        )
        if conexionBD.is_connected():
            # print("Conexión exitosa a la BD")
            return conexionBD

    except mysql.connector.Error as error:
        print(f"No se pudo conectar: {error}")
        return None

"""
la función connectionBD() con @contextmanager es esencial para lograr esa estructura limpia usando with.
Este decorador permite controlar que la conexión se cierre automáticamente al salir del bloque with,
lo cual asegura una gestión más segura de los recursos y evita fugas de conexión.
"""
@contextmanager
def connectionBD():
    conexion = obtener_conexion()
    try:
        yield conexion
    finally:
        if conexion and conexion.is_connected():
            conexion.close()
            print("Conexión cerrada")
            
            
"""
Explicación:

Context Manager: connectionBD usa @contextmanager de contextlib para permitir el uso de with en la conexión, asegurando que siempre se cierre.
Manejo de Cursor: Con with conexion_MySQLdb.cursor(dictionary=True) as cursor, el cursor se gestiona automáticamente sin tener que cerrarlo explícitamente.
Consulta y Renderizado: Si la conexión y el cursor se abren correctamente, el resultado de grados se pasa al template. En caso de error, se maneja la excepción y se retorna un mensaje.
"""