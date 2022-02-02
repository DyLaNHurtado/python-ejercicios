def cinco_nombres():
    inp1=input("Introduce nombre 1 : ")
    inp2=input("Introduce nombre 2 : ")
    inp3=input("Introduce nombre 3 : ")
    inp4=input("Introduce nombre 4 : ")
    inp5=input("Introduce nombre 5 : ")
    list=[inp1,inp2,inp3,inp4,inp5]
    list.sort()
    return list
    #Se puede usar en el metodo sort(key=nombre_funcion,reverse=False)

for i in cinco_nombres():
    print(i)