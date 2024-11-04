# Aquí puedes centralizar los importes de rutas para mejorar la estructura.

# Declarando nombre de la aplicación e inicializando, crear la aplicación Flask
from app import app
    
# Esto carga todas las rutas dentro de la carpeta Routers
import Routers as Routers 


"""
Al usar import Controllers as app_controllers, 
estás creando un alias para el módulo Controllers,
lo que te permitirá acceder a sus contenidos de manera más clara y concisa en tu código.
"""
import Controllers as app_controllers

# # Ejecutando el objeto Flask, Arrancando mi Aplicacion de Flask
if __name__ == '__main__':
    # Método que inicia la app con la dirección, puertos y modo de argumentos
    app.run('127.0.0.1', port=5000, debug=True)
