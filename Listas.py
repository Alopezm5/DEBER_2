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
    
    def listaFactorial(self):
       lista=[]
       avan="SI"
       while avan=="SI":
           numero = int(input("Ingresar numero: "))
           fact = 1
           if numero != 0:
               for i in range(1, numero + 1):
                   fact *= i
           print('El factorial de {} es: {}'.format(numero, fact))
           lista.append([numero, fact])
           avan=input("Desea ingresar mas numeros").upper()
       print("El primer valor en cada sublista es el numero ingresado y el segundo valor es el resultado factorial\n" , lista)
    
    def listaPrimo(self):
       n = int(input("Ingrese un numero, este indicará cuantos datos se va a ingresar en la siguiente lista: "))
       lista = []
       i=1
       while i<=n:
           numero = int(input("Ingresar numero: "))
           lista.append(numero)
           i += 1
       print("La lista de numeros ingresado es:",lista)
       print("Solo son primos:")
       primos=[]
       for i in lista:
           p = 0
           if i == 1:
               primos.append(i)
           else:
               for j in range(1, i + 1):
                   if i % j == 0:
                       p += 1
               if p == 2:
                   primos.append(i)
       print(primos)
    
    
    # def listaNotas(listaNotasDicccionario):
   #     pass
   
    def insertarLista(valor):
        Lista=[]
        #Valor=str(input("Ingrese una palabra, al finaizar use el punto\n"))
        while Valor!=".":
            Lista.append(Valor)
            Valor=str(input("Ingrese una palabra, al finaizar use el punto\n"))
        print("La Lista seria\n"+ str(Lista))
        buscado1=str(input("Ingrese lo que desea agregar a la lista\n"))
        Posicion=int(input("Ingrese en que posicion desea agregar el anadido\n"))
        Lista.insert(Posicion, str(buscado1))
        print("La Lista ahora es\n"+ str(Lista))
   
   
   # def eliminarLista(valor):
   #     pass
   #
   # def retornaValorLista(posicion):
   #     pass
   #
   # def copiarTuplaLista(tupla):
   #     pass
   #
   # def vueltoLista(listaClientesDiccionario):
   #     pass

