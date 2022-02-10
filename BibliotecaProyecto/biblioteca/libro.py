from datetime import datetime

import biblioteca.usuario as user

class Libro:
    def __init__(self,isbn="",titulo="",autor="",genero="",portada="",sinopsis="",n_ejemplares="",usuario=user.Usuario(),fecha_prestado=datetime.now()):
        self.__isbn=isbn
        self.__titulo=titulo
        self.__autor=autor
        self.__genero=genero
        self.__portada=portada
        self.__sinopsis=sinopsis
        self.__n_ejemplares=n_ejemplares
        self.__usuario = usuario
        self.__fecha_prestado = fecha_prestado

    def __str__(self) -> str:
        return f'\nISBN: {self.isbn} \n Titulo: {self.titulo} \n Autor: {self.autor}\n Genero: {self.genero}\n Portada: {self.portada} \n Sinopsis: {self.sinopsis} \n Numero de ejemplares: {self.n_ejemplares}'


    @property
    def isbn(self):
        return self.__isbn
    
    @isbn.setter
    def isbn(self,isbn):
        self.__isbn=isbn

    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self,titulo):
        self.__titulo=titulo
    
    @property
    def autor(self):
        return self.__autor
    
    @autor.setter
    def autor(self,autor):
        self.__autor=autor
    
    @property
    def genero(self):
        return self.__genero
    
    @genero.setter
    def genero(self,genero):
        self.__genero=genero

    @property
    def portada(self):
        return self.__portada
    
    @portada.setter
    def portada(self,portada):
        self.__portada=portada
    
    @property
    def sinopsis(self):
        return self.__sinopsis
    
    @sinopsis.setter
    def sinopsis(self,sinopsis):
        self.__sinopsis=sinopsis
    
    @property
    def n_ejemplares(self):
        return self.__n_ejemplares
    
    @n_ejemplares.setter
    def n_ejemplares(self,n_ejemplares):
        self.__n_ejemplares=n_ejemplares

    @property
    def usuario(self):
        return self.__usuario
    
    @usuario.setter
    def usuario(self,usuario):
        self.__usuario=usuario
    
    @property
    def fecha_prestado(self):
        return self.__fecha_prestado
    
    @fecha_prestado.setter
    def fecha_prestado(self,fecha_prestado):
        self.__fecha_prestado=fecha_prestado
