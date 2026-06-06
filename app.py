from flask import Flask, request, jsonify
import os
import re
import re
from collections import Counter

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Servidor funcionando"

@app.route("/analizar", methods=["POST"])
def analizar():

    datos = request.get_json()
    
    title = datos.get("title", "")
    content = datos.get("content", "")
    image = datos.get("image", "")
    url = datos.get("url", "")

    texto = title + " " + content

    riesgo = 0
    razones = []

    texto_lower = texto.lower()

    exclamaciones = texto.count("!!") + texto.count("¡¡")
    if exclamaciones > 3:
         riesgo += 10
         razones.append("demasiados signos de exclamación")
    
    palabras_mayus = re.findall(r'\b[A-ZÁÉÍÓÚÑ]{3,}\b', texto)
    if len(palabras_mayus) > 5:
        riesgo += 7
        razones.append("Uso excesivo de mayúsculas")

    to titular_sensacionalista = ["urgente", "alerta", "impactante", "increíble", "escandaloso", "épico", "alucinante", "no creerás", "nadie sabía", "cambia todo", "cambiará todo", "inimaginable", "indignante", "alarmante","última hora", "polémico"., "controversial", "terrible", "te sorprenderá", "rompe internet", "tendencia", "viral", "conspiración", "lo que no te cuentan", "revolucionario", "el lado oculto", "te están engañando", "debes saberlo", "insóliro", "jamás visto"]
    title_lower = title.lower()

    coincidencias_titulo = 0 
     
    for palabra_titulo in titular_sensacionalista:
        if palabra in title_lower:
            coincidencias_titulo += 1
            razones.append(f"Título sensacionalista: {palabra_titulo}")

    if coincidencias_titulo == 1:
        riesgo += 5
    elif coincidencias_titulo == 2:
        riesgo += 10
    elif coincidencias_titulo >= 3:
        riesgo += 15

    lexico_valorativo = {
        "axiologico_postivo": 
        "axiologico_negativo":
        "axiologico_sensacionalista":
        "axiologico_emoional":
        "axiologico_absoluto":

class EvaluadorLexico:
        def __init__(self, lexico_valorativo):
            self.lexico_valorativo = lexico_valorativo
        def separar_texto(self, content):
           return re.findall(r"\b\w+\b", content.lower())
        def analizar(self, content):
            texto_separado = self.separar_texto(content)
            frecuencia = Counter(texto_separado)

            resultados = {}
            for categoria, lista_palabras in self.lexico_valorativo.items():
                puntaje = sum(frecuencia[palabra] for palabra in lista_palabras if palabra in frecuencia)
                resultados[categoria] = puntaje / len(texto_separado) if texto_separado else 0


    content_lower = content.lower()

    concidencias_content = 0

    for palabra_content in lexico_valorativo:
        if palabra in content_lower:
            coincidencias_content+= 1
            razones.append(f"Léxico valorativo: {palabra_content]")
    
    return jsonify({
        "resultado": f"Recibi este texto: {texto}"
    })

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )
