class Messenger:
    def __init__(self,name,pack,zone):
        self.name = name
        self.pack = pack
        self.zone = zone
class Pack_Buissnes:
    def __init__(self):
        self.mess = []
    def add_mess(self,messenger):
        self.mess.append(messenger)
def Menu():
    print("Paquetería BingBong")
    print("1.Ingresar repartidores: ")
    print("2.Mostrar repartidores desordenados")
    print("3.Mostrar repartidores ordenados")
    print("4.Buscar repartidor")
    print("5.Estadisticas generales")
    print("6.Salir")
allow = False
names = []
while allow == False:
    Menu()
    opt = int(input("Ingrese la opción que desee: "))
    print(" ")
    match opt:
        case 1:
            num = int(input("Ingrese cuantos repartidores desea agregar: "))
            if num <= 0:
                print("El valor ingresado no es valido")
            else:
                for i in range (num):
                    name = input("Ingrese el nombre del repartidor: ")
                    if name in names:
                        print("No se puede repetir el nombre")
                    else:
                        names.append(name)
                        pack = int(input("Cuantos paquetes entregó? "))
                        if pack <= 0:
                            print("El valor ingresado no es valido")
                        else:
                            zone = input("Ingrese la zona del repartidor: ")
                            new_mess = Messenger(name,pack,zone)
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