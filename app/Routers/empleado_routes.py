from flask import Blueprint
from Controllers.empleado_controller import listar_empleados, agregar_empleado



# Creando mi Decorador para el Home
@app.route('/')
def hello():
    return 'Hello, World!'

    
@app.route('/')
def index():
    # return render_template('index.html')
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


#Redireccionando cuando la página no existe
@app.errorhandler(404)
def not_found(error):
        return redirect(url_for('inicio'))