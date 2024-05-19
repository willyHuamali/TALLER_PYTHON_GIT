"""
6. Los alumnos de un curso se han dividido en dos grupos A y B de
acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres
con un nombre anterior a la M y los hombres con un nombre posterior a
la N y el grupo B por el resto. Escribir un programa que pregunte al
usuario su nombre y sexo, y muestre por pantalla el grupo que le
corresponde.
"""
print("PERTENCE AL GRUPO 'A' O GRUPO 'B' ")
M="Marculino"
F="Femenino"

nombre=str(input("ingrese nombre: "))
genero=str(input("selecione masculino [M] o femenino [F]: "))

if genero =="F":
    if nombre < str('M'):
        print(f'{nombre} es {F} y pertenece al grupo A')
    else: 
        print(f'{nombre} es {F} y pertenece al grupo B')
if genero =="M":
    if nombre > str('N'):
        print(f'{nombre} es {M} y pertenece al grupo A')
    else: 
        print(f'{nombre} es {M} y pertenece al grupo B')  
