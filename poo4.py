class Vehiculos():
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
        self.en_marcha=False
        self.acelera=False
        self.frena=False
    
    def arrancar(self):
        
        self.en_marcha=True
        
    def acelerar(self):
        
        self.acelera=True
        
    def frenar(self):
        
        self.frena=True
        
    def estado(self):
        print("Marca ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.en_marcha, "\nAcelerando: ", self.acelera, "\nFrenar: ", self.frena)


class Motos(Vehiculos):
    pass
        
my_moto1 = Motos("Honda", "CBR")

my_moto1.estado()