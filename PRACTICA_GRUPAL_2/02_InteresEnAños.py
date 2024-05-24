# EJERCICIO NUMERO DE 2
"""Escribir un programa que pregunte al usuario una cantidad a invertir, el
interés anual y el número de años, y muestre por pantalla el capital
obtenido en la inversión cada año que dura la inversión """
print("EJERCICIO 2")

monto=int(input("ingrese monto a invertir: "))
taza=int(input("ingrese el poncetaje de interes:"))
años=int(input("ingrese numero de años: "))

print("Capital final: " + str(round(monto * (taza / 100 + 1) ** años, 2)))
i=1
while i <= años:
    interes=round((monto*taza)/100,2)
    monto=round(monto+interes,2)
    print(f'El capital mas el interes {interes} en el año {i} es igual a: {monto}')
    i=i+1


