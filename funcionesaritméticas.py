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