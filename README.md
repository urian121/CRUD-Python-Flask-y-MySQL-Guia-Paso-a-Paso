# CRUD con Python 🐍 Flask y MySQL - Guía Paso a Paso 🚀

En este proyecto, aprenderás a desarrollar un sistema **CRUD** utilizando Python 🐍, Flask y MySQL. Esta guía te llevará paso a paso en la creación de aplicaciones interactivas, con la capacidad de gestionar empleados de manera eficiente.

Estructura de carpetas: Ya tienes carpetas organizadas para templates, static, Routers, Controllers y Config, lo cual es excelente. Esto hace que el proyecto sea más modular y fácil de escalar.


## Funcionalidades Principales:

- **Crear**: Añadir nuevos empleados.
- **Leer**: Consultar información de empleados.
- **Actualizar**: Modificar datos de empleados existentes.
- **Eliminar**: Borrar registros de empleados.

### Otros aspectos cubiertos:
- Establecer la **conexión entre Python y MySQL**.
- Crear un **panel de administración** y un **panel para empleados**.
- Gestionar **roles y permisos**.
- Generar **reportes en Excel**.
- ¡Y mucho más!

## Requisitos

- Python 3.x (Descárgalo desde [aquí](https://www.python.org/downloads/)).
  - Asegúrate de marcar la casilla **Add Python 3.x to PATH** al instalar.
- MySQL (Gestor de Base de Datos Relacional) (Descárgalo desde [aquí](https://dev.mysql.com/downloads/installer/)).
- `pip` (Instalador de paquetes de Python) (Descárgalo desde [aquí](https://pypi.org/project/pip/)).

## Verificar versiones:

- **Python**:
  ```bash
  python --version   # En Windows
  python3 --version  # En Mac/Linux
  ```

- **Pip**:
  ```bash
  pip --version   # En Windows
  pip3 --version  # En Mac/Linux
  ```

## Actualizar `pip`
Es recomendable mantener `pip` actualizado. Ejecuta el siguiente comando según tu sistema operativo:

- **Windows**:
  ```bash
  python -m pip install --upgrade pip
  ```

- **Mac/Linux**:
  ```bash
  python3 -m pip install --upgrade pip
  ```

## Preparación del entorno de desarrollo

### Paso 1: Crear un entorno virtual

- **Opción 1**: Usar `virtualenv` (Instalarlo si no lo tienes).
  ```bash
  pip install virtualenv    # Instalar virtualenv
  virtualenv env            # Crear el entorno virtual
  ```

- **Opción 2**: Usar el módulo `venv` que viene por defecto en Python.
  ```bash
  python -m venv env        # En Windows
  python3 -m venv env       # En Mac/Linux
  ```

### Paso 2: Activar el entorno virtual

- **Windows**:
  ```bash
  . env/Scripts/activate
  ```

- **Mac/Linux**:
  ```bash
  source env/bin/activate
  ```

Cuando el entorno esté activo, verás el nombre del entorno virtual al inicio de la línea de comandos, por ejemplo: `(env) C:\ruta\proyecto>`.

Para desactivar el entorno virtual:
```bash
deactivate
```

### Paso 3: Instalar Flask
Con el entorno virtual activo, instala Flask:
```bash
pip install flask
```

### Paso 4: Instalar el conector MySQL para Python
Instala el driver necesario para conectar Python con MySQL:
```bash
pip install mysql-connector-python
```

### Paso 5: Listar los paquetes instalados
Para ver los paquetes instalados en tu entorno:
```bash
pip list
```

### Generar el archivo `requirements.txt`
Este archivo contendrá todas las dependencias del proyecto:
```bash
pip freeze > requirements.txt
```

### Paso 6: Instalar dependencias desde `requirements.txt`
Para instalar todas las dependencias necesarias:
```bash
pip install -r requirements.txt
```

---

¡Ahora estás listo para iniciar el desarrollo del proyecto CRUD con Python y Flask! 🎉

## Crear la Estructura de un Proyecto Flask 🚀

Flask es un popular microframework de Python que permite construir y ejecutar aplicaciones web de forma sencilla. Al ser un microframework, proporciona lo esencial para empezar, pero es lo suficientemente flexible como para que puedas agregar más funcionalidades según tus necesidades.
Estructura Básica de un Proyecto Flask

Flask no impone una estructura de carpetas estricta, lo que te da la libertad de organizar tu proyecto como prefieras. Sin embargo, hay dos carpetas clave que Flask espera encontrar:

1. Carpeta static

En esta carpeta se almacenan todos los archivos estáticos de tu aplicación, tales como:

  - Imágenes
  - Hojas de estilo (CSS)
  - Scripts JavaScript (JS)
  - Otros activos como fuentes o archivos descargables
- Ejemplo de la carpeta:

    /static
      /css
      /js
      /images

2. Carpeta templates

Esta carpeta contendrá todos los archivos HTML que forman parte de tu aplicación. Flask utilizará estos archivos para renderizar vistas y devolver contenido dinámico.

Ejemplo de la carpeta:

  /templates
      index.html
      about.html
      layout.html

Estructura Básica Recomendada

Un ejemplo de estructura para un proyecto Flask simple podría verse así:

  /mi_proyecto_flask
    /static
        /css
        /js
        /images
    /templates
        base.html
        index.html
    app.py
    config.py
    requirements.txt

Explicación:

    app.py: El archivo principal de la aplicación donde defines las rutas y lógica principal de tu aplicación Flask.
    config.py: Archivo opcional para configuraciones de la aplicación (bases de datos, claves secretas, etc.).
    requirements.txt: Archivo que contiene todas las dependencias que necesita el