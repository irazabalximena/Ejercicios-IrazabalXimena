#Ejercicio 10- Irazabal Ximena 
#Titulo
import random
from tkinter import N

intentos=0
numero =random.randint(1, 10)
print ("Adivina adivinador")
print ("Bienvenid@, ingresa tu nombre:")
n=str(input())
print ("Adivina el numero entre 1 al 10 inclusive")
while intentos<5:
    print ("En que numero estas pensando?")
    adivinado= int(input())
    intentos= intentos+1
    if adivinado<numero:
        intentosrestantes= 5-intentos
        print ("Tienes", intentosrestantes, "intentos restantes")
        print ("Piensa en un numero mas grande")
        print ("") #vacio
    if adivinado>numero:
        intentosrestantes= 5-intentos
        print ("Tienes", intentosrestantes, "intentos restantes")
        print ("Piensa en un numero mas pequeño")
        print ("") #vacio
    if adivinado==numero:
        break
if intentos==5:
    print ("Oh no, juego terminado")
if adivinado==numero and intentos<5:
    print ("Excelente!",n, "has podido adivinar el numero en",intentos, "intentos!")