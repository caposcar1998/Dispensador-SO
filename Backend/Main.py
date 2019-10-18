
from Despachador import Despachador
from Micro import Micro
from Proceso import Proceso

class Main:


    #Aqui se pone el numero de micros que se van a utlizar
    print("Cuantos micros vas a usar perro loco?")
    micros = input()
    despachador = Despachador()
    print ("Introduce procesos")
    
    #Crear micros que el usuario da
    for i in range(0, int(micros)):
        i = Micro(0,True)
        despachador.micros.append(i)

    #Procesos que el usuario da

    oscar = Proceso("A",300,1500,2)
    manuel = Proceso ("B",100,1500,2)
    gio = Proceso ("C",500,1500,3)
    diego = Proceso ("D", 700,1500,4)

    despachador.procesos_a_ejecutar.append(oscar)
    despachador.procesos_a_ejecutar.append(manuel)
    despachador.procesos_a_ejecutar.append(gio)
    despachador.procesos_a_ejecutar.append(diego)
    
    
    def pasar_procesos_a_micros(obj):
        for micro_vacio in despachador.micros:
            print(micro_vacio)

    #Encontrar con n micros cual es el menor
    def asignar_procesos(despachador):
       
        #Con el micro mas pequeño meter proceso a ejecutar
        print (despachador.micros)

    def detener_en_tiempo_disponible(despachador):
        pass

    def ejecutar_despachador(despachador):
        pass

    asignar_procesos(despachador)