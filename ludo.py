import random

# Estado inicial del juego
tablero = ["█"] * 50
posicion_jugador_A1 = 0  # Ficha 1 del Jugador A
posicion_jugador_A2 = 0  # Ficha 2 del Jugador A
posicion_jugador_B1 = 49  # Ficha 1 del Jugador B
posicion_jugador_B2 = 49  # Ficha 2 del Jugador B
jugador_usuario = "A"  # Jugador controlado por el usuario
jugador_maquina = "B"  # Jugador controlado por la máquina
turno = 0  # 0 para Jugador A, 1 para Jugador B
ultimo_dado = None  # Almacena el resultado del último lanzamiento de dado

# Función para mostrar el tablero
def mostrar_tablero():
    tablero_display = tablero.copy()
    if posicion_jugador_A1 < 50:
        tablero_display[posicion_jugador_A1] = "🔴"  # Ficha 1 del Jugador A
    if posicion_jugador_A2 < 50:
        tablero_display[posicion_jugador_A2] = "🔶"  # Ficha 2 del Jugador A
    if posicion_jugador_B1 >= 0:
        tablero_display[posicion_jugador_B1] = "🔵"  # Ficha 1 del Jugador B
    if posicion_jugador_B2 >= 0:
        tablero_display[posicion_jugador_B2] = "🔷"  # Ficha 2 del Jugador B
    return " ".join(tablero_display)

# Función para lanzar el dado
def lanzar_dado():
    global ultimo_dado
    ultimo_dado = random.randint(1, 6)
    return ultimo_dado

# Función para verificar si una casilla está ocupada por el oponente
def casilla_ocupada_por_oponente(posicion, jugador):
    if jugador == "A":
        return posicion == posicion_jugador_B1 or posicion == posicion_jugador_B2
    elif jugador == "B":
        return posicion == posicion_jugador_A1 or posicion == posicion_jugador_A2
    return False

# Función para "matar" una ficha del oponente
def matar_ficha_oponente(posicion, jugador):
    global posicion_jugador_A1, posicion_jugador_A2, posicion_jugador_B1, posicion_jugador_B2
    if jugador == "A":
        if posicion == posicion_jugador_B1:
            posicion_jugador_B1 = 49  # Regresa a la casa
        elif posicion == posicion_jugador_B2:
            posicion_jugador_B2 = 49  # Regresa a la casa
    elif jugador == "B":
        if posicion == posicion_jugador_A1:
            posicion_jugador_A1 = 0  # Regresa a la casa
        elif posicion == posicion_jugador_A2:
            posicion_jugador_A2 = 0  # Regresa a la casa

# Función para mover una ficha del Jugador A
def mover_jugador_A(ficha, dado):
    global posicion_jugador_A1, posicion_jugador_A2
    if ficha == 1:
        nueva_posicion = posicion_jugador_A1 + dado
        if nueva_posicion >= 50:
            nueva_posicion = 49  # Límite del tablero
        if casilla_ocupada_por_oponente(nueva_posicion, "A"):
            matar_ficha_oponente(nueva_posicion, "A")
        posicion_jugador_A1 = nueva_posicion
    elif ficha == 2:
        nueva_posicion = posicion_jugador_A2 + dado
        if nueva_posicion >= 50:
            nueva_posicion = 49  # Límite del tablero
        if casilla_ocupada_por_oponente(nueva_posicion, "A"):
            matar_ficha_oponente(nueva_posicion, "A")
        posicion_jugador_A2 = nueva_posicion

# Función para mover una ficha del Jugador B
def mover_jugador_B(ficha, dado):
    global posicion_jugador_B1, posicion_jugador_B2
    if ficha == 1:
        nueva_posicion = posicion_jugador_B1 - dado
        if nueva_posicion < 0:
            nueva_posicion = 0  # Límite del tablero
        if casilla_ocupada_por_oponente(nueva_posicion, "B"):
            matar_ficha_oponente(nueva_posicion, "B")
        posicion_jugador_B1 = nueva_posicion
    elif ficha == 2:
        nueva_posicion = posicion_jugador_B2 - dado
        if nueva_posicion < 0:
            nueva_posicion = 0  # Límite del tablero
        if casilla_ocupada_por_oponente(nueva_posicion, "B"):
            matar_ficha_oponente(nueva_posicion, "B")
        posicion_jugador_B2 = nueva_posicion

# Función para verificar si alguien ha ganado
def verificar_ganador():
    if posicion_jugador_A1 == 49 and posicion_jugador_A2 == 49:
        return "¡Jugador A ha ganado!"
    elif posicion_jugador_B1 == 0 and posicion_jugador_B2 == 0:
        return "¡Jugador B ha ganado!"
    return None

# Función para realizar un movimiento
def realizar_movimiento(jugador, ficha):
    global turno
    if ultimo_dado is None:
        return {"error": "Primero debes lanzar el dado."}
    if jugador == "A":
        mover_jugador_A(ficha, ultimo_dado)
    elif jugador == "B":
        mover_jugador_B(ficha, ultimo_dado)
    turno = 1 - turno  # Cambia el turno
    return {"dado": ultimo_dado, "ficha": ficha}

# Función para que la máquina juegue
def jugar_maquina():
    ficha = random.choice([1, 2])  # La máquina elige una ficha aleatoria
    realizar_movimiento(jugador_maquina, ficha)
    return ficha

# Función para obtener el estado actual del juego
def obtener_estado():
    return {
        "tablero": mostrar_tablero(),
        "posiciones": {
            "A1": posicion_jugador_A1,
            "A2": posicion_jugador_A2,
            "B1": posicion_jugador_B1,
            "B2": posicion_jugador_B2,
        },
        "turno": "A" if turno == 0 else "B",
        "ganador": verificar_ganador(),
    }
