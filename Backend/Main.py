
from Despachador import Despachador
from Micro import Micro
from Proceso import Proceso

class Main:


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
    

    def pasar_procesos_a_micros(despachador):
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
                procesar_metodos()
            else:
                pass


    def procesar_metodos(despachador):
            pass            
        
        
    pasar_procesos_a_micros(despachador)

