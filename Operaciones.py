class Basico:
    def numerosN1(n):
        n=int(input("Ingresar un numero: "))
        print('Numeros del 1 al ', n)
        for i in range(1, n + 1):
            if i == n:
                print(str(i) + '.')
            else:
                print(str(i) + ', ', end='')

        def sumaNumeros(n):
        n = int(input("Ingresar un numero: "))
        print('Numeros del 1 al ', n)
        p=0
        for i in range(1, n + 1):
            p=p+i
        print("La suma desde el 1 hasta el: {}, es: {}".format(n,p) )

    def multiplo(numero):
        numero=int(input("Ingresar numero a sacar sus mutiplos: "))
        print('Multiplos de', numero, '\n0, ', end='')
        for i in range(1, numero+1):
            if (numero * i) % i == 0:
                if i == numero:
                    print(str(i*numero) + '.')
                else: print(str(i*numero) + ', ' ,end='')

    def DivisoresNumero(numero):
        numero=int(input("Ingresar numero a sacar sus divisores: "))
        print('Divisores de', numero)
        for i in range(1, numero+1):
            if numero % i == 0:
                if i == numero:
                    print(str(i) + '.')
                else: print(str(i) + ', ' ,end='')

    def primo(numero):
        numero=int(input("Ingresar numero para ser verificado: "))
        con=0
        for i in range(1,numero+1):
            if numero%i==0:
                con=con+1
        if con==2:
            print("Es primo")
        else:
            print("No es primo")

    def perfecto(numero):
        numero=int(input("Ingresar numero a ser verificado: "))
        sum = 0
        for i in range(1, numero):
            if numero % i == 0:
                sum += i
        if numero == sum:
            print(' >El número es perfecto')
        else:
            print(' >El número no es perfecto')


class Intermedio(Basico):

    def numerosN2(n):  # aplicar polimorfismo
        pass

    def factorial(numero):  #
        pass

    def fibonacci(n):
        pass

    def primosGemelos(num1, num2):
        pass

    def amigos(num1, num2):
        pass


