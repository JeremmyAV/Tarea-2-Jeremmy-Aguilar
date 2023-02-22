from dado import *


class Ficha:

    dado = Dado(6)
    color = ""
    posicion = 0

    def __init__(self,color2):
        self.color=color2
        self.posicion=0

    def avanzar(self):
        pasos = self.dado.lanzar()
        self.posicion += pasos
        print(self.posicion)
