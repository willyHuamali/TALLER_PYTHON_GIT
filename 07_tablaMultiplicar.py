"""
7. Escribir un programa que muestre por pantalla la tabla de multiplicar del
1 al 10.
"""

for i in range (1,11):
    print(f"tabla de multiplicar de {i} ")
    for j in range(1,11):
        r=i*j
        print(f'El Producto {i} x {j} : {r} ')
        j=j+1
    i=i+1
    print()

"""
def tabla_multiplicar():
    for i in range(1, 11):  # Para cada número del 1 al 10
        print(f"Tabla de multiplicar del {i}:")
        for j in range(1, 11):  # Multiplicar por cada número del 1 al 10
            resultado = i * j
            print(f"{i} x {j} = {resultado}")
        print()  # Salto de línea para separar las tablas

tabla_multiplicar()

"""