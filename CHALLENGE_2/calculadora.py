import heapq
from constantes import *

class CalculadoraDeRutas:
    def __init__(self, mapa):
        self.mapa = mapa

    def calcular_ruta(self, inicio, salida):

        # Diccionario de distancias inicializado en infinito
        dist = {
            (y, x): float('inf')
            for y in range(self.mapa.filas)
            for x in range(self.mapa.columnas)
        }
        dist[inicio] = 0

        padres = {}
        cola_p = [(0, inicio)]

        while cola_p:
            costo, actual = heapq.heappop(cola_p)
            if actual == salida:
                return self._reconstruir_ruta(padres, inicio, salida)
            
            # Si el costo actual es mayor que el registrado, lo salteamos
            if costo > dist[actual]:
                continue

            # Explorar vecinos
            for vecino in self.mapa.vecinos(actual):
                if not self.mapa.es_accesible(vecino):
                    continue

                nuevo_costo = costo + self.mapa.obtener_costo(vecino)
                if nuevo_costo < dist[vecino]:
                    dist[vecino] = nuevo_costo
                    padres[vecino] = actual
                    heapq.heappush(cola_p, (nuevo_costo, vecino))

        return None # si no hay ruta posible
    
    def _reconstruir_ruta(self, padres, inicio, salida):
        # Reconstruye la ruta final desde el diccionario padres
        ruta = []
        actual = salida
        while actual != inicio:
            ruta.append(actual)
            actual = padres.get(actual)
            if actual is None:
                return None
        
        ruta.append(inicio)
        ruta.reverse()
        return ruta