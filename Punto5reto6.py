def valorPrestamo(capitalFinal:float, tasaDeInteres:float, tiempo:int) -> float:
    interes = (tasaDeInteres/100)/ 12
    return capitalFinal/((1 + interes)**tiempo)

if __name__ == "__main__":
  capitalFinal = float(input("Ingrese el valor pagado:"))
  tasaDeInteres = float(input("Ingrese la tasa de interes anual fijada para el prestamo:"))
  tiempo = int(input("Ingrese la cantidad de cuotas pagadas:"))
  prestamo = valorPrestamo(capitalFinal, tasaDeInteres, tiempo)
  print("El prestamo realizado fue por un valor de "+ str(prestamo)+" pesos")