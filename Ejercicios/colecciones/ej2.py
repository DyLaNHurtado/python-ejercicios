def introduce_nombre():
    inp = input("Introduce una palabra: ")
    file = open("colecciones/mostrar_historial.txt",'a')
    if(file.writable):
        file.writelines(inp+",")
        file.close()
    return inp
        
def mostrar_historial():
    file = open("colecciones/mostrar_historial.txt",'r')
    if(file.readable()):
        list = file.read().split(",")
        print("\n\t-- HISTORIAL --")
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
    2.- Cargar palabras
    3.- Salir
            
            """)
    option=int(input("Selecciona una opcion:"))
    list=[]
    if(option==1):
        print("Valor introducido es -> ",introduce_nombre())
    elif(option==2):
        mostrar_historial()
    elif(option==3):
        print("Saliendo...")
        exit=True
    else:
        print("Has seleccionado una opcion no valida (Opciones validas: 1 / 2 / 3)")
