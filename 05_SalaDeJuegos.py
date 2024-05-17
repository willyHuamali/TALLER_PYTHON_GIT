""""
Escribir un programa para una empresa que tiene salas de juegos para
todas las edades y quiere calcular de forma automática el precio que
debe cobrar a sus clientes por entrar. El programa debe preguntar al
usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente
es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe
pagar 5€ y si es mayor de 18 años, 10€.
"""
def calcular_precio_entrada(edad):
    if edad < 4:
        return 0
    elif 4 <= edad <= 18:
        return 5
    else:
        return 10

def main():
    while True:
        try:
            edad = int(input("Por favor, introduzca la edad del cliente (0 para salir): "))
            if edad == 0:
                print("Gracias por usar nuestro programa. ¡Hasta luego!")
                break
            elif edad < 0:
                print("La edad no puede ser negativa. Por favor, introduzca una edad válida.")
            else:
                precio_entrada = calcular_precio_entrada(edad)
                print("El precio de la entrada es:", precio_entrada, "€")
        except ValueError:
            print("Por favor, introduzca una edad válida (número entero).")

if __name__ == "__main__":
    main()
