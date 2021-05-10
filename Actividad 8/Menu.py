from Conjunto import Conjunto

def imprimir():
    print(" ")
    print("--------MENU----------")
    print("1. Unión de dos conjuntos")
    print("2. Diferencia de dos conjuntos")
    print("3. Verificar si los conjuntos son iguales")
    print("0. Salir")
    print(" ")

def menu(c1,c2):
    print('')
    print("El primer conjunto es: ",c1.mostrar())
    print("El segundo conjunto es: ",c2.mostrar())
    print('')

    band=True
    while band:
        imprimir()
        opcion = int(input('Ingrese una opción: '))

        if opcion == 1:
            c = c1 + c2
            print("Union: ", c.mostrar())
        
        elif opcion == 2:
            c = c1 - c2
            print("Diferencia: ", c.mostrar())

        elif opcion == 3:
            if c1 == c2:
                print('Son iguales.')
            else: 
                print('Son diferentes.')

        else:
            band=False
            print('Programa finalizado.')

if __name__ == '__main__':
        c1=[30,23,6,17,43,55,20,24,8,37]
        c2=[17,78,23,43,5,34,20,49,25,14]

        c1=Conjunto(c1)
        c2=Conjunto(c2)
        menu(c1,c2)

