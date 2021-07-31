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
