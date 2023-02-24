from tablero import*
from ficha import*
import random



def iniciarJuego():

    #crear la lista de posibles jugadores
    listaJug=['rojo','verde','azul','morado','lila','amarillo','naranja']
    listaJug=aleatLista(listaJug)
    listaJug2=[]

    #asignar la lista de fichas con los colores de la lista(jugadores)
    for i in listaJug:
        listaJug2.append(Ficha(i))

    #asignar la lista de jugadores a la clase tablero y las casillas que este tiene
    tablero2=Tablero(listaJug2,50)


    #comienaza el juego
    fin=0
    ganador=0
    r=1
    while fin==0:
        print('Ronda '+str(r))
        r+=1
        print('')
        for n in tablero2.jugadores:
            n.avanzar()
            if n.posicion>tablero2.cantCasillas:
                fin=1
                ganador=n
                print('-------------------------------')
                print('Tenemos un ganador.')
                break
        print('')
        print('')
    print('-------------------------------')
    print('El ganador es '+ganador.color)
    




def aleatLista(lista):
    listaN=[]

    while len(lista)>1:
        Ncolor=random.randint(0,len(lista)-1)
        listaN.append(lista[Ncolor])

        if Ncolor==0:
            lista=lista[1:]

        elif Ncolor==len(lista)-1:
            lista=lista[:Ncolor]

        else:
            lista=lista[:Ncolor]+lista[Ncolor+1:]
    listaN.append(lista[0])

    return listaN


print("_Para comenzar utilice el comando 'iniciarJuego()'_")
