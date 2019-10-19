from Proceso import Proceso
from Micro import Micro
import math

class Despachador:
  
    micros = []
    procesos_a_ejecutar = []



    def determinar_tiempo_vencimiento_quantum(self, obj, quantum, cambioContexto):
        obj.tiempo_vencimiento_quantum =  (math.ceil((obj.tiempo_ejecucion/quantum)-1)*cambioContexto)
        print(obj.tiempo_vencimiento_quantum)
        print(" paso determinar_tiempo_vencimiento_quantum")


    def determinar_tiempo_cambio_contexto(self, obj, valor):
        obj.tiempo_cambio_contexto = valor
        print(obj.tiempo_cambio_contexto)
        print(" paso determinar_tiempo_cambio_contexto")


    def determinar_tiempo_bloqueo(self, obj,tBloqueo):
        obj.tiempo_bloqueo =  obj.tiempo_bloqueo*tBloqueo
        print(obj.tiempo_bloqueo)
        print("paso determinar_tiempo_bloqueo")


    def determinar_tiempo_inicial(self, obj,procesos_a_ejecutar):
        for i in range(0, len(procesos_a_ejecutar)):
            if (procesos_a_ejecutar[i] == procesos_a_ejecutar[0]):
                procesos_a_ejecutar[i].tiempo_inicial  = 0
                print(procesos_a_ejecutar[i].tiempo_inicial)
                break
            else:
                procesos_a_ejecutar[i].tiempo_inicial = procesos_a_ejecutar[i-1].tiempo_final
                print(procesos_a_ejecutar[i].tiempo_inicial)
                break
        print("paso determinar_tiempo_inicial")


    def determinar_tiempo_total(self, obj):
        obj.tiempo_total=  obj.tiempo_ejecucion+obj.tiempo_vencimiento_quantum+obj.tiempo_bloqueo+obj.tiempo_cambio_contexto
        print(obj.tiempo_total)
        print("paso determinar_tiempo_total")


    def determinar_tiempo_final(self, obj, procesos_a_ejecutar):
        print("Lelga al meotdo")
        obj.tiempo_final = obj.tiempo_inicial+ obj.tiempo_total
        print( obj.tiempo_final)
        print("paso determinar_tiempo_final")


    def determinar_tiempo_ejecucion_micro(self, obj1, obj2):
        obj1.tiempoEjecucion += obj2.tiempo_final
        print("paso determinar_tiempo_ejecucion_micro")