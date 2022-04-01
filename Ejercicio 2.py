#Titulo
#Ejercicio 2 - Ximena Irazabal
print("Area de un triangulo")
#bucle
a=1
while a==1:
    print ("") #vacio
    print("Que desea realizar")
    print("1-Calcular el area de un triangulo")
    print("0-Finalizar programa")
    x=float(input())
    
    if x==1:
        print("")#vacio
        print ("Ingrese la altura del triangulo, en metros")
        a=float(input()) #variable de altura
        if a<0:
            print ("El valor ingresado de la altura es negativo")
            print("")#vacio
            x=1
        elif a>0:
            print ("Ingrese la base del triangulo, en metros")
            b=float(input()) #variable de base
            if b<0:
                print ("El valor ingresado de la base es negativo")
                x=1
            elif b>0:
                v=(a*b)/2
                print("")#vacio
                print("El area del triangulo es",v, "mts")
                print ("") #vacio
    elif x==0:
        print ("") #vacio
        print ("Fin del programa")
        print ("") #vacio
        a=a+1
        
    else:
        print ("opcion invalida, ingrese una opcion valida")
        print("")#vacio