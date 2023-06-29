from flask import json
from flask import Flask
from flask_basicauth import BasicAuth

app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'usuario1'
app.config['BASIC_AUTH_PASSWORD'] = '123456'
basic_auth = BasicAuth(app)

@app.route("/")
@basic_auth.required
def Test():
    body = {
            "Nombres": "RICARDO ANTONIO",
            "Apellidos": "VALLADARES RENDEROS",
            "Documentos": [
                {
                    "TipoDocumento": "DUI",
                    "NumeroDocumento": "123456789-0"
                },
                {
                    "TipoDocumento": "PASAPORTE",
                    "NumeroDocumento": "A01234567"
                }
            ]
        }
    return app.response_class(response=json.dumps(body), mimetype='application/json')


if __name__ == "__main__":
    app.run()
