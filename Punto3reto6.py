def cantidadCarneAves(N:int, M:int, K:int) -> int:
    return N*6 + M*7 + K*1 

if __name__ == "__main__":
  N = int(input("Ingrese la cantidad de gallinas:"))
  M = int(input("Ingrese la cantidad de gallos:"))
  K = int(input("Ingrese la cantidad de pollitos:"))
  Total = cantidadCarneAves(N, M, K)
  print("La cantidad total de carne de aves es de "+ str(Total)+" kilogramos")