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
    
menu1=MENU("Menu Principal",["1)Calculadora", "2)Operación de Numeros", "3)Tratamientos de Listas", "4)Operaciones de Cadenas", "5)Salir"] )
opc = menu1.menu()
if opc=="1":
    menu1 = MENU("Menu Calculadora", ["1)Suma", "2)Resta", "3)Multiplicacion", "4)Division", "5)Salir"])
    opc1=menu1.menu()
    if opc1=="1":
        cal=Calculadora(0,0)
        cal.suma()
    elif opc1=="2":
        cal = Calculadora(0,0)
        cal.resta()

elif opc=="2":
    menu1 = MENU("Menu Operación Numero ", ["1)", "2)", "3)", "4)", "5)", "6)", "7)", "8)", "9)", "10)", "11)"])
    opc1=menu1.menu()

elif opc=="3":
    menu1=MENU("Menu Tratamiento de Lista", ["1)Recorrer y presentar los datos", "2)Buscar un valor en una lista", "3)Retornar una lista con los factoriales", "4)Retornar una lista de números primos", "5)Recorrer una lista de diccionario con notas de alumnos","6)Insertar un dato en una Lista dada lo Posición","7)Eliminar todas las ocurrencias en una Lista","8)Retornar cualquier valor de una lista eliminándolo","9)Copiar cada elemento de una tupla en una lista","10)Dar el vuelto a varios clientes","11)Salir"])
    opc1=menu1.menu()
    if opc1=="1":
        cal=Cadena()
        cal.recorrerCadena()
    elif opc1=="2":
        cal = Calculadora(0,0)
        cal.resta()
    elif opc1=="3":
        cal=Calculadora(0,0)
        cal.suma()
    elif opc1=="4":
        cal = Calculadora(0,0)
        cal.resta()
    elif opc1=="5":
        cal=Calculadora(0,0)
        cal.suma()
    elif opc1=="6":
        cal = Calculadora(0,0)
        cal.resta()
    elif opc1=="7":
        cal=Calculadora(0,0)
        cal.suma()
    elif opc1=="8":
        cal = Calculadora(0,0)
        cal.resta()
    elif opc1=="9":
        cal=Calculadora(0,0)
        cal.suma()
    elif opc1=="10":
        cal = Calculadora(0,0)
        cal.resta()
    elif opc1=="11":
        cal = Calculadora(0,0)
        cal.resta()
    else:
        print("Mal ingreso")
elif opc=="4":
    menu1=MENU("Menu Operaciones de Cadena", ["1)Recorrer y presentar los datos de una cadena", "2)Buscar un cáracter en una cadena", "3)Retornar una lista con las posiciones dado un cáracter de la cadena", "4)Retornar una lista de todas las palabras de una cadena", "5)Retornar una cadena a partir de una lista","6)Insertar un dato en una cadena dada la Posición","7)Eliminar todas las ocurrencias en una cadena","8)Retornar cualquier valor de una lista eliminándolo","9)Concatenar cualquier valor de una cadena eliminandola","10)Salir"])
    opc1=menu1.menu()
    if opc1=="1":
        cad=Cadena("")
        cad.recorrerCadena()
    elif opc1=="2":
        cad = Cadena("")
        cad.buscarCaracter()
    elif opc1=="3":
        cad=Cadena("")
        cad.listaPosiciones()
    # elif opc1=="4":
    # elif opc1=="5":
    # elif opc1=="6":
    # elif opc1=="7":
    # elif opc1=="8":
    # elif opc1=="9":
    # elif opc1=="10":
    else:
        print("Mal ingreso")
elif opc=="5":
    print("NAda")
else:
    print("Ingreso invalido")
    
else:
    print("Ingreso invalido")
  
