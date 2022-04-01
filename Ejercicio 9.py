#Ejercicio 9 - Irazabal Ximena
#Titulo
import math
print ("Calculadora basica")
def suma (a,b):
    resultadosuma= (a + b)
    print (resultadosuma)
def resta (a,b):
    resta = (a-b)
    print (resta)
def division_entera (a,b):
    division_entera= (a//b)
    print (division_entera)
def multiplicacion (a,b):
    multiplicacion= (a*b)
    print (multiplicacion)
def exponencial (a,b):
    exponencial= (a**b)
    print (exponencial)
print ("Hola! Ingrese que operacion matematica quiere realizar:")
print ("1- Suma", "2- Resta", "3- Division", "4- Multiplicacion", "5- Potencial")
operacion= float(input())
if operacion ==1:
    print ("Ingrese los dos dijitos a sumar:")
    a= input()
    b= input()
    x= a.isdigit and b.isdigit #comprobacion
    if x: True
    a= float(a)
    b= float (b)
    print (suma (a,b))
if operacion ==2:
    print ("Ingrese los dos dijitos a restar:")
    a= input()
    b= input()
    x= a.isdigit and b.isdigit #comprobacion
    if x: True
    a= float(a)
    b= float (b)
    print (resta(a,b))
if operacion ==3:
    print ("Ingrese primero el numero a dividir, luego el divisor")
    a= input()
    b= input()
    x= a.isdigit and b.isdigit #comprobacion
    if x: True
    a= float(a)
    b= float (b) 
    print (division_entera(a,b))
if operacion ==4:
    print ("Ingrese los numeros a multiplicar")
    a= input()
    b= input()
    x= a.isdigit and b.isdigit #comprobacion
    if x: True
    a= float(a)
    b= float (b)
    print (multiplicacion(a,b))
if operacion==5:
    print("Ingrese primero la base, luego exponente")
    a= input()
    b= input()
    x= a.isdigit and b.isdigit #comprobacion
    if x: True
    a= float(a)
    b= float (b)
    print (exponencial(a,b))
