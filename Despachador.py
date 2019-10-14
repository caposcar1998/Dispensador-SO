from Proceso import Proceso
from Micro import Micro

class Despachador:

    micros = []
    procesos = []
    tBloqueo = None
    cambioContexto = None
    def __init__(self, micros, procesos, tBloqueo, cambioContexto):
        self.micros=micros
        self.procesos=procesos
        self.tBloqueo=tBloqueo
        self.cambioContexto=cambioContexto

 
    def definirQuantum(self):
        pass
    def definirBloqueo(self):
        pass
    def definirCambioContext(self):
        pass
    def tiempoDisponible(self):
        pass
    #FUNCION MAIN
    def main(self):
        print("Funcion principal")

    if __name__ == "__main__":
        main()