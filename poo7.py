class Coche():
    def desplazamiento(self):
        print("medezplazo 4 ruedas")


class Moto():
    def desplazamiento(self):
        print("medezplazo 2 ruedas")


class Camion():
    def desplazamiento(self):
        print("medezplazo 6 ruedas")

def desplazamiento_vehiculo(vehiculo):
    vehiculo.desplazamiento()

my_vehiculo=Coche()

desplazamiento_vehiculo(my_vehiculo)