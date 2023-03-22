def totalPersonasContagiadasNuncalandia(C:int, D:int) -> int:
    return C * (2**D)

if __name__ == "__main__":
  C = int(input("Ingrese la cantidad de personas contagiadas actualmente:"))
  D = int(input("Ingrese los días transcurridos:"))
  Total = totalPersonasContagiadasNuncalandia(C, D)
  print("La cantidad de personas contagiadas transcurridos "+str(D)+" días, es de "+ str(Total)+" personas")