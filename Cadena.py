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
        self.caracter=input("ingrese El caracter a buscar en lista: ")
        for j, l in enumerate(self.cadena):
            print("Caracter: %s - Puesto: %i " % (l,j))
            if self.cadena[j]==caracter:
                print("El caracter: %s  - Se encuentra en el puesto: %i " % (l,j))

    def listaPalabras(self):
        pass
    def cadenaLista(self):
        pass
    def insertarDato(self, buscado, posicion):
        pass
    def eliminarOcurrencias(self,buscado):
        pass
    def retornaValor(self,posicion):
        pass
    def concatenarCadena(self,dato):
        pass
