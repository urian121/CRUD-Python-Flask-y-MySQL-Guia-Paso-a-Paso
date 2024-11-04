# Importando Libreria mysql.connector para conectar Python con MySQL
import mysql.connector

def obtener_conexion():
    try:
        conexionBD = mysql.connector.connect(
            host='localhost',
            user='root',
            password='password',
            database='empleados_db'
        )
        print("Conexión exitosa")
        return conexionBD
    except mysql.connector.Error as err:
        print("Error al conectar a la base de datos:", err)
        return None
