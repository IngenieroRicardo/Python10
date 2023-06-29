from flask import json
from flask import Flask

app = Flask(__name__)

@app.route("/")
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
