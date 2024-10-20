from flask import Blueprint
from Controllers.empleado_controller import listar_empleados, agregar_empleado

empleado_bp = Blueprint('empleado', __name__)

# Rutas
@empleado_bp.route('/')
def index():
    return listar_empleados()

@empleado_bp.route('/crear', methods=['GET', 'POST'])
def crear():
    return agregar_empleado()

# Otras rutas como actualizar y eliminar irán aquí...
