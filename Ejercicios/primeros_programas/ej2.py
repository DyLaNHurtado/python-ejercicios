def numPie():
    print("Pensar, escribir o apuntar su talla de zapato.")
    print("Multiplicar ese número por 5.")
    print("Sumarle 50.")
    print("Multiplicarlo por 20.")
    print("Sumarle 1021.")
    print("Restarle el año de nacimiento.\n")

    res = (input("Introduce el resultado:"))
    while(len(res)!=4):
        print("** Revisa el resultado deberian salir un numero de 4 cifras **")
        res = (input("Introduce el resultado:"))

    print("Tu talla de pie es: %s"%res[0:2],"\nTu edad es: %s"%res[2:4])




    

numPie()