#Ejercicio 5 - Ximena Irazabal
print("Ingresar 3 numeros y elegir el mayor")
#bucle
a=1
while a==1:
    print("Que desea realizar")
    print("1-Agregar primer numero")
    print ("2- Agregar segundo numero")
    print ("3- Agregar 3 numero")
    print ("4- El mayor numero de los tres")
    print("0-Finalizar programa")
    x=float(input())
    #vacio
    if x==1:
        print ("Ingrese el primer numero:")
        s= float(input()) #variable del primer numero
    elif x==2:
        print ("Ingrese el segundo numero")
        d= float(input()) #variable del segundo numero
    elif x==3:
        print ("ingrese el tercer numero")
        f= float(input()) #variable del tercer numero
    elif x==4:
        numeros= [s,d,f] #lista de numeros ingresados
        max_numeros= max(numeros)
        print ("El mayor numero es", max_numeros)
        a=a+1
    elif x==0:
        print ("Fin del programa")
        a=a+1
    else:
        print ("Eleccion invalida")
        x=1