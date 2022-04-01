#Titulo
#Ejercicio 4 - Ximena Irazabal
print("Ingresar dos numeros y ver si el primero es divisible por el segundo")
#bucle
a=1
while a==1:
    print("Que desea realizar")
    print("1-Agregar primer numero")
    print ("2- Agregar segundo numero")
    print("0-Finalizar programa")
    x=float(input())
    #vacio
    if x==1:
        print ("Ingrese el primer numero:")
        v=float(input())
    elif x==2:
        print ("Ingrese el segundo numero")
        b=float(input())
        if b!=0 and v//b:
            c=v//b
            print ("el primer numero es divisible por el segundo numero")
            print ("¿Quiere ver el resultado de la division? S/N")
            r= str(input()) #Respuesta a la pregunta de ver o no el resultado
            if r=="S":
                 print("El valor de la razon es", c)
                 a=a+1
            elif r=="N":
                 print ("Fin del programa")
                 a=a+1
            else:
                print ("Dato invalido")
                x==1

        elif b==0:
            print ("el numero debe ser distinto de cero")
            x=2
        else:
            print ("El primer numero no es divisible por el segundo")
            a=a+1