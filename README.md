# Reto #6 Funciones 1

Espero que se encuentren excelente estimados lectores, en el presente repositorio haremos varios ejemplos de código en Python utilizando las funciones.

##  Ejemplo No. 1
Se debe diseñar un código que dearrolle una función para cálcular el área superficial y el volumen de la siguiente figura:

![image](https://user-images.githubusercontent.com/124615034/226771682-a8274912-9c8d-4057-add2-fba0b1c817eb.png)

Para ello debemos tener en cuenta las fórmulas para hallar el área supericial y el volumen de una esfera y de un cono

> Área Superficial Esfera: 4*π*r²

> Volumen Esfera: 1/3hπr²

> Área Superficial Cono: πrl + πr²

> Volumen Esfera: V = 4/3 πr³

El código solución al anterior problema se presenta a continuación

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
Se debe desarrollar una función matemática que resuelva el área y perímetro de la siguiente figura:

![image](https://user-images.githubusercontent.com/124615034/226773245-eec6d80c-ffae-42c4-ada9-72718c707870.png)

Para ello debemos tener en cuenta las fórmulas para hallar el área y el perímetro de una circunferencia y de un rectángulo

> Perímetro Rectángulo: 2b+2h

> Área Rectángulo: b*h

> Perímetro Circunferencia: 2πr

> Área Circunferencia: πr²

El pseudocódigo que resuelve el problema de áreas y perímetro de la figura, es el siguiente:
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
Ahora bien se debe diseñar un programa en Python que contenga la función que relacione la cantidad de aves (gallinas, gallos y pollitos) con su respectivo peso (6 kg, 7 kg y 1 kg) y que al sumar dichas relaciones nos indique la cantidad total de carne de aves.
El programa se ejecuta de una manera óptima mediante el uso del siguiente código:

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
A continuación se debe crear un código, el cual al ejecutarlo me imprima la solución al siguiente problema:

+ Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a 3300 cada una y H huevos a 350 cada uno. Cual es el valor de las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.

El siguiente pseudocódigo contiene la solución al problema
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
El interés compuesto es un tipo de préstamo que acumula intereses, la fórmula básica de dicho concepto financiero es:
> Cf= Ci (1+i)^n

El siguiente código al ejecutarse muestra el capital inicial, es decir el dinero prestado, mediante el uso de la fórmula del interes compuesto, utilizando las variables del capital total pagado, la tasa de interés anual y la cantidad de cuotas pagadas.
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
El crecimiento exponencial es un tipo de crecimiento en el que la tasa de crecimiento aumenta constantemente en función del tamaño actual de una cantidad.
En este caso si el número de contagiados aumenta exponencialmente, duplicandose cada día la cantidad, la función que se usará es la siguiente:
> C x 2^D

Siendo C la cantidad de contagiados actual y D la cantidad de días transcurridos
El código solución es el siguiente:
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
Se importaron las funciones del archivo independiente funcionesaritméticas.py
```sh
from funcionesaritméticas import promedio
```

##  Ejemplo No. 8
Este archivo contiene los códigos que solucionan el promedio, la mediana, el promedio multiplicativo, el orden ascendente y descendente, la potencia del mayor número elevado al menor y la raíz cúbica del menor; todo aquellos con 5 números reales ingresados por el usuario
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

##  PIP en Python
Pip es un sistema de gestión de paquetes en Python, el cual se encarga de instalar, administrar y analizar paquetes software y módulos no incluidos en Python, es decir adiciona funciones útiles para la realización de tareas, el manejo de datos, el diseño específico, la creación de gráficas, entre otras utilidades.
Su uso se facilita en cierta manera, ya que se puede encontrar formatos de código en la web, disponibles para el uso de todo programador. Además para instalar un paquete basta con colocar el comando  
```sh
`pip install + nombre del módulo`
```
para ya comenzar a disfrutar de las funciones incluidas del paquete instalado

##  Módulos populares de PIP en Python

* Numpy: Usada para realizar operaciones matemáticas
```sh
`pip install numpy`
```
* Pandas: Útil en la gestión de datos
```sh
`pip install pandas
```
* Matplotlib: Visualiza datos y gráficos
```sh
`pip install matplotlib`
```
* Scikit-learn: Realiza aprendizaje autónomo
```sh
`pip install scikit-learn`
```
* Requests: Envía solicitudes HTTP a sitios web
```sh
`pip install requests`
```
* TensorFlow: Desarrolla modelos de aprendizaje complejos
```sh
`pip install tensorflow`
```
* Django: Útil en el desarrollo de aplicaciones web
```sh
`pip install django`
```
* Flask: Útil en el desarrollo de aplicaciones web pequeñas y medianas
```sh
`pip install flask`
```
* Pygame: Es usada para el desarrollo de videojuegos
```sh
`pip install pygame`
```

## FIN
Hasta acá llega nuestro camino en el presente repo, espero que haya sido de tu interés, si encuentras algún error o alguna inconsistencia, no dudes en contactarme y hacermela saber.

   **"Cuando todo parece ir en tu contra, recuerda que el avión despega con el viento en contra, no a favor"**
         - Henry Ford
