from constantes import *

class Mapa: 

   def __init__(self, filas, columnas): 
        self.filas = filas # self no es una palabra reservada
        self.columnas = columnas
        self.mapa = self._crear_mapa()

   def _crear_mapa(self):
        mapa = [[EDIFICIO for _ in range(self.columnas)] for _ in range(self.filas)]
        for f in range(self.filas):
            for c in range(self.columnas):
                if f % 3 == 0 or c % 3 == 0:
                    mapa[f][c] = LIBRE
        return mapa
    
   def mostrar(self):
       for filas in self.mapa:
          lista_vista = []
          for celda in filas:
            if celda == EDIFICIO:
               lista_vista.append(SIMBOLOS[EDIFICIO]())
            else:
               lista_vista.append(SIMBOLOS[celda])

          print(" ".join(lista_vista))

   def rango_permitido(self, coordenada):
       y, x = coordenada
       return 0 <= y < self.filas and 0 <= x < self.columnas
    
   def es_accesible(self, coordenada):
      y, x = coordenada
      return(
         self.rango_permitido(coordenada)
         and self.mapa[y][x] not in (EDIFICIO, OBSTACULO)
      )
       
   def obtener_costo(self, coordenada):
       y, x = coordenada
       celda = self.mapa[y][x]
       # obtener tipo de celda desde grid
       return COSTOS.get(celda, 1)
    
   def vecinos(self, coordenada):
       y, x = coordenada
       movimientos = [(1,0),(-1,0),(0,1),(0,-1)]
       for df, dc in movimientos:
          nf, nc = y + df, x + dc
          if self.rango_permitido((nf, nc)):
             yield (nf, nc)
          
   def marcar_inicio_salida(self, inicio, salida):
       y1, x1 = inicio
       y2, x2 = salida
       self.mapa[y1][x1] = INICIO
       self.mapa[y2][x2] = SALIDA

   def marcar_ruta(self, ruta, emoji):
       for (y, x) in ruta:
          if self.mapa[y][x] not in (INICIO, SALIDA, OBSTACULO):
             self.mapa[y][x] = emoji

   def agregar_agua(self, prob= 0.2):
      for f in range(self.filas):
          for c in range(self.columnas):
              if self.mapa[f][c] == LIBRE and random.random() < prob:
                  self.mapa[f][c] = AGUA

   def agregar_semaforos_en_ruta(self, ruta, cantidad=2):
       posiciones = [p for p in ruta if self.mapa[p[0]][p[1]] == RUTA_VERDE]
       semaforos = random.sample(posiciones, min(cantidad, len(posiciones)))
       for y, x in semaforos:
           self.mapa[y][x] = OBSTACULO
   
