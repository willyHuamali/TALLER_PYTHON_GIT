"""3. Escribir un programa que pida al usuario un número entero positivo
mayor que 2 y muestre por pantalla si es un número primo o no."""

def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            print(f'El numero {num} No es primo, es divisible por {n}')
            return False
    print(f'El numero {num} Es primo :)')
    return True

num=int(input("ingrese numero: "))
print(es_primo(num))

