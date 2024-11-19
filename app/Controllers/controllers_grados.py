from flask import render_template
# Importando la aplicación Flask
from app import app
# from Config.database import connectionBD, obtener_conexion
from Functions.funciones import selectAll

        
@app.route('/grados/', methods=['GET'])
def grados():
    respuestaDB = selectAll("tbl_grados")
    return render_template('grados/index.html', data=respuestaDB)


@app.route('/editar-grado/<int:id>', methods=['GET'])
def viewEdit(id):
    print(id)
    return f"Editar {id}"
