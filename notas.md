




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

1. Config/database.py

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

### Expresiones de Gratitud 🎁

    Comenta a otros sobre este proyecto 📢
    Invita una cerveza 🍺 o un café ☕
    Paypal iamdeveloper86@gmail.com
    Da las gracias públicamente 🤓.

## No olvides SUSCRIBIRTE 👍


https://jinja.palletsprojects.com/en/2.10.x/templates/#template-inheritance

<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="{{ url_for('static', filename= 'css/style.css') }}">
    <title>FlaskBlog</title>
</head>
Aquí utiliza la función de ayuda url_for() para generar la ubicación apropiada del archivo. El primer argumento especifica que está vinculando a un archivo estático, y el segundo argumento es la ruta del archivo dentro del directorio estático.

Para crear una plantilla base, primero cree un archivo llamado base.html dentro de su directorio templates
nano templates/base.html


 las siguientes partes resaltadas son específicas para el motor de plantillas Jinja:

    {% block title %} {% endblock %}: un bloque que sirve como marcador de posición para un título. Más adelante lo usará en otras plantillas para dar un título personalizado a cada página de su aplicación sin tener que reescribir toda la sección <head> cada vez.
    {{ url_for('index')}: una invocación de función que devolverá la URL para la función de vista index(). Esto es diferente a la invocación anterior url_for() que utilizó para vincular a un archivo CSS estático, porque solo requiere un argumento, que es el nombre de la función de vista, y enlaza a la ruta asociada con la función en vez de con un archivo estático.
    {% block content %} {% endblock %}: otro bloque que se sustituirá por contenido dependiendo de la plantilla secundaria (plantillas que heredan de base.html) que lo anulará.

Ahora que tiene una plantilla base, puede aprovecharla usando la herencia. Abra el archivo index.html:

    nano templates/index.html

{% extends 'base.html' %}

{% block content %}
    <h1>{% block title %} Welcome to FlaskBlog {% endblock %}</h1>
{% endblock %}

En esta nueva versión de la plantilla index.html, utiliza la etiqueta {% extends %} para que herede de la plantilla base.html. Luego la extiende sustituyendo el bloque content en la plantilla base con lo que está dentro del bloque content en el bloque de código anterior.

Este bloque content contiene una etiqueta <h1> con el texto Welcome to FlaskBlog dentro de un bloque title, que a su vez sustituye el bloque title original en la plantilla base.html con el texto Welcome to FlaskBlog. De esta forma, puede evitar repetir el mismo texto dos veces, ya que funciona como título para la página y como encabezado que aparece bajo la barra de navegación heredada de la plantilla base.

La herencia de plantillas también le ofrece la capacidad de reutilizar el código HTML que tiene en otras plantillas (base.html en este caso), sin tener que repetirlo cada vez que sea necesario.


Aquí, la sintaxis {% for post in posts %} es un bucle for Jinja, que es similar a un bucle for Python, excepto que tiene que ser cerrado posteriormente con la sintaxis {% endfor %}. Utiliza esta sintaxis para realizar un bucle sobre cada elemento en la lista posts que se pasó por la función index() en la línea return render_template('index.html', posts=posts). Dentro de este bucle for, muestra el título de la entrada en un encabezado <h2> dentro de una etiqueta <a> (más tarde utilizará esta etiqueta para vincular con cada entrada individualmente).

Muestra el título utilizando un delimitador variable literal ({{ ... }}). Recuerde que post será un objeto similar a un diccionario, para que pueda acceder al título de la entrada con post['title']​​​. También muestra la fecha de creación de la entrada usando el mismo método.


create.html

{% extends 'base.html' %}

{% block content %}
<h1>{% block title %} Create a New Post {% endblock %}</h1>

<form method="post">
    <div class="form-group">
        <label for="title">Title</label>
        <input type="text" name="title"
               placeholder="Post title" class="form-control"
               value="{{ request.form['title'] }}"></input>
    </div>

    <div class="form-group">
        <label for="content">Content</label>
        <textarea name="content" placeholder="Post content"
                  class="form-control">{{ request.form['content'] }}</textarea>
    </div>
    <div class="form-group">
        <button type="submit" class="btn btn-primary">Submit</button>
    </div>
</form>
{% endblock %}


edit.html
{% extends 'base.html' %}

{% block content %}
<h1>{% block title %} Edit "{{ post['title'] }}" {% endblock %}</h1>

<form method="post">
    <div class="form-group">
        <label for="title">Title</label>
        <input type="text" name="title" placeholder="Post title"
               class="form-control"
               value="{{ request.form['title'] or post['title'] }}">
        </input>
    </div>

    <div class="form-group">
        <label for="content">Content</label>
        <textarea name="content" placeholder="Post content"
                  class="form-control">{{ request.form['content'] or post['content'] }}</textarea>
    </div>
    <div class="form-group">
        <button type="submit" class="btn btn-primary">Submit</button>
    </div>
</form>
<hr>
{% endblock %}


delete.html
<hr>

<form action="{{ url_for('delete', id=post['id']) }}" method="POST">
    <input type="submit" value="Delete Post"
            class="btn btn-danger btn-sm"
            onclick="return confirm('Are you sure you want to delete this post?')">
</form>

{% endblock %}


@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    post = get_post(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('index'))


@app.route('/about')
def about():
    return render_template(
        "about.html",
        title = "About HelloFlask",
        content = "Example app page for Flask.")


    from flask import Flask, render_template
from datetime import datetime
 
app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template('index.html', title='Home', name='User', datetime=datetime.now())
 
if __name__ == '__main__':
    app.run(debug=True)

    
** Archivos estaticos en Flask
** Cómo crear y utilizar plantillas en Flask
En la sección anterior, usted aprendió cuáles son plantillas y archivos estáticos, y por qué son importantes para el desarrollo de la web. En esta sección, aprenderá cómo crear y utilizar plantillas en Flask para mostrar páginas web dinámicas.

Para crear y utilizar plantillas en Flask, es necesario seguir estos pasos:

    Crea una carpeta con plantillas nombradas en el directorio de tu proyecto. Aquí es donde almacenará sus archivos de plantilla.
    Crear un archivo de plantilla con la extensión .html en la carpeta plantillas. Puedes nombrarlo lo que quieras, pero es una buena práctica usar nombres descriptivos que coin figuren con el propósito de la plantilla. Por ejemplo, puedes nombrar tu plantilla file index.html si muestra la página principal de tu web 

la aplicación.
Escriba su código HTML en el archivo de plantilla. Puede utilizar cualquier etiqueta y atributos HTML que desee, pero debe utilizar una sintaxis especial para insertar variables y expresiones que serán reemplazadas por Flask en tiempo de ejecución. La sintaxis es de "Varia" o expresuación. Por ejemplo, puedes usar el título de tu página web.
Importe la función render-template de Flask en su archivo Python. Esta función toma el nombre del archivo de plantilla como argumento y devuelve el código HTML renderado.
Utilíce la función render-template en su función de ruta para devolver la plantilla como respuesta. También puede pasar cualquier variable o dato que desee utilizar en la plantilla como argumentos de palabras clave. Por ejemplo, puede utilizar la plantilla de retorno render-template(.index.html, title=-Home-) para renderizar la plantilla de índice y pasar el título como datos.

** Cómo crear y utilizar archivos estáticos en Flask
Los archivos estáticos son archivos que no son procesados por Flask, tales como archivos CSS y JavaScript. Estos archivos se utilizan generalmente para añadir estilo e interactividad a sus páginas web. En esta sección, aprenderá cómo crear y utilizar archivos estáticos en Flask.

Para usar archivos estáticos en Flask, necesita seguir estos pasos:

    Crea una carpeta llamada estática en el directorio de tu proyecto. Aquí es donde almacenarás tus archivos estáticos.
    Crear archivos estáticos con las extensiones apropiadas en la carpeta estática. Puedes nombrarles lo que quieras, pero es una buena práctica usar nombres descriptivos que coin figuren con el propósito del archivo. Por ejemplo, puede nombrar su archivo CSS style.css si define el estilo de su página web.
    Escriba su código en los archivos estáticos. Puede utilizar cualquier sintaxis y características que sean compatibles con el tipo de archivo. Por ejemplo, puede utilizar selectores, propiedades y valores de CSS para estilizar sus elementos HTML en el archivo CSS.
    Vincular sus archivos estáticos a sus archivos de plantilla usando la función url-for de Flask. Esta función toma el nombre del endpoint y el nombre del archivo como argumentos y devuelve la URL del archivo estático. Por ejemplo, puedes usar .link rel=-stylesheet. href=. url.for(.static-, filename=-style.css- para vincular tu archivo CSS a tu archivo HTML.

- Aquí hay un ejemplo de un simple archivo estático que define el estilo de la página web:
  body {
    font-family: Arial, sans-serif;
    background-color: lightblue;
}
 
h1 {
    color: white;
    text-align: center;
}
 
ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
}
 
li {
    display: inline-block;
    margin: 10px;
    padding: 10px;
    border: 1px solid black;
    background-color: white;
}
- Y aquí hay un ejemplo de un archivo de plantilla que enlaza el archivo estático:
<html>
<head>
    <title>Products</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <h1>Products</h1>
    <ul>
        {% for product in products %}
        <li>{{ product.name }} - {{ product.price }}</li>
        {% endfor %}
    </ul>
</body>
</html>

*** Cómo personalizar sus plantillas con Jinja2
Jinja2 es un motor de plantilla que Flask utiliza para procesar plantillas. Proporga un rico conjunto de características y sintaxis que puede utilizar para hacer sus plantillas más flexibles y expresivas. En esta sección, aprenderá cómo personalizar tus plantillas con Jinja2.

Para personalizar tus plantillas con Jinja2, necesitas usar una sintaxis especial que empiece y termine con aparatos corridos y signos porcentuales, como este: . %1 . Esta sintaxis le permite añadir el flujo de lógica y control a sus plantillas, tales como condiciones, bucles, filtros, macros y otras características. Por ejemplo, puedes usar el porcentaje de condición si la condición % y el % endif %- para añadir una declaración si a tu plantilla, o al% para el elemento en el porcentaje de iterable y % para % para añadir un para el bucle a tu plantilla.

Aquí están algunas de las características y sintaxis más comunes que puede utilizar para personalizar sus plantillas con Jinja2:

    Variables : Puede utilizar variables para almacenar y mostrar datos en sus plantillas. Puedes usar la misma sintaxis que en 

    Python asignar y acceder a variables, como esta: "% de nombre conjunto = "User" % y nombre. También puede utilizar la notación de punto para acceder a los atributos y métodos de los objetos, como este: - product.name y producto.Preséndito .
    Expresiones: Puedes usar expresiones para realizar cálculos y operaciones en tus plantillas. Puedes usar la misma sintaxis que en Python para escribir expresiones como esta: 2 2 y producto.Preprecio * 1.1 . También puedes usar operadores de comparación y lógica, como este: product.Presaje 10 y .name.
    Filtros : Puede utilizar filtros para modificar y formatear la salida de variables y expresiones en sus plantillas. Puedes usar el símbolo de la tubería para |aplicar un filtro a una variable o expresión, como esta: "nombre - capitalizar y - product.Presorce" redondo ((2) . También puedes encadenar varios filtros, como este: "nombre más" inferior, sustitúyase: "usuario", edise de huésco. Jinja2 proporciona muchos filtros incorporados que puede utilizar, como capitalizar, inferior, superior, trimrecortar, longitud, redondo, formato, escape, caja fuerte y mucho más. También puedes crear tus propios filtros personalizados si lo deseas.
    Condiciones: Puedes usar las condiciones para controlar qué parte de tu plantilla se representa en función de algunos criterios. Puedes usar las palabras clave de si, elif y de lo contrario para crear una declaración en tu plantilla, como esta: % si product.Prescidor 10 %, "% product.principia".{% else %} También puede utilizar las palabras de acceso y no en las palabras clave para comprobar si un valor está en una lista o en un diccionario, como este: "% si product.name en [Apple, "Banana", "Naranja" %" y "%" si product.name no en productos.keys() %.
    Bucles : Puede utilizar bucles para iterar sobre una secuencia de elementos en su plantilla. Puedes usar las palabras clave para y end para crear un bucle en tu plantilla, como esta: % para el producto en productos % y % para %. También puede utilizar la roya y continuar las palabras clave para controlar el flujo del bucle, así: "% romper %" y "% continuar %". También puede acceder a algunas variables especiales dentro del bucle, como loop.index, loop.first, loop.last, loop.length, y más.
    Macros : Puedes usar macros para definir bloques de código reutilizables en tu plantilla. Puedes usar las palabras clave macro y endmacro para crear una macro en tu plantilla, así: .% macro product.item(product) %' y .% endmacro %. También puede pasar argumentos y valores predeterminados a su macro, así: .% macro product.item.item (product, show-price=True) %. A continuación, puede llamar a su macro en cualquier lugar de su plantilla, así:: producto.item(product) y . producto .item . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Los Macros son útiles para crear componentes reutilizables y evitar la duplicación de código en su plantilla.

Aquí hay un ejemplo de un archivo de plantilla que utiliza algunas de las características y sintaxis de Jinja2 para personalizar la página web:

<html>
<head>
    <title>{{ title }}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <h1>Hello, {{ name | capitalize }}!</h1>
    <p>The current date and time is {{ datetime | format('%Y-%m-%d %H:%M:%S') }}.</p>
    <h2>Products</h2>
    <ul>
        {% for product in products %}
        <li>{{ product_item(product) }}</li>
        {% endfor %}
    </ul>
    {% macro product_item(product, show_price=True) %}
    <div class="product">
        <img src="{{ url_for('static', filename=product.image) }}" alt="{{ product.name }}">
        <h3>{{ product.name }}</h3>
        {% if show_price %}
        <p>Price: {{ product.price | round(2) }}</p>
        {% endif %}
    </div>
    {% endmacro %}
</body>
</html>

Y aquí hay un ejemplo de un PythonArchivo Python que utiliza el archivo de plantilla:
from flask import Flask, render_template
from datetime import datetime
 
app = Flask(__name__)
 
products = [
    {'name': 'Apple', 'price': 0.99, 'image': 'apple.png'},
    {'name': 'Banana', 'price': 0.79, 'image': 'banana.png'},
    {'name': 'Orange', 'price': 0.89, 'image': 'orange.png'}
]
 
@app.route('/')
def index():
    return render_template('index.html', title='Home', name='User', datetime=datetime.now(), products=products)
 
if __name__ == '__main__':
    app.run(debug=True)

Jinja2 es un potente motor de plantilla que permite personalizar sus plantillas con lógica y flujo de control. Puede utilizar Jinja2 para añadir condiciones, bucles, filtros, macros y otras características a sus plantillas, haciéndolos más flexibles y expresivos. También puede utilizar Jinja2 para crear diseños y herencias, que son características avanzadas que puede utilizar para crear una plantilla de base y extenderla a otras plantillas, evitando la duplicación de código y creando un aspecto y una sensación consistente para su aplicación web. Puede obtener más información sobre Jinja2 y sus características y sintaxis de la documentación oficial.


**** Cómo agregar la interactividad con JavaScript

JavaScript es un lenguaje de scripting que se ejecuta en el navegador y le permite añadir características dinámicas e interactivas a sus páginas web. Por ejemplo, puede utilizar JavaScript para manipular los elementos HTML, responder a los eventos de los usuarios, validar la entrada del usuario, comunicarse con el servidor y más.
