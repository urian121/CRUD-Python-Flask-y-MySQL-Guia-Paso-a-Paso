
from flask import render_template
from app import app


@app.route('/agregar-nueva-materia/', methods=['GET', 'POST'])
def index():
    pass
    #return render_template('materias/index.html')