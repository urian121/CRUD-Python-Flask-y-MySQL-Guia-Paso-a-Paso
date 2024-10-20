from flask import render_template, request, redirect, url_for
from Config.database import obtener_conexion

# Función para listar empleados
def listar_empleados():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tbl_empleados")
    empleados = cursor.fetchall()
    conexion.close()
    return render_template('empleado/index.html', empleados=empleados)

# Función para agregar un nuevo empleado
def agregar_empleado():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        sexo = request.form['sexo']
        telefono = request.form['telefono']
        email = request.form['email']
        profesion = request.form['profesion']
        salario = request.form['salario']

        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO tbl_empleados (nombre_empleado, apellido_empleado, sexo_empleado, telefono_empleado, email_empleado, profesion_empleado, salario_empleado)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (nombre, apellido, sexo, telefono, email, profesion, salario))
        conexion.commit()
        conexion.close()
        return redirect(url_for('empleado.listar_empleados'))
    return render_template('empleado/add.html')

