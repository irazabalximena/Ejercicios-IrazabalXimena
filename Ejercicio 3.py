#Ejercicio 3 - Ximena Irazabal
#Titulo
print("Multiplos y sumas de un numero")
#bucle
a=1
while a==1:
    c= 3
    suma= 0
    mult= 0
    print("Que desea realizar")
    print("1-Ver multiplos")
    print("0-Finalizar programa")
    x=float(input())
    
    if x==1:
        print("Ingrese el numero a evaluar")
        z=float(input())
        if z<3:
            print("")#vacio
            print("No existen multiplos de 3 del numero ingresado")
        elif z>=3 and z<100:
            print ("Los multiplos son:")
            while z>=c:
                print ("")#vacio
                print(c)
                print ("")#vacio
                c=c+3
        elif z==100:
            print ("El numero ingresado debe ser menor a 100")
    elif x==0:
        print("Fin del programa")
        a=a+1        
    
    else:
        print ("opcion invalida, ingrese una opcion valida")
        print("")#vacio
            