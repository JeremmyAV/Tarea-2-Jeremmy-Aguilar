from random import*

class Dado:
    caras=0
    rnd=Random(42)

    def __init__(self,numCaras):
        self.caras=numCaras

    def lanzar(self):
        return self.rnd.randint(1, self.caras)
