import biblioteca.biblioteca as biblio

biblioteca = biblio.Biblioteca()

def main():
    salir = False
    while (salir == False):
        option = input("""\n\t\t*** MENU ***
        
        1.- Alta Usuario
        2.- Baja Usuario
        3.- Alta Libro
        4.- Baja Libro
        5.- Prestar libro
        6.- Devolver libro
        7.- Consultar libros
        8.- Consultar usuarios
        9.- Consultar prestamos
        0.- Salir

        Seleccione opcion(0 - 9): """)
        if(option == "0"):
            print("Saliendo...")
            salir = True

        elif(option == "1"):
            biblioteca.alta_usuario()

        elif(option == "2"):
            biblioteca.baja_usuario()

        elif(option == "3"):
            biblioteca.alta_libros()

        elif(option == "4"):
            biblioteca.baja_libros()

        elif(option == "5"):
            biblioteca.prestar_libro()

        elif(option == "6"):
            biblioteca.devolver_libro()

        elif(option == "7"):
            biblioteca.consultar_libros()

        elif(option == "8"):
            biblioteca.consultar_usuarios()

        elif(option == "9"):
            biblioteca.consultar_prestamos()
        else:
            print("**Opción incorrecta**")
            print("Volviendo al menu...")

        

if __name__ == '__main__':
    main()