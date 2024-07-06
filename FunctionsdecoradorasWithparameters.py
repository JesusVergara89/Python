
def function_decoradora(function_parametro):

    def interior(*args):
        print("Vamos a realizar un calculo:")
        function_parametro(*args)
        print("Hemos terminado el calculo")
    return interior


@function_decoradora
def suma(num1,num2):
    print(num1+num2)
    
@function_decoradora   
def resta(num1,num2):
    print(num1-num2)

suma(10,5)
resta(10,5)