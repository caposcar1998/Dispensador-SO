class Proceso:
    
    nombre = None
    tiempo_disponible = 0 
    tiempo_cambio_contexto = 0
    tiempo_ejecucion = 0
    tiempo_vencimiento_quantum = 0
    tiempo_bloqueo = 0
    tiempo_total = 0
    tiempo_inicial = 0
    tiempo_final = 0

    

    def __init__(self, nombre,tiempo_ejecucion,tiempo_disponible , tiempo_bloqueo ):
        self.nombre=nombre
        self.tiempo_disponible= tiempo_disponible
        self.tiempo_ejecucion = tiempo_ejecucion
        self.tiempo_bloqueo= tiempo_bloqueo

        
    

    