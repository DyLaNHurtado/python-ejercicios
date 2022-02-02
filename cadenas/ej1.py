

def op_strings():
    inp= input("Introduzca cualquier cadena/string/frase : ")
    print("Longitud del string: ",len(inp))
    print("Longitud del string: ",inp.find(" "))
    print("Longitud del string: ",inp.upper())
    print("Duplicar valor cadena: ",inp*2)
    list=inp.split(" ")
    print("Lista a traves de espacios: ",list)
    print("Recorriendo la lista : ")
    for i in list:
        print(i)
    print("-- FIN --")
op_strings()