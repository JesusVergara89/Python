class Areas:
  """
  this is a class that get inside a bunch of functions that calculate the area of differents geometric figures
  """
  def areaCuadrado(lado):
     """
     This function take a int and return the area of the square figure of side lado
     """
     return "EL area de cuadrado es: " + str(lado*lado)

  def areaTriangulo(base, altura):
     return "EL area de triangulo es: " + str((base*altura)/2)



help(Areas)