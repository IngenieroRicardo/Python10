from flask import json
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def Test():
    try:
        content = request.json
        print("Nombres: "+content['Nombres'])
        print("Apellidos: "+content['Apellidos'])
        print("Documentos: ")
        for recepcion in content['Documentos']:
            print("Documento:" + recepcion['NumeroDocumento'] + " TipoDocumento:" + recepcion['TipoDocumento'])
        return jsonify({"Dato": "JSON Leido", "Error": 0}), 200
    except:
        return jsonify({"Dato": "JSON no Valido", "Error": 1}), 401


if __name__ == "__main__":
    app.run()
