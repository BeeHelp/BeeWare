from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Servidor funcionando"

@app.route("/analizar", methods=["POST"])
def analizar():

    datos = request.get_json()

    texto = datos["texto"]

    return jsonify({
        "resultado": f"Recibi este texto: {texto}"
    })

app.run()
