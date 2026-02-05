from mapa import Mapa
from calculadora import CalculadoraDeRutas
from constantes import *

def pedir_coordenada(mapa, mensaje, reservadas= set()):
    while True:
        try:
            y, x = map(int, input(mensaje).split(","))
            coord = (y, x)
        except ValueError:
            print("Formato inválido. Usa fila,columna (ej: 3,5)."); continue
        
        if coord in reservadas:
            print("Esa coordenada ya fue utilizada. Intente con otra"); continue
        
        if not mapa.es_accesible(coord):
            print("Fuera de rango o no transitable, intente de nuevo"); continue
        
        return coord

def pedir_tamaño(mensaje):
    while True:
        try:
            tamaño = int(input(mensaje))
            return tamaño
        except ValueError:
            print("Formato invalido, ingrese numeros")
    

def main():

    filas = pedir_tamaño("Ingrese la cantidad de filas: ")
    columnas = pedir_tamaño("Ingrese la cantidad de columnas: ")

    mapa = Mapa(filas, columnas)
    mapa.mostrar()

    inicio = pedir_coordenada(mapa, "Ingrese la coordenada de inicio (y, x): ")
    salida = pedir_coordenada(mapa, "Ingrese la coordenada de salida (y, x): ", reservadas={inicio})
    mapa.marcar_inicio_salida(inicio, salida)
    mapa.mostrar()

    calculadora = CalculadoraDeRutas(mapa)
    ruta = calculadora.calcular_ruta(inicio, salida)

    if ruta:
        print("Ruta encontrada")
        mapa.marcar_ruta(ruta, RUTA_VERDE)
        mapa.mostrar()
    else:
        print("No hay ruta posible")

    obs = input("Desea añadir obstaculos? (s/n): ").lower()
    if obs == "s":
        mapa.agregar_agua(prob=0.2)
        mapa.agregar_semaforos_en_ruta(ruta, 2)
        mapa.marcar_ruta(ruta, RUTA_NARANJA)
        print("Obstaculos añadidos 🚧")
        mapa.mostrar()

        input("Presione enter para recalcular la ruta...")

        nueva_ruta = calculadora.calcular_ruta(inicio, salida)
        if nueva_ruta:
            mapa.marcar_ruta(nueva_ruta, RUTA_VERDE)
            print("Nueva ruta recalculada con exito")
            mapa.mostrar()
        else:
            print("No hay nueva ruta posible")

if __name__ == "__main__":
    main()