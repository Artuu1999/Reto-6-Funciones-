from funcionesaritméticas import promedio

if __name__ == "__main__":
  a = float(input("Ingrese un numero real:"))
  b = float(input("Ingrese un numero real:"))
  c = float(input("Ingrese un numero real:"))
  d = float(input("Ingrese un numero real:"))
  e = float(input("Ingrese un numero real:"))
  media = promedio(a, b, c, d, e)
  print("El promedio es de " + str(media))