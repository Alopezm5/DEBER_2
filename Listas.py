from Operaciones import *

class Lista(Intermedio):
    def __init__(self, lista=""):
        self.lista = lista


    def presentarLista(self):
        self.lista = self.lista.split()
        nueva = str(input("Ingresar datos que desea tener en la lista, en caso de ingrear mas ingrese un puntito(.) \n"))
        while nueva != ".":
            self.lista.append(nueva)
            nueva = str(input("Si desea ingresar mas datos hagalo, caso contrario para finaizar ingrese un puntito\n"))
        Cade = " ".join(self.lista)
        print("Los datos ingresados son: \n" + Cade)
        print("La lista es: '{}'y cuenta con:{} caracteres".format(self.lista, len(self.lista)))
    
    def buscarLista(self,valor=""):
        self.lista = self.lista.split()
        nueva = str(input("Ingresar datos que desea tener en la lista, en caso de ingrear mas ingrese un puntito(.) \n"))
        while nueva != ".":
            self.lista.append(nueva)
            nueva = str(input("Si desea ingresar mas datos hagalo, caso contrario para finaizar ingrese un puntito\n"))
        print("La lista es: '{}'y cuenta con:{} caracteres".format(self.lista, len(self.lista)))
        con = 0
        valor = str(input("Ingresar el dato a ser buscado: "))
        for i in range(len(self.lista)):
            if self.lista[i] in valor:
                con += 1
        print("Existe solo: " + str(con) + " veces el caracter:" + valor)
