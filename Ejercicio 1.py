from pickle import LIST
#Titulo
print ("Cursada aprobada o desaprobada")
#Ejercicio 1 - Ximena Irazabal

print ("Indique la materia que quiere calificar")
materias = ["1-Fisica", "2-Lengua", "3-Matematica", "4-Quimica"]
nota=[]
a=1
while a==1:
    print("")#vacio
    print("Las materias son:")
    print (materias)
    print ("Elija la materia que quiere ingresar la nota")
    print("0-Finalizar programa.")
    x=float(input())
    d=1 #Variable para materia aprobada o desaprobada
    if x==1:
        print("Ingrese nota del primer parcial")
        nota1= float(input())
        print("Ingrese nota del segundo parcial")
        nota2= float(input())
        print("Ingrese nota del tercer parcial")
        nota3= float(input())
        nota.append([nota1,nota2,nota3])
        suma=(nota1 +nota2+nota3)
        promedio= suma/3
        print("Su promedio es de:", promedio)
        if promedio >=8:
            print("Promocionado")
            f=0
        elif promedio >=6 and promedio <8:
            print ("Aprobado, debe rendir final ")
            f=0

        else :
             print("Desaprobado")
             f=1
        
    elif x==2:
        print("Ingrese nota del primer parcial")
        nota1= float(input())
        print("Ingrese nota del segundo parcial")
        nota2= float(input())
        print("Ingrese nota del tercer parcial")
        nota3= float(input())
        nota.append([nota1,nota2,nota3])
        suma=(nota1 +nota2+nota3)
        promedio= suma/3
        print("Su promedio es de:", promedio)
        if promedio >=8:
            print("Promocionado")
            l= 0
        elif promedio >=6 and promedio <8:
            print ("Aprobado, debe rendir final ")
            l= 0
        else :
             print("Desaprobado")
             l= 1
    elif x==3:
        print("Ingrese nota del primer parcial")
        nota1= float(input())
        print("Ingrese nota del segundo parcial")
        nota2= float(input())
        print("Ingrese nota del tercer parcial")
        nota3= float(input())
        nota.append([nota1,nota2,nota3])
        suma=(nota1 +nota2+nota3)
        promedio= suma/3
        print("Su promedio es de:", promedio)
        if promedio >=8:
            print("Promocionado")
            q= 0
        elif promedio >=6 and promedio <8:
            print ("Aprobado, debe rendir final ")
            q= 0
        else :
             print("Desaprobado")
             q= 1
        
    elif x==4:
        print("Ingrese nota del primer parcial")
        nota1= float(input())
        print("Ingrese nota del segundo parcial")
        nota2= float(input())
        print("Ingrese nota del tercer parcial")
        nota3= float(input())
        nota.append([nota1,nota2,nota3])
        suma=(nota1 +nota2+nota3)
        promedio= suma/3
        print("Su promedio es de:", promedio)
        if promedio >=8:
             print("Promocionado")
             m=0
        elif promedio >=6 and promedio <8:
             print ("Aprobado, debe rendir final ")
             m=0
        else :
             print("Desaprobado")
             m=1 
        a= a+1 #cerrar bucle 
    elif x==0:
         print("Fin del programa")
         print("")#vacio
         a=a+1
    
    else:
        print ("opcion invalida, ingrese una opcion valida")
        print("")#vacio
d= (f+l+m+q) #Variables si se desaprueba la materia
if d<3:
    print ("Cursada aprobada")
else:
    print ("Cursada desaprobada")
