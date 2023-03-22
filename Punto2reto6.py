from math import pi, sqrt

def areaFigura(radioCirculo:float, altura:float, base:float) -> float:
    areaCirculo = pi * radioCirculo**2 * 2
    areaRectangulo = base * altura
    return areaCirculo + areaRectangulo

def perimetroFigura(radioCirculo:float, altura:float, base:float) -> float:
    perimetroCirculo = 2 * 2 * pi * radioCirculo
    perimetroRectangulo = (altura * 2) + (base * 2)
    return perimetroCirculo + perimetroRectangulo

if __name__ == "__main__":
  radioCirculo = float(input("Ingrese el radio del círculo en cm:"))
  altura = float(input("Ingrese la altura del rectángulo en cm:"))
  base = float(input("Ingrese la base del rectángulo en cm:"))
  area = areaFigura(radioCirculo, altura, base)
  perimetro = perimetroFigura(radioCirculo, altura, base)
  print ("El area de la figura es "+str(area)+" centímetros")
  print ( "El perímetro de la figura es "+ str(perimetro)+" centímetros")