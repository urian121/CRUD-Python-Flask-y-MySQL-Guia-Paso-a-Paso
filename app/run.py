# Importando del archivo application app
from application import app


# Ejecutando el objeto Flask
# Arrancando mi Aplicacion
# Condicional de que si la aplicación ejecutada se coincide al nombre de la aplicación
if __name__ == '__main__':
    # Método que inicia la app con la dirección, puertos y modo de argumentos
    app.run('127.0.0.1', port=5000, debug=True)
