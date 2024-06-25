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

#########################################################

class Furgoneta(Vehiculos):
    
    def carga(self, cargar):
        self.cargado= cargar
        if(self.cargado):
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta NO esta cargada"

#########################################################

class Motos(Vehiculos):
    hcaballito=""
    
    def caballito(self):
        self.hcaballito="Voy haciendo caballito"
    
    def estado(self):
        print("Marca ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.en_marcha, "\nAcelerando: ", self.acelera, "\nFrenar: ", self.frena, "\n", self.hcaballito)
 
 #########################################################   

class Velectricos(Vehiculos):
  
    def __init__(self,marca, modelo):
        super().__init__(marca, modelo)
        self.autonimia=100
        
    def caraga_energia(self):
        self.cargando=True
        
######################################################### 

class Bicicletas_electricas(Velectricos,Vehiculos):
    pass        
        
my_moto1 = Motos("Honda", "CBR")
my_moto1.caballito()
my_moto1.estado()
print("#####################################")
my_furgoneta = Furgoneta("ford","f150")
print(my_furgoneta.carga(False))
my_furgoneta.estado()
print("#####################################")

my_bici = Bicicletas_electricas("Shimano","thor")

my_bici.estado()
print("#####################################")
print(isinstance(my_bici,Vehiculos))

print(isinstance(my_moto1,Velectricos))