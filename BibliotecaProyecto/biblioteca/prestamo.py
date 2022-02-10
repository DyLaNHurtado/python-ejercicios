class Prestamo:

    def __init__(self,dni,isbn):
        self.__dni=dni
        self.__isbn=isbn

    def __str__(self) -> str:
        return f'DNI USUARIO: {self.__dni} -> ISBN LIBRO: {self.__isbn}' #Parecido a javascript pero sin '$'

    @property
    def dni(self):
        return self.__dni
    
    @dni.setter
    def usuario_dni(self,dni):
        self.__dni=dni

    @property
    def isbn(self):
        return self.__isbn
    
    @isbn.setter
    def isbn(self,isbn):
        self.__isbn=isbn

