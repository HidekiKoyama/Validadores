from flask import Blueprint, jsonify
from .Validadores import ValidarCnpj

cnpj_app = Blueprint("cnpj", __name__)

@cnpj_app.route("/cnpj/<id>/",methods=["POST", "GET"])
def valid_cnpj(id):
    cn = ValidarCnpj(id)
    resul =  ({"valid" : cn.cnValidar()})
    return jsonify(resul)