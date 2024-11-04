from flask import render_template
from app import app


@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/cursos/')
def cursos():
    return render_template('cursos/index.html')


@app.route('/materias/')
def materias():
    return render_template('materias/index.html')


@app.route('/profesores/')
def profesores():
    return render_template('profesores/index.html')


@app.route('/estudiantes/')
def estudiantes():
    return render_template('estudiantes/index.html')