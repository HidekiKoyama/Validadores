from flask import Flask
from api import cnpj_app, cpf_app

app = Flask(__name__)

app.register_blueprint(cnpj_app)
app.register_blueprint(cpf_app)

if __name__ == "__main__":
    app.run(debug=False)