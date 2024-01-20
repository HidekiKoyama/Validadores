from flask import Blueprint
from .Validadores import ValidarCPF

cpf_app = Blueprint("cpf", __name__)

@cpf_app.route("/cpf/<id>/", methods=["POST", "GET"])
def valid_cpf(id):
    cp = ValidarCPF(id)
    resul = ({"valid": cp.cpValidar()})
    return resul