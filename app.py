from flask import Flask, request, jsonify
from ludo import realizar_movimiento, obtener_estado

app = Flask(__name__)

@app.route("/estado", methods=["GET"])
def estado():
    estado_juego = obtener_estado()
    return jsonify(estado_juego)

@app.route("/mover", methods=["POST"])
def mover():
    data = request.get_json()
    jugador = data.get("jugador")
    ficha = data.get("ficha")
    if jugador not in ["A", "B"] or ficha not in [1, 2]:
        return jsonify({"error": "Datos inválidos"}), 400
    dado = realizar_movimiento(jugador, ficha)
    estado_juego = obtener_estado()
    return jsonify({"dado": dado, **estado_juego})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
