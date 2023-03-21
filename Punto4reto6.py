def cantidadVueltas(P:int, M:int, H:int, B:float) -> float:
    return B - (P*300 + M*3300 + H*350)

if __name__ == "__main__":
  P = int(input("Ingrese la cantidad de panes:"))
  M = int(input("Ingrese la cantidad de leche:"))
  H = int(input("Ingrese la cantidad de huevos:"))
  B = float(input("Ingrese el valor del billete usado para pagar en pesos :"))
  Vueltas = cantidadVueltas(P, M, H, B)
  print("Las vueltas correspondientes al mandado son de "+ str(Vueltas)+" pesos")