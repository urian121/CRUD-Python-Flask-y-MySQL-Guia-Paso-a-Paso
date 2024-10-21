from flask import Flask, render_template, request, redirect, url_for
from Controllers.empleado_controller import listar_empleados, agregar_empleado, actualizar_empleado, eliminar_empleado

# Declarando nombre de la aplicación e inicializando, crear la aplicación Flask
# Creando una instancia de la aplicación Flask
# Creando una app instanciando la clase Flask (automáticamente el nombre de la app)
app = Flask(__name__,)
app.secret_key = '97110c78ae51a45af397befe'

# Rutas
configurar_rutas(app)


# Inicializando app
if __name__ == '__main__':
    app.run()