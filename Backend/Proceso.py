class Proceso:
    
    nombre = None
    tiempo_disponible = None 
    tiempo_cambio_contexto = None
    tiempo_ejecucion = None
    tiempo_vencimiento_quantum = None
    tiempo_bloqueo = None
    tiempo_total = None
    tiempo_inicial = None
    tiempo_final = None

    

    def __init__(self, nombre,tiempo_ejecucion,tiempo_disponible , tiempo_bloqueo ):
        self.nombre=nombre
        self.tiempo_disponible= tiempo_disponible
        self.tiempo_ejecucion = tiempo_ejecucion
        self.tiempo_bloqueo= tiempo_bloqueo

        
    

    