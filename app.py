from flask import Flask, request, jsonify
from ludo import lanzar_dado, realizar_movimiento, obtener_estado, jugar_maquina, jugador_usuario, jugador_maquina, turno

app = Flask(__name__)

@app.route("/estado", methods=["GET"])
def estado():
    estado_juego = obtener_estado()
    return jsonify(estado_juego)

@app.route("/lanzar_dado", methods=["POST"])
def lanzar_dado_endpoint():
    dado = lanzar_dado()
    estado_juego = obtener_estado()
    return jsonify({"dado": dado, **estado_juego})

@app.route("/mover", methods=["POST"])
def mover():
    data = request.get_json()
    jugador = data.get("jugador")
    ficha = data.get("ficha")
    
    if jugador not in ["A", "B"] or ficha not in [1, 2]:
        return jsonify({"error": "Datos inválidos"}), 400
    
    # Realizar el movimiento del jugador
    resultado = realizar_movimiento(jugador, ficha)
    if "error" in resultado:
        return jsonify(resultado), 400
    
    # Si el siguiente turno es de la máquina, la máquina juega automáticamente
    if turno == 1 and jugador_maquina == "B":
        ficha_maquina = jugar_maquina()
        estado_juego = obtener_estado()
        return jsonify({
            "dado_jugador": resultado["dado"],
            "ficha_maquina": ficha_maquina,
            **estado_juego
        })
    
    estado_juego = obtener_estado()
    return jsonify({**resultado, **estado_juego})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
