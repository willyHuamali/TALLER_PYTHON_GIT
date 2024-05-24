"""Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> 
entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por 
el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente."""

num1=int(input("ingrese primer numero:"))
num2=int(input("ingrese segundo numero:"))

cociente=int((num1/num2))
reciduo=num1-(cociente*num2)
r=num1%num2 #OTRA FORMA DE SCAR EL RECIDUO
print(f"el cociente de la division es: {cociente}")
print(f"el reciduo de la division es: {reciduo}")
print(f"el reciduo de la division es: {r}")