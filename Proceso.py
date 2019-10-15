class Proceso:
    
    nombre = None
    tiempoE = None
    nBloqueos = None
    disponible = None
    tiempoBloqueo = None

    def vencimientoQuantum(self):
        venc = None
        return venc

    def __init__(self, nombre, tiempoE, nBloqueos, disponible):
        self.nombre = nombre
        self.tiempoE = tiempoE
        self.nBloqueos = nBloqueos
        self.disponible = disponible
        self.tiempoBloqueo = 2
        
