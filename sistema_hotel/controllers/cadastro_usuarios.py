"""Modulo para as rotas de login."""
from flask import (
    Blueprint,
    redirect,
    render_template,
    request,
    session,
    url_for
)

app = Blueprint('cadastro_usuarios', __name__)


@app.route('/', methods=['GET'])
def view():
    return render_template('Cadastro_Usuarios.html')
