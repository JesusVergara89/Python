class Coches():
    Largo_chasis=250
    ancho_chasis=120
    ruedas=4
    en_marcha=False

    def arrancar(self):
        self.en_marcha=True

    def state(self):
        if(self.en_marcha):
            return "the cars is running"
        else:
            return "The cars is stop"


mi_Coche = Coches()

mi_Coche.arrancar()

print(mi_Coche.state())

