from pickle import FALSE
import random

def adivinar_num(min,max):
    num = random.randint(min,max)
    fin=False
    while(fin!=True):
        res = str(input("Introduce si tu numero es mayor o menor que %i : "%num)).lower()
        if(res == "mayor"):
            num = num+(max+min)/2
        elif(res == "menor"):
            num = num-(max-min)/2

        elif(res == "si"):
            print("Numero adivinado. Fin del programa")
            fin=True
        else:
            print("Has introducido un opcion que no es valida.** Opciones validas: Mayor / Menor / Si **")
    
adivinar_num(0,100)
