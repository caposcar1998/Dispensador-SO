from Proceso import Proceso
from Micro import Micro

class Despachador:


    oscar = Proceso("Proceso1",8,2,True)
    gio = Proceso("Proceso2",9,5,True)
    manuel = Proceso("Proceso3",3,6,True)

    micros = []
    procesos = []
    tBloqueo = None
    cambioContexto = None

    procesos.append(oscar)
    procesos.append(gio)
    procesos.append(manuel)

  
    def __init__(self, micros, procesos, tBloqueo, cambioContexto):
        self.micros=micros
        self.procesos=procesos
        self.tBloqueo=tBloqueo
        self.cambioContexto=cambioContexto



    def acomodarProcesosMayorAMenor(lista):
        lista.sort(key= lambda x: x.tiempoE, reverse=False)
        

    def definirQuantum(self):
        pass
    def definirBloqueo(self):
        pass
    def definirCambioContext(self):
        pass
    def tiempoDisponible(self):
        pass

    
   
   
