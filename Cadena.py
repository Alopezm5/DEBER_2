class Cadena:
    def __init__(self, cadena=""):
        self.cadena=cadena
        self.cadena = input("Ingresar cadena:")

    def recorrerCadena(self):
        print("La cadena es: '{}'y cuenta con:{} caracteres".format(self.cadena, len(self.cadena)))
        # for i, c in enumerate(self.cadena):
        #     print('Caracter: %s' % (c))

    def buscarCaracter(self, buscado=0):
        self.buscado= buscado
        con=0
        self.buscado=input("Ingresar el caracter a ser buscado")
        for i in range(len(self.cadena)):
            if (self.cadena[i] == self.buscado):
                con += 1
                print("En la posicion: " + str(i))
        print("Existe solo: " + str(con) + " veces el caracter:" + self.buscado)

    def listaPosiciones(self, caracter=""):
        self.caracter= caracter
        self.caracter=input("Ingrese el caracter a buscar en lista: ")
        puesto=[]
        for j, l in enumerate(self.cadena):
            if self.cadena[j]==self.caracter:
                puesto.append(j)
        print("El caracter:{}  - Se encuentra en el puesto: {}".format(self.caracter,puesto))


    def listaPalabras(self,pal=""):
        self.pal=pal
        self.pal = self.cadena.split()
        print(self.pal)
        print(len(self.pal))
    
    def cadenaLista(self):
        self.pal = self.cadena.split()
        Palabras=str(input("Si desea ingresar mas palabra hagalo, caso contrario para finaizar ingrese un puntito\n"))
        while Palabras!=".":
            self.pal.append(Palabras)
            Palabras=str(input("Si desea ingresar mas palabra hagalo, caso contrario para finaizar ingrese un puntito\n"))
        print("La Lista seria", (self.pal))
        Cade=" ".join(self.pal)
        print("La Cadena seria\n"+ str(Cade))
    
    def insertarDato(self, buscado, posicion):
        pass
    def eliminarOcurrencias(self,buscado):
        pass
    def retornaValor(self,posicion):
        pass
    def concatenarCadena(self,dato):
        pass
