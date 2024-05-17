"""
1. Escribir un programa que pida al usuario un número entero y muestre
por pantalla un triángulo rectángulo como el de más abajo, de altura el
número introducido.
"""
numero=int(input("ingrese numero: "))
i=1
print("EJEMPLO 1 CON WHILE")
while i <= numero:
    print(i*"*" )
    i=i+1
   
print("EJEMPLO 2 CON FOR")
for numero in range(1,numero+1):    
    print(numero*"*")