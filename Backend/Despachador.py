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
    manuel = Proceso ("B",100,1500,2)
    gio = Proceso ("C",500,1500,3)
    diego = Proceso ("D", 700,1500,4)

    procesos_a_ejecutar.append(oscar)
    procesos_a_ejecutar.append(manuel)
    procesos_a_ejecutar.append(gio)
    procesos_a_ejecutar.append(diego)


    def determinar_tiempo_vencimiento_quantum(obj, quantum, cambioContexto):
        obj.tiempo_vencimiento_quantum =  (math.ceil((obj.tiempo_ejecucion/quantum)-1)*cambioContexto)
        print(obj.tiempo_vencimiento_quantum)


    def determinar_tiempo_cambio_contexto(obj, valor):
        obj.tiempo_cambio_contexto = valor


    def determinar_tiempo_bloqueo(obj,tBloqueo):
        obj.tiempo_bloqueo =  obj.tiempo_bloqueo*tBloqueo
        print(obj.tiempo_bloqueo)


    def determinar_tiempo_inicial(obj,procesos_a_ejecutar):
        for i in range(0, len(procesos_a_ejecutar)):
            if (procesos_a_ejecutar[i] == procesos_a_ejecutar[0]):
                procesos_a_ejecutar[i].tiempo_inicial  = 0
                print(procesos_a_ejecutar[i].tiempo_inicial)
            else:
                procesos_a_ejecutar[i].tiempo_inicial = procesos_a_ejecutar[i-1].tiempo_final
                print(procesos_a_ejecutar[i].tiempo_inicial)


    def determinar_tiempo_total(obj):
        obj.tiempo_total=  obj.tiempo_ejecucion+obj.tiempo_vencimiento_quantum+obj.tiempo_bloqueo+obj.tiempo_cambio_contexto
        print(obj.tiempo_total)

    def determinar_tiempo_final(obj, procesos_a_ejecutar):
        obj.tiempo_final = obj.tiempo_inicial+ obj.tiempo_total
        print( obj.tiempo_final)
 

    print("OSCAR")
    print("Tiempo de camvio contexto")
    determinar_tiempo_cambio_contexto(oscar,0)
    print("determinar_tiempo_vencimiento_quantum")
    determinar_tiempo_vencimiento_quantum(oscar, quantum, cambioContexto)
    print("determinar_tiempo_bloqueo")
    determinar_tiempo_bloqueo(oscar, tBloqueo)
    print("determinar_tiempo_inicial")
    determinar_tiempo_inicial(oscar,procesos_a_ejecutar)
    print("determinar_tiempo_total")
    determinar_tiempo_total(oscar)
    print("determinar_tiempo_final")
    determinar_tiempo_final(oscar, procesos_a_ejecutar)
    
    print("MANUEL")
    print("Tiempo de camvio contexto")
    determinar_tiempo_cambio_contexto(manuel,0)
    print("determinar_tiempo_vencimiento_quantum")
    determinar_tiempo_vencimiento_quantum(manuel, quantum, cambioContexto)
    print("determinar_tiempo_bloqueo")
    determinar_tiempo_bloqueo(manuel, tBloqueo)
    print("determinar_tiempo_inicial")
    determinar_tiempo_inicial(manuel,procesos_a_ejecutar)
    print("determinar_tiempo_total")
    determinar_tiempo_total(manuel)
    print("determinar_tiempo_final")
    determinar_tiempo_final(manuel, procesos_a_ejecutar)

    print("GIO")
    print("Tiempo de camvio contexto")
    determinar_tiempo_cambio_contexto(gio,15)
    print("determinar_tiempo_vencimiento_quantum")
    determinar_tiempo_vencimiento_quantum(gio, quantum, cambioContexto)
    print("determinar_tiempo_bloqueo")
    determinar_tiempo_bloqueo(gio, tBloqueo)
    print("determinar_tiempo_inicial")
    determinar_tiempo_inicial(gio,procesos_a_ejecutar)
    print("determinar_tiempo_total")
    determinar_tiempo_total(gio)
    print("determinar_tiempo_final")
    determinar_tiempo_final(gio, procesos_a_ejecutar)

    print("DIEGO")
    print("Tiempo de camvio contexto")
    determinar_tiempo_cambio_contexto(diego,15)
    print("determinar_tiempo_vencimiento_quantum")
    determinar_tiempo_vencimiento_quantum(diego, quantum, cambioContexto)
    print("determinar_tiempo_bloqueo")
    determinar_tiempo_bloqueo(diego, tBloqueo)
    print("determinar_tiempo_inicial")
    determinar_tiempo_inicial(diego,procesos_a_ejecutar)
    print("determinar_tiempo_total")
    determinar_tiempo_total(diego)
    print("determinar_tiempo_final")
    determinar_tiempo_final(diego, procesos_a_ejecutar)