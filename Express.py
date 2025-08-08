def Menu():
    print("Paquetería BingBong")
    print("1.Ingresar repartidores: ")
    print("2.Mostrar repartidores desordenados")
    print("3.Mostrar repartidores ordenados")
    print("4.Buscar repartidor")
    print("5.Estadisticas generales")
    print("6.Salir")
allow = False
while allow == False:
    Menu()
    opt = int(input("Ingrese la opción que desee: "))
    print(" ")
    match opt:
        case 1:
            num = int(input("Ingrese cuantos repartidores desea agregar: "))
        case 2:
            print("Mostrar")
        case 3:
            print("Mostrar")
        case 4:
            print("Buscar")
        case 5:
            print("Stats")
        case 6:
            print("Gracias por utilizar el programa")
            break
        case _:
            print("La opción seleccionada no es valida")