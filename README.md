# Employee Management System (CRUD) with Flask and MySQL

Este proyecto es una aplicación CRUD (Crear, Leer, Actualizar, Eliminar) simple para gestionar empleados utilizando Python, Flask y MySQL.

## Requisitos

- Python 3.x
- MySQL
- pip (Python package installer)

## Pasos para crear el proyecto desde 0

### 1. Configura el entorno de desarrollo

#### 1.1. Instalar Python y pip
Asegúrate de tener Python instalado. Si no lo tienes, descárgalo de [aquí](https://www.python.org/downloads/).

#### 1.2. Instalar MySQL
Puedes descargar MySQL desde [aquí](https://dev.mysql.com/downloads/installer/).

#### 1.3. Crear un entorno virtual (opcional pero recomendado)
En la carpeta del proyecto, ejecuta:
```bash
python -m venv venv
source venv/bin/activate    # En Linux/Mac
venv\Scripts\activate       # En Windows


2. Crear la base de datos y la tabla
2.1. Accede a MySQL y crea la base de datos:
    CREATE DATABASE empleados_db;
    USE empleados_db;

2.2. Crear la tabla de empleados:
CREATE TABLE IF NOT EXISTS `tbl_empleados` (
  `id_empleado` int NOT NULL AUTO_INCREMENT,
  `nombre_empleado` varchar(50) DEFAULT NULL,
  `apellido_empleado` varchar(50) DEFAULT NULL,
  `sexo_empleado` int DEFAULT NULL,
  `telefono_empleado` varchar(50) DEFAULT NULL,
  `email_empleado` varchar(50) DEFAULT NULL,
  `profesion_empleado` varchar(50) DEFAULT NULL,
  `foto_empleado` mediumtext,
  `salario_empleado` bigint DEFAULT NULL,
  `fecha_registro` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_empleado`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

2. Config/database.py

Aquí configuramos la conexión a la base de datos MySQL.

    import mysql.connector

    def obtener_conexion():
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='password',  # Cambia tu contraseña
            database='empleados_db'
        )
        return conexion

1. app.py
    Aquí centralizamos todas las rutas y usamos controladores para mantener la lógica separada.

3. Configura el proyecto Flask
3.1. Instalar Flask y otras dependencias necesarias:

    pip install flask flask-mysql-connector

3. Controllers/empleado_controller.py

Controlador que maneja toda la lógica relacionada con los empleados (CRUD).

4. Routers/empleado_routes.py

Archivo que se encarga de definir las rutas específicas para empleados.

5. Vistas (templates/empleado/)
add.html - Formulario para agregar un empleado


3.2. Estructura del proyecto:

    flask_crud_empleados/
    │
    ├── app.py                      # Archivo principal para iniciar la app
    ├── Config/                     # Configuraciones del proyecto
    │   └── database.py             # Configuración de la conexión con la base de datos
    ├── Controllers/                # Funciones principales del proyecto
    │   └── empleado_controller.py  # Lógica de CRUD para empleados
    ├── Routers/                    # Rutas de la aplicación
    │   └── empleado_routes.py      # Rutas relacionadas con los empleados
    ├── templates/                  # Vistas del proyecto
    │   ├── public/                 # Vistas públicas
    │   │   └── view/               # Otras vistas públicas
    │   └── empleado/               # Vistas específicas para empleados
    │       ├── add.html
    │       ├── index.html
    │       ├── update.html
    │       └── view.html
    ├── static/                     # Archivos estáticos (CSS, JS, imágenes, etc.)
    └── README.md


4. Escribe el código
4.1. Código de app.py:

from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Configuración de la conexión a la base de datos
db_config = {
    'user': 'root',
    'password': 'password',  # Cambia esta contraseña
    'host': 'localhost',
    'database': 'empleados_db'
}

def obtener_conexion():
    return mysql.connector.connect(**db_config)

# Ruta principal: Lista de empleados
@app.route('/')
def index():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tbl_empleados")
    empleados = cursor.fetchall()
    conexion.close()
    return render_template('index.html', empleados=empleados)

# Ruta para crear un nuevo empleado
@app.route('/crear', methods=['POST'])
def crear():
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
    
    return redirect(url_for('index'))

# Otras rutas como actualizar y eliminar irán aquí...

if __name__ == '__main__':
    app.run(debug=True)


4.2. Código de templates/index.html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRUD Empleados</title>
</head>
<body>
    <h1>Lista de Empleados</h1>
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Nombre</th>
                <th>Apellido</th>
                <th>Sexo</th>
                <th>Teléfono</th>
                <th>Email</th>
                <th>Profesión</th>
                <th>Salario</th>
            </tr>
        </thead>
        <tbody>
            {% for empleado in empleados %}
            <tr>
                <td>{{ empleado.id_empleado }}</td>
                <td>{{ empleado.nombre_empleado }}</td>
                <td>{{ empleado.apellido_empleado }}</td>
                <td>{{ empleado.sexo_empleado }}</td>
                <td>{{ empleado.telefono_empleado }}</td>
                <td>{{ empleado.email_empleado }}</td>
                <td>{{ empleado.profesion_empleado }}</td>
                <td>{{ empleado.salario_empleado }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
    <h2>Agregar nuevo empleado</h2>
    <form action="/crear" method="POST">
        <input type="text" name="nombre" placeholder="Nombre" required>
        <input type="text" name="apellido" placeholder="Apellido" required>
        <input type="text" name="sexo" placeholder="Sexo" required>
        <input type="text" name="telefono" placeholder="Teléfono" required>
        <input type="email" name="email" placeholder="Email" required>
        <input type="text" name="profesion" placeholder="Profesión" required>
        <input type="number" name="salario" placeholder="Salario" required>
        <button type="submit">Agregar</button>
    </form>
</body>
</html>


5. Ejecutar la aplicación

Para ejecutar la aplicación, ejecuta el siguiente comando en la terminal dentro de la carpeta del proyecto:

python app.py

Luego, abre tu navegador y accede a http://localhost:5000 para ver la lista de empleados.



1. Instalar Flask y otros paquetes necesarios:
    pip install flask
    pip install flask-mysql-connector

2. Crear el archivo requirements.txt:

Para generar automáticamente el archivo requirements.txt con las dependencias instaladas en tu entorno, utiliza el siguiente comando:

    pip freeze > requirements.txt
Esto creará un archivo requirements.txt con todas las dependencias del proyecto.
Ahora, cualquier persona puede instalar las mismas dependencias usando:

    pip install -r requirements.txt

