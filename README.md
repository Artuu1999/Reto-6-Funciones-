# Reto #6 Funciones 1

Espero que se encuentren excelente estimados lectores, en el presente repositorio haremos varios ejemplos de código en Python utilizando las funciones.

##  Ejemplo No. 1

```sh
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
```
![image](https://user-images.githubusercontent.com/124615034/226496094-1c47bc99-9718-413d-9dba-402d44374194.png)
El programa funcionando se ve de la siguiente manera:
![image](https://user-images.githubusercontent.com/124615034/226497100-62d2b76b-a53e-486b-b25a-ce12e04b8245.png)

##  Ejemplo No. 2

```sh
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
```
![image](https://user-images.githubusercontent.com/124615034/226497251-7c755e12-17db-4c41-93d4-3e764042958a.png)
De la siguiente manera se ve el programa ejecutado:
![image](https://user-images.githubusercontent.com/124615034/226503617-0d42a21f-a352-4390-a18e-79ded2c99625.png)

##  Ejemplo No. 3

```sh
def cantidadCarneAves(N:int, M:int, K:int) -> int:
    return N*6 + M*7 + K*1 

if __name__ == "__main__":
  N = int(input("Ingrese la cantidad de gallinas:"))
  M = int(input("Ingrese la cantidad de gallos:"))
  K = int(input("Ingrese la cantidad de pollitos:"))
  Total = cantidadCarneAves(N, M, K)
  print("La cantidad total de carne de aves es de "+ str(Total)+" kilogramos")
```
![image](https://user-images.githubusercontent.com/124615034/226768729-064c25c4-9844-4531-bc04-b670d0a18eec.png)
 El programa al ejecutarse se ve así:
 ![image](https://user-images.githubusercontent.com/124615034/226768849-53774eea-e37d-4272-a1c2-cf4e77b5b763.png)
 
##  Ejemplo No. 4

```sh
def cantidadVueltas(P:int, M:int, H:int, B:float) -> float:
    return B - (P*300 + M*3300 + H*350)

if __name__ == "__main__":
  P = int(input("Ingrese la cantidad de panes:"))
  M = int(input("Ingrese la cantidad de leche:"))
  H = int(input("Ingrese la cantidad de huevos:"))
  B = float(input("Ingrese el valor del billete usado para pagar en pesos :"))
  Vueltas = cantidadVueltas(P, M, H, B)
  print("Las vueltas correspondientes al mandado son de "+ str(Vueltas)+" pesos")
```
![image](https://user-images.githubusercontent.com/124615034/226768989-1a321c7b-18e0-4e43-b3c7-0f0a93ceff0c.png)
De la siguiente forma el programa se ejecuta:
![image](https://user-images.githubusercontent.com/124615034/226769175-73d142d0-2d31-4585-a815-0cd19e0dd9e9.png)
 
##  Ejemplo No. 5

```sh
def valorPrestamo(capitalFinal:float, tasaDeInteres:float, tiempo:int) -> float:
    interes = (tasaDeInteres/100)/ 12
    return capitalFinal/((1 + interes)**tiempo)

if __name__ == "__main__":
  capitalFinal = float(input("Ingrese el valor pagado:"))
  tasaDeInteres = float(input("Ingrese la tasa de interes anual fijada para el prestamo:"))
  tiempo = int(input("Ingrese la cantidad de cuotas pagadas:"))
  prestamo = valorPrestamo(capitalFinal, tasaDeInteres, tiempo)
  print("El prestamo realizado fue por un valor de "+ str(prestamo)+" pesos")
```
![image](https://user-images.githubusercontent.com/124615034/226769382-27685788-a27d-4c57-bf00-3789c8a1457f.png)
De la siguiente manera se ve al ejecutar el programa diseñado:
![image](https://user-images.githubusercontent.com/124615034/226769544-43e76834-22f3-4b21-a962-dd9d5c82349c.png)
 
##  Ejemplo No. 6

```sh
def totalPersonasContagiadasNuncalandia(C:int, D:int) -> int:
    return C * (2**D)

if __name__ == "__main__":
  C = int(input("Ingrese la cantidad de personas contagiadas actualmente:"))
  D = int(input("Ingrese los días transcurridos:"))
  Total = totalPersonasContagiadasNuncalandia(C, D)
  print("La cantidad de personas contagiadas transcurridos "+str(D)+" días, es de "+ str(Total)+" personas")
```
![image](https://user-images.githubusercontent.com/124615034/226769698-82836fe4-22de-4ed7-815e-25adf9ad0fff.png)
Programa ejecutado:
![image](https://user-images.githubusercontent.com/124615034/226769825-9567d9db-2a72-435f-843c-805c67a9757c.png)
 
##  Ejemplo No. 7

```sh
from funcionesaritméticas import promedio
```

##  Ejemplo No. 8

```sh
# Se declaran las variables que va se van a utilizar en el programa
a:float
b:float 
c:float
d:float
e:float
m1:float
m2:float
m3:float
m4:float
m5:float
promedio : float
potencia : float
promult : float 
raizm : float 
# Se pide lque se ingresen los 5 números reales 
a = float(input("Ingrese el primer número real: "))
b = float(input("Ingrese el segundo número real: "))
c = float(input("Ingrese el tercer número real: "))
d = float(input("Ingrese el cuarto número real: "))
e = float(input("Ingrese el quinto número real: "))
# El programa nos imprimira los números ingresados 
print ("los números ingresados son ("+ str(a)+ ", "+ str(b)+", "+ str(c)+ ", "+str(d)+ ", "+str(e) +")" )
# Se calcula el promedio por lo que se dividira los suma de los números ingresados por 5 que es la 
# la cantidad de tatos que se tienen que ingresar 
promedio = (a+b+c+d+e)/5
# se imprime el resultado del promedio 
print("El promedio es "+ str(promedio))
# se utilizan  condicionales para indicarnos cual variable es menor que otra y hacirla a esta variable un
# nuevo nombre la mas pequeña sera m1, luego m2, m3 m4 y  m5 que sera la mas grande 
if a<=b and a<=c and a<=d and a<=e:
    m1=a
    if b<=c and b<d and b<=e:
       m2=b
       if c<=d and c<=e:
          m3=c
          if d<=e:
             m4=d ; m5=e 
          else : 
             m4=e ; m5=d 
    elif c<=b and c<=d and c<=e:
       m2=c
       if b<=d and b<=e:
          m3=b
          if d<=e:
             m4=d ; m5=e 
          else : 
             m4=e ; m5=d 
    elif d<=b and d<=c and d<=e:
       m2=d
       if b<=c and b<=e:
          m3=b
          if c<=e:
              m4=c ; m5=e 
          else : 
             m4=e ; m5=c
    elif e<=b and e<=c and e<=d:
       m2=e
       if b<=c and b<=d:
          m3=b
          if b<=d:
              m4=b ; m5=d
          else : 
             m4=d ; m5=b 
elif b<=a and b<=c and b<=d and b<=e:
    m1=b
    if a<=c and a<=d and a<=e:
       m2=a 
       if c<=d and c<=e:
          m3=c
          if d<=e:
             m4=d ; m5=e 
          else : 
             m4=e ; m5=d 
    elif c<=a and c<=d and c<=e:
       m2=c
       if a<=d and a<=e:
          m3=a
          if d<=e:
             m4=d ; m5=e 
          else : 
             m4=e ; m5=d 
    elif d<=a and d<=c and d<=e:
       m2=d
       if a<=c and a<e:
          m3=a
          if c<=e:
              m4=c ; m5=e 
          else : 
             m4=e ; m5=c
    elif e<=a and e<=c and e<=d:
       m2=e
       if a<c and a<d:
          m3=a
          if a<=d:
              m4=a ; m5=d 
          else : 
             m4=d ; m5=a
if c<=b and c<=a and c<=d and c<=e:
    m1=c
    if b<=a and b<=d and b<=e:
       m2=b 
       if a<=d and a<=e:
          m3=a
          if d<=e:
             m4=d ; m5=e 
          else : 
             m4=e ; m5=d 
    elif a<=b and a<=d and a<=e:
       m2=a
       if b<=d and b<=e:
          m3=b
          if d<=e:
             m4=d ; m5=e 
          else : 
             m4=e ; m5=d 
    elif d<=b and d<=a and d<=e:
       m2=d
       if b<=a and b<=e:
          m3=b
          if a<e:
              m4=a ; m5=e 
          else : 
             m4=e ; m5=a 
    elif e<=b and e<=a and e<=d:
       m2=e
       if b<=a and b<=d:
          m3=b
          if b<d:
              m4=b ; m5=d 
          else : 
             m4=d ; m5=b
if d<=b and d<=c and d<=a and d<=e:
    m1=d
    if b<=c and b<=a and b<=e:
       m2=b 
       if c<=a and c<=e:
          m3=c
          if a<e:
              m4=a ; m5=e 
          else : 
             m4=e ; m5=a 
    elif c<=b and c<=a and c<=e:
       m2=c
       if b<=a and b<=e:
          m3=b
          if d<=e:
            if d<=e:
             m4=d ; m5=e 
          else : 
             m4=e ; m5=d 
    elif a<=b and a<=c and a<=e:
       m2=a
       if b<=c and b<=e:
          m3=b
          if c<=e:
              m4=c ; m5=e 
          else : 
             m4=e ; m5=c
    elif e<=b and e<=c and e<=a:
       m2=e
       if b<=c and b<=a:
          m3=b
          if b<=a:
              m4=b ; m5=a 
          else : 
             m4=a ; m5=b
if e<=b and e<=c and e<=d and e<=a:
    m1=e
    if b<=c and b<=d and b<=a:
       m2=b 
       if c<=d and c<=a:
          m3=c
          if d<=a:
              m4=d ; m5=a 
          else : 
             m4=a ; m5=d 
    elif c<=b and c<=d and c<=a:
       m2=c
       if b<=d and b<=a:
          m3=b
          if d<=a:
              m4=d ; m5=a 
          else : 
             m4=a ; m5=d 
    elif d<=b and d<=c and d<=a:
       m2=d
       if b<=c and b<=a:
          m3=b
          if c<=a:
              m4=c ; m5=a 
          else : 
             m4=a ; m5=c 
    elif a<=b and a<=c and a<=d:
       m2=a
       if b<=c and b<=d:
          m3=b
          if b<=d:
              m4=b ; m5=d 
          else : 
             m4=d ; m5=b  
# Se calcula la potencia del numero mayor elavado al menor
potencia = m5**m1
# se calcula el promedio multiplicativo
promult= (m1*m2*m3*m4*m5)**(1/5)
# se calcula la raiz del número menor 
raizm = (m1)**(1/2)
# se imprimen los resultados 
print("la mediana es "+ str(m3))
print("El promedio multilpicativo es "+ str(promult))
print("los numeros en orden descendente son ("+ str(m5)+ ", "+ str(m4)+", "+ str(m3)+ ", "+str(m2)+ ", "+str(m1) +")") 
print("los numeros en orden ascendente son ("+ str(m1)+ ", "+ str(m2)+", "+ str(m3)+ ", "+str(m4)+ ", "+str(m5) +")") 
print("la potencia del mayor numero elvado el menor numero  es "+ str(potencia))
print("la raiz del menor número es " + str (raizm))
```
Al ejecutar el programa se ve de la siguiente manera
![image](https://user-images.githubusercontent.com/124615034/226770179-5caad4ca-e5ef-4fb9-87c9-4ba78a8a510a.png)
