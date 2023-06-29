from flask import json, jsonify
from flask import Flask
from flask_basicauth import BasicAuth
from datetime import timedelta
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager

app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'usuario1'
app.config['BASIC_AUTH_PASSWORD'] = '123456'
basic_auth = BasicAuth(app)
app.config["JWT_SECRET_KEY"] = "super-secret"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=15)
jwt = JWTManager(app)


@app.route("/Token")
@basic_auth.required
def Token():
    access_token = create_access_token(identity=app.config['BASIC_AUTH_USERNAME'])
    return jsonify(access_token=access_token)


@app.route("/")
@jwt_required()
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
