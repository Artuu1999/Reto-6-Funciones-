from math import pi, sqrt

def areaSuperficialFigura(radioEsfera:float, radioCono:float, altura:float) -> float:
    areaEsfera = 4 * radioEsfera**2 * pi
    alturaInclinada = sqrt(radioCono**2 + altura**2)
    areaCono = (pi * radioCono * alturaInclinada) + (pi * radioCono**2)
    return areaCono + areaEsfera

def volumenFigura(radioEsfera:float, radioCono:float, altura:float) -> float:
    volumenEsfera = (4/3) * pi * radioEsfera**3
    volumenCono = (pi * radioCono**2 * altura) / 3
    return volumenEsfera + volumenCono

if __name__ == "__main__":
  radioEsfera = float(input("Ingrese el radio de la esfera en cm:"))
  radioCono = float(input("Ingrese el radio del cono en cm:"))
  altura = float(input("Ingrese altura del cono en cm:"))
  area = areaSuperficialFigura(radioEsfera, radioCono, altura)
  volumen = volumenFigura(radioEsfera, radioCono, altura)
  print("El area de la figura en centímetros es " + str(area))
  print("El volumen de la figura en centímetros es " + str(volumen))