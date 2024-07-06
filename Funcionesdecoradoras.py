
def function_decoradora(function_parametro):

    def interior():
        print("Vamos a realizar un calculo:")
        function_parametro()

        print("Hemos terminado el calculo")
    return interior


@function_decoradora
def suma():
    print(15+20)
    
def resta():
    print(20-10)

suma()
resta()