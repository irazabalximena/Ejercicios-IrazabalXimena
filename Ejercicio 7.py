#Titulo
print ("Cuestionario")
#Ejercicio 7 - Ximena Irazabal
#bucle
a=1
while a==1:
    print ("") #vacio
    print("Ingrese su nombre y apellido")
    n= str(input()) #Variable de nombre
    print ("Ingrese su edad")
    e= int(input ())
    if e<0 or e>100:
        print ("Error ---> La edad ingresada incorrecta")
        a=1
    print ("Ingrese el dinero que tiene en su billetera")
    b= float(input()) #variable del valor en su billetera
    if b<0:
        print ("No se puede realizar con valores negativos, vaya al cajero mas cercano, gracias")
        a=1
    print ("Indique del 1 al 10 el rango de hambre que tiene")
    h= int(input()) #variable del rango de hambre
    a=a+1
if e<(35):
    print ("Hola", n, "eres una persona joven, ya que tu edad es de", e, "años")
if e>(34) and b>500 and h>4:
    print ("Hola", n, "Hoy hay asado?")
if h>=(7) or b<(100) or e<(18):
    print("Vas a comer a lo de tus padres?")

