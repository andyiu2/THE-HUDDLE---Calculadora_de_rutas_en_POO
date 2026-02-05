import random

LIBRE = 0
EDIFICIO = 1
AGUA = 2
OBSTACULO = 3
INICIO = 4
SALIDA = 5
RUTA_VERDE = 6
RUTA_NARANJA = 7

EDIFICIOS = ["🏢", "🏦", "🏨"]

SIMBOLOS ={
    LIBRE: "⬛",
    EDIFICIO: lambda: random.choice(EDIFICIOS),
    AGUA: "🟦",
    OBSTACULO: "🚦",
    INICIO: "🟢",
    SALIDA: "🔴",
    RUTA_VERDE: "🟩",
    RUTA_NARANJA: "🟧"
}

COSTOS = {
    LIBRE: 1,
    AGUA: 5,
    RUTA_VERDE: 2,
    RUTA_NARANJA: 2,
    INICIO: 0,
    SALIDA: 0,
    OBSTACULO: float('inf'),
    EDIFICIO: float('inf')
}