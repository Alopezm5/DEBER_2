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
   
    def insertarLista(valor="", posicion=0):
        Lista=[]
        valor=str(input("Ingrese una palabra, al finaizar use el punto\n"))
        while valor!=".":
            valor=str(input("Ingrese una palabra, al finaizar use el punto\n"))
            Lista.append(valor)
        print("La Lista seria\n"+ str(Lista))
        buscado1=str(input("Ingrese lo que desea agregar a la lista\n"))
        posicion=int(input("Ingrese en que posicion desea agregar el anadido\n"))
        Lista.insert(posicion, str(buscado1))
        print("La Lista ahora es\n"+ str(Lista))
   
    def eliminarlista(valor):
        import re
        Lista1=[]
        while valor!=".":
            valor=str(input("Ingrese una palabra, al finaizar use el punto\n"))
            Lista1.append(valor)
        print("La Lista seria\n"+ str(Lista1))
        buscado1=str(input("Ingrese la concurrencia que desea eliminar de la lista\n"))
        oncurrencia=len(re.findall(str(buscado1), str(Lista1)))
        print('La Concurrencia de su caracter es:',oncurrencia)
        Cad1=" ".join(Lista1)
        Cad1 = ''.join( x for x in Cad1 if x not in buscado1)
        lista12= Cad1.split()
        print("La Lista quedaria como\n" + str(lista12))
   
   def retornaValor(posicion):
        Lista5=[]
        Lista6=[]
        #posicion = str(input("Ingrese una palabra, al finaizar use el punto\n"))
        while posicion!=".":
            posicion=str(input("Ingrese una palabra, al finaizar use el punto\n"))
            Lista5.append(posicion)
        print("La Lista seria\n"+ str(Lista5))
        lugar=int(input("Que posicion de la lista desea eliminar\n "))
        Lista6.append(lugar)
        print("El Elemento borrado es de la posicion {}".format(Lista6))
        Retorno=Lista5[lugar]
        Lista5.pop(lugar)
        print("El elemento a eliminar es {}\n ".format(Retorno))
        print("La lista nueva seria {}\n" .format(Lista5))
  
   def copiarTuplaLista(tupla):
        lista=[]
        valor = input("Ingrese una palabra, para finaizar use el punto\n")
        while valor!=".":
            lista.append(valor)
            valor=input("Ingrese una palabra, para finaizar use el punto\n")
            tupla= tuple(lista)
            lista= list(tupla)
        print(tupla)
        print( "Copiamos la tupla en una lista y quedó: {}".format(lista))
  
   # def vueltoLista(listaClientesDiccionario):
   #     pass

