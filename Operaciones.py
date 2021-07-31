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

    # def numerosN2(n):  # aplicar polimorfismo
    #     n = int(input("Ingresar numero"))
    #     print('Suma del número 1 al', n)
    #     sum = 0
    #     for i in range(1, n + 1):
    #         sum += i
    #     print('La suma es:', sum)

    def factorial(numero):
        numero=int(input("Ingresar numero: "))
        fact = 1
        if numero != 0:
            for i in range(1, numero + 1):
                fact *= i
        print('El factorial de {} es: {}'.format(numero,fact))

    def fibonacci(n):
        n=int(input("Ingresar numero: "))
        print('Fibonacci hasta el', n, '\n' + '0')
        for i in range(n - 1):
            a = 0
            b = 1
            for j in range(i):
                c = a + b
                a = b
                b = c
            print(b)

    def primosGemelos(num1=0, num2=0):
        num1=int(input("Ingresar un numero menor: "))
        num2=int(input("Ingresar un numero mayor: "))
        if num1 != num2:
            a,b = 0,0
            if num1 > num2:
                n3 = num1
                num1 = num2
                num2 = n3
            print('Números primos gemelos del', num1, 'al', num2)
            if num2 > 4:
                for i in range(num1, num2 + 1):
                    incremento = 2
                    primo = True
                    while primo and incremento < i:
                        if i % incremento == 0:
                            primo = False
                        else:
                            incremento += 1
                    if primo and not a:
                        a = i
                    elif primo and a:
                        b = i
                        if b - a == 2:
                            print(a, 'y', b, 'son números primos gemelos.')
                        a = i
            else:
                print('No hay números gemelos.')
        else:
            print('Ingrese números diferentes')

    def amigos(num1=0, num2=0):
        while True:
            num1 = int(input("Ingresar numero 1: "))
            num2 = int(input("Ingresar numero 2: "))
            if num1 != num2:
                suma_a, suma_b = 0, 0
                if num1 > num2:
                    n3 = num1
                    num1 = num2
                    num2 = n3
                for cont in range(1, num1 + 1):
                    if num1 % cont == 0:
                        suma_a += cont
                for cont in range(1, num2 + 1):
                    if num2 % cont == 0:
                        suma_b += cont
                if suma_a == suma_b and suma_b == suma_a:
                    print(' >Son amigos')
                    break
                else:
                    print(' >No son amigos')
                    break
            print('Ingrese números diferentes')


