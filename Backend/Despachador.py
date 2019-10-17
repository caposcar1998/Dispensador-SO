from Proceso import Proceso
from Micro import Micro
import math

class Despachador:


    micros = []
    procesos_a_ejecutar = []
    tBloqueo = 15
    cambioContexto = 15
    quantum = 3000

    oscar = Proceso("A",300,1500,2)
    manuel = Proceso ("B",250,600,5)
    gio = Proceso ("C",450,234,8)
    diego = Proceso ("D", 678,54,4)

    procesos_a_ejecutar.append(oscar)
    procesos_a_ejecutar.append(manuel)
    procesos_a_ejecutar.append(gio)
    procesos_a_ejecutar.append(diego)

    def determinar_tiempo_vencimiento_quantum(obj, quantum, cambioContexto):
        return (math.ceil((obj.tiempo_ejecucion/quantum)-1)*cambioContexto)


    def determinar_tiempo_bloqueo(obj,tBloqueo):
        return obj.tiempo_bloqueo*tBloqueo

    #Hacer que el proceso pasado por el metodo encuentre su posicion
    #No encunetra bn la posicion del elemento, al igual que determinar tiempo final
    def determinar_tiempo_inicial(obj,procesos_a_ejecutar):
        counter = 0
        for proceso in procesos_a_ejecutar:
            if counter == 0:
                obj.tiempo_inicial = 0
                return 0
            else:
                counter +=1
                obj.tiempo_inicial =proceso-1[obj.tiempo_final]
                return proceso-1[obj.tiempo_final]


    def determinar_tiempo_final(obj, procesos_a_ejecutar):
        counter = 0
        for proceso in procesos_a_ejecutar:
            if counter == 0:
                obj.tiempo_final = obj.tiempo_total
                return 0
            else:
                obj.tiempo_final = obj.tiempo_total+obj.tiempo_inicial
                return obj.tiempo_total+obj.tiempo_inicial


    def determinar_tiempo_total(obj):
        return obj.tiempo_cambio+obj.tiempo_ejecucion+obj.tiempo_vencimiento_quantum+obj.tiempo_bloqueo
    


   
    print(determinar_tiempo_vencimiento_quantum(oscar, quantum, cambioContexto))
    print(determinar_tiempo_bloqueo(oscar, tBloqueo))
    print(determinar_tiempo_inicial(oscar,procesos_a_ejecutar))
    print(determinar_tiempo_total(oscar))
    print(determinar_tiempo_final(oscar))
    