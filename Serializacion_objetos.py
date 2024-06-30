import pickle
class Vehiculos():
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False
   
    def arrancar(self):
        self.enmarcha=True

    def acelerar(self):
        self.ace=True

    def frenar(self):
        self.frena=True

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)


Car1 = Vehiculos("mazda","6")
Car2 = Vehiculos("renault","pi")
Car3 = Vehiculos("wolsvagen","dum")


cars= [Car1,Car2,Car3]

fichero = open("losCoches","wb")

pickle.dump(cars,fichero)

fichero.close()

del (fichero)

