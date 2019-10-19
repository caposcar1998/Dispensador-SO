
from Despachador import Despachador
from Micro import Micro
from Proceso import Proceso

class Main:

    tBloqueo = 15
    cambioContexto = 15
    quantum = 3000


    #Aqui se pone el numero de micros que se van a utlizar
    print("Cuantos micros vas a usar perro loco?")
    micros = input()
    despachador = Despachador()
    
    #Crear micros que el usuario da
    for i in range(0, int(micros)):
        i = Micro(0,True, str(i))
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
    

    def pasar_procesos_a_micros(despachador, quantum, tBloqueo, cambioContexto):
        #Crear funcion 1 que regrese menor_desp
        menor = []
        for menor_despachador in despachador.micros:
            menor.append((len(menor_despachador.procesos_ejecucion),menor_despachador.procesos_ejecucion, menor_despachador.nombre))
        menor_desp = min(menor)
        
        #Crear funcion 2
        for entrada_proceso in despachador.micros:
            if(entrada_proceso.nombre == menor_desp[2]):
                entrada_proceso.procesos_ejecucion.append(despachador.procesos_a_ejecutar[0])
                despachador.procesos_a_ejecutar.pop(0)


                #metodos que calculan valores de los procesos dentro de los micros
                despachador.determinar_tiempo_vencimiento_quantum(entrada_proceso.procesos_ejecucion[0], quantum, cambioContexto)
                despachador.determinar_tiempo_cambio_contexto(entrada_proceso.procesos_ejecucion[0], cambioContexto)
                despachador.determinar_tiempo_bloqueo(entrada_proceso.procesos_ejecucion[0],tBloqueo)
                despachador.determinar_tiempo_inicial(entrada_proceso.procesos_ejecucion[0],despachador.micros)
                despachador.determinar_tiempo_total(entrada_proceso.procesos_ejecucion[0])
                despachador.determinar_tiempo_final(entrada_proceso.procesos_ejecucion[0],despachador.micros)
                despachador.determinar_tiempo_ejecucion_micro(entrada_proceso.procesos_ejecucion[0], despachador.micros)

            else:
                pass


    def main (despachador, pasar_procesos_a_micros):
        for procesos in despachador.procesos_a_ejecutar:
            print("Para proceso ", procesos.nombre)
            pasar_procesos_a_micros(despachador, quantum, tBloqueo, cambioContexto)         
        
        
    pasar_procesos_a_micros(despachador, quantum, tBloqueo, cambioContexto) 

