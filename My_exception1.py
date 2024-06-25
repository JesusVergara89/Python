import math as mt

def root(num):
    if num<0:
        raise ValueError("No se permiten numeros negativos")
    else:
        return mt.sqrt(num)

op=(int(input("digit a number: ")))


try:
    print(root(op))
except ValueError as Error_Negative_Number:
    print(Error_Negative_Number)