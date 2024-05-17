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

def principal():
    numero = int(input("Ingrese un número entero positivo mayor que 2: "))
    if numero <= 2:
        print("El número ingresado no es mayor que 2")
        return
    if es_primo(numero):
        print(f"{numero} es un número primo")
    else:
        print(f"{numero} no es un número primo")

principal()
