import random,shutil

class Word:
    def __init__(self,name,meaning) -> None:
        self.name=name
        self.meaning=meaning

class Diccionary:
    def __init__(self,file) -> None:
        self.file=file

    def importDic(self):
        inp=input("Input the uri of diccionary file to import : ")
        shutil.copy(input,"objectos/diccionary.csv")
    def exportDic(self):
        inp=input("Input the uri with the new filename to export : ")
        shutil.copy("objectos/diccionary.csv",input)

    def show(self):
        self.file = open("objetos/diccionary.csv",'r')
        if(file.readable()):
            list = file.read().split(",")
            print("\n\t-- DICCIONARIO --")
            for i in list:
                print(i)

            file.close()
        else:
            print("El archivo no se ha podido leer")

    def inputWord(self):
        inp_name= input("Input a name of word: ")
        inp_meaning = input("Input the meaning of word: ")
        word=Word(inp_name,inp_meaning)
        file = open("objetos/diccionary.csv",'a')
        if(file.writable):
            file.writelines(word.name+"->"+word.meaning+",")
            file.close()
        tuple = word.name,word.meaning
        print("Valor introducido es: ",tuple[0],"->",tuple[1])
    
class Menu:

    def startMenu(self):
        exit = False
        file = open("objetos/diccionary.csv",'r')
        dicc = Diccionary(file)
        while(exit == False):
            print("""
                    -- MENU --
            1.- Introducir palabra
            2.- Consultar Diccionario
            3.- Importar Diccionario
            4.- Exportar Diccionario
            5.- Salir
                    
                    """)
            option=int(input("Selecciona una opcion:"))
            list=[]
            if(option==1):
                dicc.inputWord()
                
            elif(option==2):
                dicc.show()

            elif(option==3):
                dicc.importDic()

            elif(option==4):
                dicc.exportDic()

            elif(option==5):
                print("Saliendo...")
                exit=True
            else:
                print("Has seleccionado una opcion no valida (Opciones validas: 1 / 2 / 3 / 4 / 5)")


menu = Menu()
menu.startMenu()