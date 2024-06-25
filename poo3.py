class Coches():
    def __init__(self):
        self.Largo_chasis=250
        self.ancho_chasis=120
        self.__ruedas=4 #encapsulamiento
        self.en_marcha=False

    def arrancar(self,arrancamos):
        self.en_marcha=arrancamos
        
        if(self.en_marcha):
            checking = self.__checar()


        if(self.en_marcha and checking):
            return "the cars is running"
        elif(self.en_marcha and checking == False):
            print("algo esta mal")
        else:
            return "The cars is stop"

    def state(self):
        print("El coche tiene " , self.__ruedas, " ruedas. Un ancho de ", self.ancho_chasis, " y un largo de ", self.Largo_chasis)
    
    def __checar(self):
        print("realizando chequeo interno")
        self.gasolina='ok'
        self.aceite='ok'
        self.puertas='cerradas'

        if(self.gasolina == 'ok' and self.aceite == 'ok' and self.puertas == 'cerradas'):
            return True
        else:
            return False

        

mi_Coche = Coches()

print(mi_Coche.arrancar(True))

mi_Coche.state()

print("######################################")

mi_Coche1 = Coches()

print(mi_Coche1.arrancar(True))

mi_Coche1.state()

