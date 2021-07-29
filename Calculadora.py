class Calculadora:
    def __init__(self, numero1=0, numero2=0):
        self.numero1 = numero1
        self.numero2 = numero2

    def suma(self):
        self.numero1 = int(input("Ingresar numero 1: "))
        self.numero2 = int(input("Ingresar numero 2: "))
        print("{} + {} = {} ".format(self.numero1,self.numero2,self.numero1+self.numero2))

    def resta(self):
        self.numero1 = int(input("Ingresar numero 1: "))
        self.numero2 = int(input("Ingresar numero 2: "))
        print("{} - {} = {} ".format(self.numero1, self.numero2, self.numero1 - self.numero2))

    def multiplicacion1(self):
        self.numero1 = int(input("Ingresar numero 1: "))
        self.numero2 = int(input("Ingresar numero 2: "))
        print("{} * {} = {} ".format(self.numero1, self.numero2, self.numero1 * self.numero2))

    def division(self):
        self.numero1 = int(input("Ingresar numero 1: "))
        self.numero2 = int(input("Ingresar numero 2: "))
        if self.numero2 == 0:
            print("No hay división para 0")
        else:
            print("{} / {} = {} ".format(self.numero1, self.numero2, self.numero1 / self.numero2))
