"""
EJERCICIO 3
 Escribir un programa que pida al usuario un número entero positivo
mayor que 2 y muestre por pantalla si es un número primo o no.
"""
def es_primo(numero):
    if numero <= 1:
        return False
    elif numero <= 3:
        return True
    elif numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

while True:
    entrada = input("Ingresa un número (o 'F' para terminar): ")
    if entrada.upper() == 'F':
        break
    try:
        numero = int(entrada)
        if es_primo(numero):
            print(numero, "es un número primo.")
        else:
            print(numero, "no es un número primo.")
    except ValueError:
        print("Ingresa un número válido o 'F' para terminar.")
