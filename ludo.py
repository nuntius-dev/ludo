import random
import time

# Tablero inicial (50 casillas)
tablero = ["█"] * 50

# Posiciones iniciales de las fichas
posicion_jugador_A1 = 0  # Ficha 1 del Jugador A (inicia en la posición 0)
posicion_jugador_A2 = 0  # Ficha 2 del Jugador A (inicia en la posición 0)
posicion_jugador_B1 = 49  # Ficha 1 del Jugador B (inicia en la posición 49)
posicion_jugador_B2 = 49  # Ficha 2 del Jugador B (inicia en la posición 49)

# Función para mostrar el tablero
def mostrar_tablero():
    tablero_display = tablero.copy()
    # Colocar las fichas en el tablero
    if posicion_jugador_A1 < 50:
        tablero_display[posicion_jugador_A1] = "🟥"  # Ficha 1 del Jugador A
    if posicion_jugador_A2 < 50:
        tablero_display[posicion_jugador_A2] = "🔶"  # Ficha 2 del Jugador A
    if posicion_jugador_B1 >= 0:
        tablero_display[posicion_jugador_B1] = "🔵"  # Ficha 1 del Jugador B
    if posicion_jugador_B2 >= 0:
        tablero_display[posicion_jugador_B2] = "🔷"  # Ficha 2 del Jugador B
    # Mostrar el tablero
    print("Tablero:", " ".join(tablero_display))
    print()

# Función para lanzar el dado
def lanzar_dado():
    return random.randint(1, 6)

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
            print("¡Jugador A ha matado la Ficha 1 del Jugador B!")
            posicion_jugador_B1 = 49  # Regresa a la casa
        elif posicion == posicion_jugador_B2:
            print("¡Jugador A ha matado la Ficha 2 del Jugador B!")
            posicion_jugador_B2 = 49  # Regresa a la casa
    elif jugador == "B":
        if posicion == posicion_jugador_A1:
            print("¡Jugador B ha matado la Ficha 1 del Jugador A!")
            posicion_jugador_A1 = 0  # Regresa a la casa
        elif posicion == posicion_jugador_A2:
            print("¡Jugador B ha matado la Ficha 2 del Jugador A!")
            posicion_jugador_A2 = 0  # Regresa a la casa

# Función para mover una ficha del Jugador A
def mover_jugador_A(ficha, dado):
    global posicion_jugador_A1, posicion_jugador_A2
    if ficha == 1:
        nueva_posicion = posicion_jugador_A1 + dado
        if nueva_posicion >= 50:
            nueva_posicion = 49  # Límite del tablero
        # Verificar si la nueva posición está ocupada por el oponente
        if casilla_ocupada_por_oponente(nueva_posicion, "A"):
            matar_ficha_oponente(nueva_posicion, "A")
        posicion_jugador_A1 = nueva_posicion
        print(f"Jugador A (Ficha 1) se movió a la posición {posicion_jugador_A1}.")
    elif ficha == 2:
        nueva_posicion = posicion_jugador_A2 + dado
        if nueva_posicion >= 50:
            nueva_posicion = 49  # Límite del tablero
        # Verificar si la nueva posición está ocupada por el oponente
        if casilla_ocupada_por_oponente(nueva_posicion, "A"):
            matar_ficha_oponente(nueva_posicion, "A")
        posicion_jugador_A2 = nueva_posicion
        print(f"Jugador A (Ficha 2) se movió a la posición {posicion_jugador_A2}.")

# Función para mover una ficha del Jugador B
def mover_jugador_B(ficha, dado):
    global posicion_jugador_B1, posicion_jugador_B2
    if ficha == 1:
        nueva_posicion = posicion_jugador_B1 - dado
        if nueva_posicion < 0:
            nueva_posicion = 0  # Límite del tablero
        # Verificar si la nueva posición está ocupada por el oponente
        if casilla_ocupada_por_oponente(nueva_posicion, "B"):
            matar_ficha_oponente(nueva_posicion, "B")
        posicion_jugador_B1 = nueva_posicion
        print(f"Jugador B (Ficha 1) se movió a la posición {posicion_jugador_B1}.")
    elif ficha == 2:
        nueva_posicion = posicion_jugador_B2 - dado
        if nueva_posicion < 0:
            nueva_posicion = 0  # Límite del tablero
        # Verificar si la nueva posición está ocupada por el oponente
        if casilla_ocupada_por_oponente(nueva_posicion, "B"):
            matar_ficha_oponente(nueva_posicion, "B")
        posicion_jugador_B2 = nueva_posicion
        print(f"Jugador B (Ficha 2) se movió a la posición {posicion_jugador_B2}.")

# Función para verificar si alguien ha ganado
def verificar_ganador():
    if posicion_jugador_A1 == 49 and posicion_jugador_A2 == 49:
        print("¡Jugador A ha ganado!")
        return True
    elif posicion_jugador_B1 == 0 and posicion_jugador_B2 == 0:
        print("¡Jugador B ha ganado!")
        return True
    return False

# Función principal del juego
def jugar():
    # Preguntar al usuario qué jugador quiere ser
    jugador_usuario = input("¿Quieres ser el Jugador A o el Jugador B? (A/B): ").upper()
    while jugador_usuario not in ["A", "B"]:
        jugador_usuario = input("Por favor, elige A o B: ").upper()

    turno = 0  # 0 para Jugador A, 1 para Jugador B
    while True:
        mostrar_tablero()
        dado = lanzar_dado()
        print(f"El dado ha salido: {dado}")
        time.sleep(2)  # Espera 2 segundos para simular el lanzamiento

        if turno == 0:
            if jugador_usuario == "A":
                ficha = int(input("Elige la ficha a mover (1 o 2): "))
                while ficha not in [1, 2]:
                    ficha = int(input("Por favor, elige 1 o 2: "))
                mover_jugador_A(ficha, dado)
            else:
                ficha = random.choice([1, 2])  # La máquina elige aleatoriamente
                mover_jugador_A(ficha, dado)
        else:
            if jugador_usuario == "B":
                ficha = int(input("Elige la ficha a mover (1 o 2): "))
                while ficha not in [1, 2]:
                    ficha = int(input("Por favor, elige 1 o 2: "))
                mover_jugador_B(ficha, dado)
            else:
                ficha = random.choice([1, 2])  # La máquina elige aleatoriamente
                mover_jugador_B(ficha, dado)

        if verificar_ganador():
            break
        
        turno = 1 - turno  # Cambia el turno

# Iniciar el juego
print("¡Bienvenido al juego!")
jugar()
