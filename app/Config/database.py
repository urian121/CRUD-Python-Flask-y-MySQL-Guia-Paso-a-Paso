import mysql.connector

def obtener_conexion():
    conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        password='password',  # Cambia tu contraseña
        database='empleados_db'
    )
    return conexion