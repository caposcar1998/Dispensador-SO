class Micro:
    procesos_ejecucion = []
    
    tiempoInicial = None
    tiempoFinal = None
    disponible = None
    
    def __init__(self, tiempoInicial, disponible):
        self.tiempoInicial = 0
        self.disponible= True

    def anadir_proceso(obj, procesos_ejecucion):
        procesos_ejecucion.append(obj)
        

    
