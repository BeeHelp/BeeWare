from flask import Flask, request, jsonify
import os

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

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )
