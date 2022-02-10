from datetime import datetime

import biblioteca.libro as lib
import biblioteca.prestamo as prest
import biblioteca.usuario as usuario


class Biblioteca:

    def __init__(self,lista_libros=[],lista_usuarios=[],lista_prestamos=[]):
        self.__lista_libros=lista_libros
        self.__lista_usuarios=lista_usuarios
        self.__lista_prestamos=lista_prestamos


    def alta_usuario(self):
        print("Has seleccionado la opción dar de alta un usuario...\n")
        user=usuario.Usuario()
        user.dni=input("\tDNI -> ")
        user.nombre=input("\tNombre -> ")
        user.correo=input("\tCorreo -> ")
        user.telefono=input("\tTelefono -> ")
        user.domicilio=input("\tDomicilio -> ")
        user.libros_prestamo=[]
        self.__lista_usuarios.append(user)
        print("Usuario " + user.nombre + " creado con exito")

    def baja_usuario(self):
        print("Has seleccionado la opción dar de baja un usuario...\n")
        inp_dni=input("\tIntroduce el DNI del usuario -> ")
        for i in self.__lista_usuarios:
            if(i.dni==inp_dni):
                self.__lista_usuarios.remove(i)
                print("Usuario borrado con exito")
            else:
                print("No se ha encontrado el usuario con el DNI indicado...")
                print("Volviendo al menu...")

    def alta_libros(self):
        print("Has seleccionado la opción dar de alta un libro...\n")
        book=lib.Libro()
        book.isbn=input("\tISBN -> ")
        book.titulo=input("\tTitulo -> ")
        book.autor=input("\tAutor -> ")
        book.genero=input("\tGenero -> ")
        book.portada=input("\tPortada -> ")
        book.sinopsis=input("\tSinopsis -> ")
        book.n_ejemplares=input("\tNumero de ejemplares -> ")
        self.__lista_libros.append(book)
        print("Libro " + book.titulo + " creado con exito")

    def baja_libros(self):
        print("Has seleccionado la opción dar de baja un libro...\n")
        inp_isbn=input("\tIntroduce el ISBN del libro -> ")
        for i in self.__lista_libros:
            if(i.isbn==inp_isbn):
                self.__lista_libros.remove(i)
                print("Libro borrado con exito")
            else:
                print("No se ha encontrado el libros con el ISBN indicado...")
                print("Volviendo al menu...")


    def prestar_libro(self):
        print("Has seleccionado la opción de prestar un libro...\n")
        inp_dni=input("\tIntroduce el DNI del usuario -> ")
        user=usuario.Usuario()
        for i in self.__lista_usuarios:
            if(i.dni==inp_dni):
                user=i
        inp_isbn=input("\tIntroduce el ISBN del libro -> ")
        for i in self.__lista_libros:
            if(i.isbn==inp_isbn):
                i.usuario=user
                i.fecha_prestado=datetime.now()
                prestamo=prest.Prestamo(user.dni,i.isbn)
                self.__lista_prestamos.append(prestamo)
                user.libros_prestamo.append(prestamo)
                print("Libro prestado")
            else:
                print("No se ha encontrado el libros con el ISBN indicado...")
                print("Volviendo al menu...")

    def devolver_libro(self):
        print("Has seleccionado la opción de devolver un libro...\n")
        inp_dni=input("\tIntroduce el DNI del usuario -> ")
        user=usuario.Usuario()
        for i in self.__lista_usuarios:
            if(i.dni==inp_dni):
                user=i
        inp_isbn=input("\tIntroduce el ISBN del libro -> ")
        for i in self.__lista_libros:
            if(i.isbn==inp_isbn):
                i.usuario=""
                i.fecha_prestado=""
                libro=i
        for i in self.__lista_prestamos:
            if(i.isbn==libro.isbn and i.dni==user.dni):
                self.__lista_prestamos.remove(i)
                user.libros_prestamo.remove(i)
                print("Libro devuelto")
            else:
                print("No se ha encontrado el libros con el ISBN indicado...")
                print("Volviendo al menu...")

    def consultar_libros(self):
        print("Has seleccionado la opción de consultar libros...\n")
        if(len(self.__lista_libros)==0):
            print("No hay libros disponibles inserte alguno...")
            print("Volviendo al menu...")
        else:
            print("--- LIBROS --")
            for i in self.__lista_libros:
                print(i)

    def consultar_usuarios(self):
        print("Has seleccionado la opción de consultar usuarios...\n")
        if(len(self.__lista_usuarios)==0):
            print("No hay usuarios disponibles inserte alguno...")
            print("Volviendo al menu...")
        else:
            print("--- USUARIOS --")
            for i in self.__lista_usuarios:
                print(i)

    def consultar_prestamos(self):
        print("Has seleccionado la opción de consultar prestamos...\n")
        if(len(self.__lista_prestamos)==0):
            print("No hay prestamos haga alguno...")
            print("Volviendo al menu...")
        else:
            print("--- PRESTAMOS --")
            for i in self.__lista_prestamos:
                print(i)