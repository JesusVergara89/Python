
# areaTriangulo(base, altura):
#    return "EL area de triangulo es: " + str((base*altura)/2)

def areaTriangulo(base, altura):
    """
    Calcula el area de un triangulo
    >>> areaTriangulo(3,6)
    'EL area de triangulo es: 9.0'

    >>> areaTriangulo(4,5)
    'EL area de triangulo es: 10.0'

    >>> areaTriangulo(9,3)
    'EL area de triangulo es: 13.5'
    """
    return "EL area de triangulo es: " + str((base*altura)/2)


import doctest 

doctest.testmod() 