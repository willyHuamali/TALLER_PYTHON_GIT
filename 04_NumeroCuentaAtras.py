"""
 EJERCICIO NUMERO 4
4. Escribir un programa que pida al usuario un número entero positivo y
muestre por pantalla la cuenta atrás desde ese número hasta cero
separados por comas.
"""

numero = int(input("ingrese un numero:"))
i=0
while i <= numero:
    print(f'{numero}')
    numero=numero-1

#########################

n1 = int(input("Ingresa un número hasta el que deseas contar: "))


if n1 < 0:
        print("Por favor, introduce un número entero positivo.")
else:
    cuenta_atras = [str(i) for i in range(n1, -1, -1)]
    print(", ".join(cuenta_atras))