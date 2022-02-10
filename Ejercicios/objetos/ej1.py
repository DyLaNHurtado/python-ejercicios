import random
class Saludo:
    saludos=["Buenas tardes Juan","Hola Juan, me alegro de verte","Pero me cago en dios si eres tu Juan","Kitipasa Juan tronco mazo tiempo no??"]
    def formal(self,nombre="Juan"):
        saludo= self.saludos[random.randint(0,1)]
        saludo=saludo.replace("Juan",nombre)
        return saludo

    def informal(self,nombre="Juan"):
        saludo= self.saludos[random.randint(2,3)]
        saludo=saludo.replace("Juan",nombre)
        return saludo
    def aleatorio(self,nombre="Juan"):
        saludo= self.saludos[random.randint(0,3)]
        saludo=saludo.replace("Juan",nombre)
        return saludo


saludo= Saludo()
print(saludo.formal())
print(saludo.informal())
print(saludo.aleatorio())
print()
print(saludo.formal("Javi"))
print(saludo.informal("Javi"))
print(saludo.aleatorio("Javi"))
