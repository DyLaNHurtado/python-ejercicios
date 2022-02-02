from optparse import Option
import random

def introduce_persona():
    inp = input("Introduce una persona: ")
    file = open("colecciones/mostrar_historial.csv",'a')
    if(file.writable):
        file.writelines(inp+",")
        file.close()
    return inp
        
def sorteo():
    file = open("colecciones/mostrar_historial.csv",'r')
    if(file.readable()):
        list = file.read().split(",")
        if(len(list)>0):
            ganador = random.randint(0,len(list)-2)
            print("El ganador es : ", list[ganador])

        else:
            print("La lista de personas esta vacia")

    else:
        print("El archivo no se ha podido leer")

def print_menu_and_get_option():
    print(""" 
            -- MENU --
    1.- Agregar persona 
    2.- Sorteo
    3.- Salir
            
            """)
    return int(input("Selecciona una opcion:"))


exit=False

while(exit==False):
    option=print_menu_and_get_option()
    list=[]
    if(option==1):
        print("Valor introducido es -> ",introduce_persona())
    elif(option==2):
        sorteo()
    elif(option==3):
        print("Saliendo...")
        exit=True
    else:
        print("Has seleccionado una opcion no valida (Opciones validas: 1 / 2 / 3)")