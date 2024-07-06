
def function_decoradora(function_parametro):

    def interior(*args, **kwargs):#numero indeterminado de parametros. number indetermind of parameters = args
        print("Vamos a realizar un calculo:")
        function_parametro(*args, **kwargs)#indetermined number or key words parameters= kwargs
        print("Hemos terminado el calculo")
    return interior


@function_decoradora
def suma(num1,num2):
    print(num1+num2)
    
@function_decoradora   
def resta(num1,num2):
    print(num1-num2)

@function_decoradora
def potencia(base, exponente):
    print(pow(base,exponente))

suma(10,5)
print("#############")
resta(10,5)
print("#############")
potencia(base=5,exponente=3)