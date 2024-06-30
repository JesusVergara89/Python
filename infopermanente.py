import pickle

class Persona:

    def __init__(self, nombre, genero, edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print("Se ha creado una persona: ", self.nombre)

    def __str__(self):
        return "{} {} {}".format(self.nombre,self.genero,self.edad)
    
class ListaPersonas:

    personas = []

    def __init__(self):
        listaDePersonas=open("FicheroExterno","ab+")
        listaDePersonas.seek(0)
        try:
            self.personas=pickle.load(listaDePersonas)
            print("Se cargaron {} personas del fichero externo".format(len(self.personas)))
        except:
            print("El fichero esta vacio")
        finally:
            listaDePersonas.close()
            del (listaDePersonas)
        
    def agregarpersonas(self,p):
        self.personas.append(p)
        self.guardarPersonasEnFicheroExterno()

    def mostrarPersonas(self):
        for p in self.personas:
            print(p) 
    
    def guardarPersonasEnFicheroExterno(self):
        listaDePersonas=open("FicheroExterno","wb")
        pickle.dump(self.personas, listaDePersonas)
        listaDePersonas.close()
        del (listaDePersonas)

    def mostrarInfoFicheroExterno(self):
        print("La información del fichero externo es la siguiente: ")
        for p in self.personas:
            print(p)



Mi_lista_de_Peronas = ListaPersonas()

p1= Persona("jesus","Masculino",34)
##p2= Persona("Rogelio","Masculino",50)
##p3= Persona("Veronica","Femenino",22)

Mi_lista_de_Peronas.agregarpersonas(p1)
Mi_lista_de_Peronas.mostrarInfoFicheroExterno()
