from flask import redirect, render_template, url_for
from app import app # Importando la aplicación Flask


@app.route('/')
def inicio():
    return render_template('base.html')


# Redireccionando cuando la página no existe
@app.errorhandler(404)
def not_found(error):
        return redirect(url_for('inicio'))
    
@app.route('/materias/')
def materias():
    return render_template('materias/index.html')


@app.route('/profesores/')
def profesores():
    return render_template('profesores/index.html')


@app.route('/estudiantes/')
def estudiantes():
    return render_template('estudiantes/index.html')