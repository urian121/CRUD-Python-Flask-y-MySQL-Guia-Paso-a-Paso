from Config.database import connectionBD, obtener_conexion


def selectAll(tabla, condicional="", orderBy=""):
    try:
        with connectionBD() as conexion_MySQLdb:
            with conexion_MySQLdb.cursor(dictionary=True) as cursor:
                querySQL = f"SELECT * FROM {tabla}"
                cursor.execute(querySQL)
                data = cursor.fetchall()
        return data
    except Exception as e:
        print(f"Error en la función selectAll: {e}")
        return "Ocurrió al realizar la consulta.", 500
    
    
"""
@app.route('/grados-demo/')
def gradosx():
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM tbl_grados")
        grados = cursor.fetchall()
        conexion.close()
        return render_template('grados/index.html', grados=grados)
    except Exception as e:
        print(e)
"""