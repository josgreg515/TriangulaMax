from flask import Flask, request, jsonify
from flask_cors import CORS
import ccxt

app = Flask(__name__)
CORS(app) # Esto permite que tu web en Vercel hable con este servidor

@app.route('/ejecutar-arbitraje', methods=['POST'])
def ejecutar():
    datos = request.json
    estrategia = datos.get('estrategia')
    par = datos.get('par')
    
    # Aquí es donde el Centinela despierta
    print(f"Orden recibida: {estrategia} para el par {par}")
    
    # Simulación de ejecución exitosa
    return jsonify({
        "status": "success",
        "mensaje": f"Centinela J.G.T. ejecutando {estrategia} en {par}",
        "ganancia_estimada": "1.45%"
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
