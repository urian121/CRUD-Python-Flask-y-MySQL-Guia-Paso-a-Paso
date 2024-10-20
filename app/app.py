from flask import Flask, render_template, request, redirect, url_for
from Controllers.empleado_controller import listar_empleados, agregar_empleado, actualizar_empleado, eliminar_empleado

app = Flask(__name__)

# Rutas principales
@app.route('/')
def index():
    return listar_empleados()

@app.route('/crear', methods=['GET', 'POST'])
def crear():
    return agregar_empleado()

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    return actualizar_empleado(id)

@app.route('/eliminar/<int:id>')
def eliminar(id):
    return eliminar_empleado(id)

if __name__ == '__main__':
    app.run(debug=True)
