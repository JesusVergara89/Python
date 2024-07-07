import math

def raizCuadrada(lista):
    """
    La raiz devuelve una lista de la raiz cuadrada de los elementos

    >>> lista=[]
    >>> for i in [4,9,16]:
    ...      lista.append(i)
    >>> raizCuadrada(lista)
    [2.0, 3.0, 4.0]

    >>> lista=[]
    >>> for i in [4,-2,16]:
    ...      lista.append(i)
    >>> raizCuadrada(lista)
    Traceback (most recent call last):
        ...
    ValueError: math domain error

    """

    return [math.sqrt(n) for n in lista]


import doctest
doctest.testmod()