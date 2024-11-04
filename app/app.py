# Este archivo inicializa la aplicación y puede también cargar la configuración global.
from flask import Flask

app = Flask(__name__)
application = app
app.secret_key = '97110c78ae51a45af397b6008f90b23a50fe'

