from Cadena import Cadena
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
    menu1 = MENU("Menu Principal",["1)Calculadora", "2)Operación de Numeros", "3)Tratamientos de Listas", "4)Operaciones de Cadenas","5)Salir"])
    opc = menu1.menu()
    if opc=="1":
        menu2 = MENU("Menu Calculadora", ["1)Suma", "2)Resta", "3)Multiplicacion", "4)Division", "5)Salir"])
        opc1=menu1.menu()
        # if opc1=="1":
        #     cal=Calculadora(0,0)
        #     cal.suma()
        # elif opc1=="2":
        #     cal = Calculadora(0,0)
        #     cal.resta()
    elif opc=="2":
        menu2 = MENU("Menu Operación Numero ", ["1)", "2)", "3)", "4)", "5)", "6)", "7)", "8)", "9)", "10)", "11)"])
        opc2=menu2.menu()
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
