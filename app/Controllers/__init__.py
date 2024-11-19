"""
El __init__.py dentro de Controllers está configurado para importar cada controlador específico (Controllers_Cursos, Controllers_Estudiantes, etc.),
lo cual permite que todos se carguen automáticamente cuando importas el paquete Controllers.
"""

from .controllers_grados import *
from .controllers_estudiantes import *
from .controllers_materias import *
from .controllers_profesores import *

