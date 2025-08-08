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
        cont = 1
        for messenger in self.mess:
            print(f"Repartidor {cont}")
            print(messenger.__str__())
            cont = cont + 1
    def Q_S(self,messenger_list=None):
        if messenger_list == None:
            return self.mess
        if len(messenger_list) <= 1:
            return messenger_list
        else:
            Check = messenger_list[0]
            low = [x for x in messenger_list[1:] if x.pack < Check.pack]
            same = [x for x in messenger_list[1:] if x.pack == Check.pack]
            upp = [x for x in messenger_list[1:] if x.pack > Check.pack]
            return self.Q_S(upp) + [Check] + same + self.Q_S(low)
    def Stats(self):
        tot = 0
        for messenger in self.mess:
            tot = tot + messenger.pack
        print(f"El total de paquetes entregados fue: {tot}")
        average = tot / len(self.mess)
        print(" ")
        print(f"El promedio de paquetes por repartidor fue {average}")
        print(" ")
        High = 0
        cont = 0
        i = 0
        for messenger in self.mess:
            if messenger.pack > High:
                High = messenger.pack
                i = cont
            cont = cont + 1
        print(f"El repartidor con más entregas fue {self.mess[i].name} con {High} entregas")
        Low = 0
        cont = 0
        i = 0
        for messenger in self.mess:
            low = messenger.pack
            break
        for messenger in self.mess:
            if messenger.pack < Low:
                Low = messenger.pack
                i = cont
            cont = cont + 1
        print(" ")
        print(f"El repartidor con menos entregas fue {self.mess[i].name}")
        print("")
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
            cont = 1
            if allow1 == False:
                print("Aún no hay datos en el sistema")
            else:
                sorted = Buissnes.Q_S()
                for messenger in sorted:
                    print(f"Repartidor {cont}")
                    print(messenger.__str__())
        case 4:
            if allow1 == False:
                print("Aún no hay datos en el sistema")
            else:
                print(" ")
        case 5:
            if allow1 == False:
                print("Aún no hay datos en el sistema")
            else:
                Buissnes.Stats()
        case 6:
            print("Gracias por utilizar el programa")
            break
        case _:
            print("La opción seleccionada no es valida")