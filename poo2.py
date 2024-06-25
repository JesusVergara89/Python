class Coches():
    def __init__(self):
        self.Largo_chasis=250
        self.ancho_chasis=120
        self.__ruedas=4 #encapsulamiento
        self.en_marcha=False

    def arrancar(self,arrancamos):
        self.en_marcha=arrancamos
        if(self.en_marcha):
            return "the cars is running"
        else:
            return "The cars is stop"


    def state(self):
        print("El coche tiene " , self.__ruedas, " ruedas. Un ancho de ", self.ancho_chasis, " y un largo de ", self.Largo_chasis)
        

mi_Coche = Coches()

print(mi_Coche.arrancar(True))

mi_Coche.state()

print("######################################")

mi_Coche1 = Coches()

print(mi_Coche1.arrancar(False))

mi_Coche1.__ruedas = 3 # this can be posible for encapsulation

mi_Coche1.state()





