def introduce_nombre():
    inpPalabra = input("Introduce una palabra: ")
    inpSignificado = input("Introduce su significado: ")
    file = open("colecciones/diccionario.csv",'a')
    if(file.writable):
        file.writelines(inpPalabra+"->"+inpSignificado+",")
        file.close()
    return inpPalabra,inpSignificado
        
def diccionario():
    file = open("colecciones/diccionario.csv",'r')
    if(file.readable()):
        list = file.read().split(",")
        print("\n\t-- DICCIONARIO --")
        for i in list:
            print(i)

        file.close()
    else:
        print("El archivo no se ha podido leer")

exit=False

while(exit==False):
    print(""" 
            -- MENU --
    1.- Introducir palabra
    2.- Consultar Diccionario
    3.- Salir
            
            """)
    option=int(input("Selecciona una opcion:"))
    list=[]
    if(option==1):
        tupla=introduce_nombre()
        print("Valor introducido es: ",tupla[0],"->",tupla[1])
    elif(option==2):
        diccionario()
    elif(option==3):
        print("Saliendo...")
        exit=True
    else:
        print("Has seleccionado una opcion no valida (Opciones validas: 1 / 2 / 3)")
