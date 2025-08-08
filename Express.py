class Messenger:
    def __init__(self,name,pack,zone):
        self.name = name
        self.pack = pack
        self.zone = zone
    def __str__(self):
        return f'Nombre:{self.name} - Entregas:{self.pack} - Zona:{self.zone}'
class Pack_Buissnes:
    def __init__(self):
        self.mess = []
    def add_mess(self,messenger):
        self.mess.append(messenger)
    def Show(self):
        for messenger in self.mess:
            print(messenger.__str__())
def Menu():
    print("Paquetería BingBong")
    print("1.Ingresar repartidores: ")
    print("2.Mostrar repartidores desordenados")
    print("3.Mostrar repartidores ordenados")
    print("4.Buscar repartidor")
    print("5.Estadisticas generales")
    print("6.Salir")
allow = False
allow1 = False
Buissnes = Pack_Buissnes()
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
                            Buissnes.add_mess(new_mess)
                            allow1 = True
        case 2:
            if allow1 == False:
                print("Aún no hay datos en el sistema")
            else:
                Buissnes.Show()
        case 3:
            if allow1 == False:
                print("Aún no hay datos en el sistema")
            else:
                print(" ")
        case 4:
            if allow1 == False:
                print("Aún no hay datos en el sistema")
            else:
                print(" ")
        case 5:
            if allow1 == False:
                print("Aún no hay datos en el sistema")
            else:
                print(" ")
        case 6:
            print("Gracias por utilizar el programa")
            break
        case _:
            print("La opción seleccionada no es valida")