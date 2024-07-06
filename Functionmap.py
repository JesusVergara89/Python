class Empleado:
    def __init__(self, nombre, cargo, salario):#the construstor
        self.nombre = nombre
        self.cargo=cargo
        self.salario=salario
    def __str__(self):
        return "{} que trabaja como {} y tiene un salario de {} euros".format(self.nombre, self.cargo,self.salario)
    

listaEmpleados = [
    Empleado("Juan", "Director", 7500),
    Empleado("Jesus", "CEO", 20000),
    Empleado("Rogelio", "Chief", 12000),
    Empleado("Maria", "Secretaria", 4500),
    Empleado("Sara", "Administrador", 2400),
    Empleado("Antonio", "Botones", 1200)
]

def calculo_comision(empleado):
    if empleado.salario<=5000:
        empleado.salario=empleado.salario*1.03
    return empleado

ListaEmpleadosComision = map(calculo_comision,listaEmpleados )

for empleado in ListaEmpleadosComision:
    print(empleado)