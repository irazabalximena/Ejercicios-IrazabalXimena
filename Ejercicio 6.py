from os import sep
#Titulo
#Ejercicio 6 - Ximena Irazabal
print("Listado de amigxs")

amigos= str(" ")
while True:
    print("Ingrese el nombre de su amigo o amiga, para finalizar ingrese: exit")
    nombre= str(input())
    if nombre == "exit":
        break
    amigos += (nombre + "-")

print(amigos)

