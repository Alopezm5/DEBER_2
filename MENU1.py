from Calculadora import *
from Operaciones import*
from Cadena import *

class MENU():
    def __init__(self,titulo,opciones=[]):
        self.titulo=titulo
        self.opciones=opciones

    def menu(self):
        print(self.titulo)
        for opcion in self.opciones:
            print(opcion)
        opc=input("Elije opcion [1.....{}]:".format(len(self.opciones)))
        return opc
    
salir=False
while not salir:
    menu = MENU("Menu Principal",["1)Calculadora", "2)Operación de Numeros", "3)Tratamientos de Listas", "4)Operaciones de Cadenas","5)Salir"])
    opc = menu.menu()
    if opc=="1":
        while not salir:
            menu1 = MENU("Menu Calculadora", ["1)Suma", "2)Resta", "3)Multiplicacion", "4)Division", "5)Exponente","6)Valor Absoluto", "7)Circunferencia", "8)Area Circulo", "9)Area Cuadrado", "10)Salir"])
            opc1=menu1.menu()
            if opc1=="1":
                cal=Calculadora(0,0)
                cal.suma()
            elif opc1=="2":
                cal = Calculadora(0,0)
                cal.resta()
            elif opc1=="3":
                cal = Calculadora(0,0)
                cal.multiplicacion1()
            elif opc1=="4":
                cal = Calculadora(0,0)
                cal.division()
            elif opc1=="5":
                cale = calEstandar(0, 0)
                cale.exponente()
            elif opc1=="6":
                cale=calEstandar(0)
                cale.valorAbsoluto()
            elif opc1=="7":
                calCi = calCientifica(0,0)
                calCi.circunferencia()
            elif opc1=="8":
                calCi = calCientifica(0, 0)
                calCi.areaCirculo()
            elif opc1=="9":
                calCi = calCientifica(0,0)
                calCi.areaCuadrado()
            elif opc1=="10":
                print("Regresando al menú principal........")
                salir=True
            else:
                print("Ingreso mal la opcion")
                opc1=menu1.menu()
        salir=False
    elif opc=="2":
        while not salir:
            menu2 = MENU("Menu Operación Numero ", ["1)Presentar los numeros de 1 a n", "2)Sumar los numeros de 1 a n", "3)Multiplos de cualquier numero", "4)Presentar los divisores de un numero", "5)Numero Primo", "6)Factorial de cualquier numero", "7)Fibonacci de una serie de n numeros", "8)Perfecto", "9)Primo gemelo", "10)Numeros amigos", "11)Salir"])
            opc2=menu2.menu()
            if opc2 == "1":
                ope = Basico()
                ope.numerosN1()
            elif opc2 == "2":
                ope = Basico()
                ope.multiplo()
            elif opc2 == "3":
                ope = Basico()
                ope.DivisoresNumero()
            elif opc2 == "4":
                ope = Basico()
                ope.primo()
            elif opc2 == "5":
                ope = Basico()
                ope.perfecto()
            elif opc2 == "6":
                ope = Intermedio()
                ope.factorial()
            elif opc2 == "7":
                ope = Intermedio()
                ope.fibonacci()
            elif opc2 == "8":
                ope = Intermedio()
                ope.perfecto()
            elif opc2 == "9":
                ope = Intermedio()
                ope.primosGemelos()
            elif opc2 == "10":
                ope=Intermedio()
                ope.amigos()
            elif opc2 == "11":
                print("Regresando al menú principal........")
                salir = True
            else:
                print("Ingreso mal la opcion")
                opc2 = menu2.menu()
        salir = False
    elif opc=="3":
        menu3=MENU("Menu Tratamiento de Lista", ["1)Recorrer y presentar los datos", "2)Buscar un valor en una lista", "3)Retornar una lista con los factoriales", "4)Retornar una lista de números primos", "5)Recorrer una lista de diccionario con notas de alumnos","6)Insertar un dato en una Lista dada lo Posición","7)Eliminar todas las ocurrencias en una Lista","8)Retornar cualquier valor de una lista eliminándolo","9)Copiar cada elemento de una tupla en una lista","10)Dar el vuelto a varios clientes","11)Salir"])
        opc3=menu3.menu()
        if opc3=="1":
            cal=Cadena()
            cal.recorrerCadena()
        elif opc3=="2":
            cal = Calculadora(0,0)
            cal.resta()
        elif opc3=="3":
            cal=Calculadora(0,0)
            cal.suma()
        elif opc3=="4":
            cal = Calculadora(0,0)
            cal.resta()
        elif opc3=="5":
            cal=Calculadora(0,0)
            cal.suma()
        elif opc3=="6":
            cal = Calculadora(0,0)
            cal.resta()
        elif opc3=="7":
            cal=Calculadora(0,0)
            cal.suma()
        elif opc3=="8":
            cal = Calculadora(0,0)
            cal.resta()
        elif opc3=="9":
            cal=Calculadora(0,0)
            cal.suma()
        elif opc3=="10":
            cal = Calculadora(0,0)
            cal.resta()
        elif opc3=="11":
            cal = Calculadora(0,0)
            cal.resta()
        else:
            print("Mal ingreso")
    elif opc=="4":
        while not salir:
            menu4 = MENU("Menu Operaciones de Cadena", ["1)Recorrer y presentar los datos de una cadena", "2)Buscar un cáracter en una cadena","3)Retornar una lista con las posiciones dado un cáracter de la cadena","4)Retornar una lista de todas las palabras de una cadena","5)Retornar una cadena a partir de una lista","6)Insertar un dato en una cadena dada la Posición","7)Eliminar todas las ocurrencias en una cadena","8)Retornar cualquier valor de una lista eliminándolo","9)Concatenar cualquier valor de una cadena eliminandola","10)Salir"])
            opc4 = menu4.menu()
            if opc4=="1":
                cad=Cadena("")
                cad.recorrerCadena()
            elif opc4=="2":
                cad = Cadena("")
                cad.buscarCaracter()
            elif opc4=="3":
                cad=Cadena("")
                cad.listaPosiciones()
            elif opc4=="4":
                cad=Cadena("")
                cad.listaPalabras()
            elif opc4=="5":
                cad = Cadena("")
                cad.cadenaLista()
            elif opc4=="6":
                cad = Cadena("")
                cad.insertarOcurrencia()
            elif opc4=="7":
                cad = Cadena("")
                cad.eliminarOcurrencia()
            elif opc4=="8":
                cad = Cadena("")
                cad.retornaValor()
            elif opc4=="9":
                cad = Cadena("")
                cad.concatenarCadena()
            elif opc4=="10":
                print("Regresando al menú principal....")
                salir=True
            else:
                print("Ingreso mal la opcion")
                opc4=menu4.menu()
        salir = False
    elif opc=="5":
        salir=True
    else:
        print("Error de ingreso, por favor escoja bien una de las opciones")
print("FIN")
