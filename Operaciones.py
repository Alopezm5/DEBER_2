class Basico:
    def numerosN1(n):
        n=int(input("Ingresar un numero: "))
        print('Numeros del 1 al ', n)
        for i in range(1, n + 1):
            if i == n:
                print(str(i) + '.')
            else:
                print(str(i) + ', ', end='')

    def multiplo(numero):
        pass

    def DivisoresNumero(numero):
        pass

    def primo(numero):
        pass

    def perfecto(numero):
        pass


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


