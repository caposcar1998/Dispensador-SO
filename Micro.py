class Micro:
    Pejecutados = []
    IdMicro = None
    tiempoInicial = None
    tiempoFinal = None
    disponible = None
    
    def __init__(self, Pejecutados, IdMicro):
        self.Pejecutados=Pejecutados
        self.IdMicro=IdMicro
        self.tiempoInicial = determinarInicial()
        self.tiempoFinal = determinarFinal()
        self.disponible= False

    def ejecutar(self):
        pass

    def determinarInicial(self):
        pass
    def determinarFinal(self):
        pass
