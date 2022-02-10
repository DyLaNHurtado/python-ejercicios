class Usuario:

    def __init__(self, dni="", nombre="", correo="", telefono="", domicilio="", libros_prestamo=[]):

        self.__dni = dni
        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono
        self.__domicilio = domicilio
        self.libros_prestamo = libros_prestamo

    def __str__(self) -> str:
        return f'\nDNI: {self.dni} \n Nombre: {self.nombre}\n Correo: {self.correo}\n Telefono: {self.telefono}\n Domicilio: {self.domicilio}'

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self,dni):
        self.__dni=dni

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre
    
    @property
    def correo(self):
        return self.__correo
    
    @correo.setter
    def correo(self,correo):
        self.__correo=correo
    
    @property
    def telefono(self):
        return self.__telefono
    
    @telefono.setter
    def telefono(self,telefono):
        self.__telefono=telefono

    @property
    def domicilio(self):
        return self.__domicilio
    
    @domicilio.setter
    def domicilio(self,domicilio):
        self.__domicilio=domicilio
    
    @property
    def libros_prestamo(self):
        return self.__libros_prestamo
    
    @libros_prestamo.setter
    def libros_prestamo(self,libros_prestamo):
        self.__libros_prestamo=libros_prestamo