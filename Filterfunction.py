'''def numero_par(num):
    if num % 2 ==0:
        return True
'''

class Empleado:
    def __init__(self, nombre, cargo, salario):#the construstor
        self.nombre = nombre
        self.cargo=cargo
        self.salario=salario
    def __str__(self):
        return "{} que trabaja como {} y tiene un salario de {} euros".format(self.nombre, self.cargo,self.salario)
    

listaEmpleados = [
    Empleado("Juan", "Director", 75000),
    Empleado("Jesus", "CEO", 200000),
    Empleado("Rogelio", "Chief", 120000),
    Empleado("Maria", "Secretaria", 45000),
    Empleado("Sara", "Administrador", 24000),
    Empleado("Antonio", "Botones", 12000)
]

for empleado in listaEmpleados:
    print(empleado)