# Importando Libreria mysql.connector para conectar Python con MySQL
import mysql.connector

def obtener_conexion():
    conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        password='password',  # Cambia tu contraseña
        database='empleados_db'
    )
    if conexion:
        print("Conexión exitosa")
    else:
        print("Error en la conexión a la base de datos")
    return conexion