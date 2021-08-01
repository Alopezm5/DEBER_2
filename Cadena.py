class Cadena:
    def __init__(self, cadena=""):
        self.cadena=cadena

    def recorrerCadena(self):
        self.cadena = input("Ingresar cadena:")
        print("La cadena es: '{}'y cuenta con:{} caracteres".format(self.cadena, len(self.cadena)))
        # for i, c in enumerate(self.cadena):
        #     print('Caracter: %s' % (c))

    def buscarCaracter(self, buscado=0):
        self.cadena = input("Ingresar cadena:")
        self.buscado= buscado
        con=0
        self.buscado=input("Ingresar el caracter a ser buscado")
        for i in range(len(self.cadena)):
            if (self.cadena[i] == self.buscado):
                con += 1
                print("En la posicion: " + str(i))
        print("Existe solo: " + str(con) + " veces el caracter:" + self.buscado)

    def listaPosiciones(self, caracter=""):
        self.cadena = input("Ingresar cadena:")
        self.caracter= caracter
        self.caracter=input("Ingrese el caracter a buscar en lista: ")
        puesto=[]
        for j, l in enumerate(self.cadena):
            if self.cadena[j]==self.caracter:
                puesto.append(j)
        print("El caracter:{}  - Se encuentra en el puesto: {}".format(self.caracter,puesto))


    def listaPalabras(self,pal=""):
        self.cadena = input("Ingresar cadena:")
        self.pal=pal
        self.pal = self.cadena.split()
        print(self.pal)
        print(len(self.pal))
    
    def cadenaLista(self):
        self.cadena = input("Ingresar cadena:")
        self.pal = self.cadena.split()
        Palabras=str(input("Si desea ingresar mas palabra hagalo, caso contrario para finaizar ingrese un puntito\n"))
        while Palabras!=".":
            self.pal.append(Palabras)
            Palabras=str(input("Si desea ingresar mas palabra hagalo, caso contrario para finaizar ingrese un puntito\n"))
        print("La Lista seria", (self.pal))
        Cade=" ".join(self.pal)
        print("La Cadena seria\n"+ str(Cade))
    
    def insertarDato(self, buscado, posicion):
        self.cadena = input("Ingresar cadena:")
        self.dato = self.cadena.split()
        print(self.dato,"Esta cadena tiene {} posiciones".format(len(self.dato)))
        buscado=input("Ingresar dato a ser aumentado en la cadena: ")
        posicion=int(input("Ingresar la posicion a agregar el dado en la cadena: "))
        self.dato.insert(posicion,buscado)
        print(self.dato)
        
    def eliminarOcurrencias(self,buscado):
        import re
        Lista1=[]
        while buscado!=".":
            Lista1.append(buscado)
            buscado=str(input("Ingrese una palabra, al finaizar use el punto\n"))
        print("La Lista seria\n"+ str(Lista1))
        buscado1=str(input("Ingrese la concurrencia que desea eliminar de la lista\n"))
        oncurrencia=len(re.findall(str(buscado1), str(Lista1)))
        print('La Concurrencia de su caracter es:',oncurrencia)
        Cad1=" ".join(Lista1)
        print("La Cadena seria\n"+ str(Cad1))
        Cad1 = ''.join( x for x in Cad1 if x not in buscado1)
        print("La Cadena quedaria como\n" + str(Cad1))
        
    def RetornarValor(posicion):
        Lista5=[]
        Lista6=[]
        posicion = str(input("Ingrese una palabra, al finaizar use el punto\n"))
        while posicion!=".":
            Lista5.append(posicion)
            posicion=str(input("Ingrese una palabra, al finaizar use el punto\n"))
        Cad1=" ".join(Lista5)
        print("La Cadena seria\n"+ str(Cad1))
        Lista7=Cad1.split()
        lugar=int(input("Que posicion de la lista desea eliminar\n "))
        Lista6.append(lugar)
        print("El Elemento borrado es {}".format(Lista6))
        Retorno=Lista5[lugar]
        Lista7.pop(lugar)
        Cad1=" ".join(Lista7)
        print("El elemento a eliminar es {}\n ".format(Retorno))
        print("La Cadena seria {}\n" .format(Cad1))
    
    def concatenarCadena(self,dato):
        Lista4=[]
        while dato!=".":
            dato=str(input("Ingrese una palabra, al finaizar use el punto\n
            Lista4.append(dato)
        ##print("La Lista seria\n"+ str(Lista))
        Cad=" ".join(Lista4)
        print("La Cadena seria\n"+ str(Cad))
