"imprimir todos los elementos de la lista"

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
  
"imprimir todos los elemento con su posicion de referencia "

thislist1 = ["apple", "banana", "cherry"]
for i in range(len(thislist1)):
  print(thislist1[i])
  
"imprimir todos los elemento de la lista usando el ciclo while  "

thislist2 = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist2):
  print(thislist2[i])
  i = i + 1
  
"Un bucle for abreviado que imprimirá todos los elementos de una lista:"

thislist3 = ["apple", "banana", "cherry"]
[print(x) for x in thislist3]


"COMPRENSION DE LISTAS"
"""La comprensión de listas ofrece una sintaxis más corta cuando desea crear una nueva lista basada en
los valores de una lista existente.
Ejemplo:
Según una lista de frutas, desea una nueva lista que contenga solo las frutas con la letra "a" en el nombre.
Sin comprensión de listas, tendrás que escribir una declaración for con una prueba condicional dentro:"""

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

"Con la comprensión de listas puedes hacer todo eso con una sola línea de código:"
"syntaxis"
'newlist = [expression for item in iterable if condition == True]'

fruits1 = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits1 if "a" in x]

print(newlist)

"condicion para quitar un elemento de la lista"
newlist2 = [x for x in fruits1 if x != "apple"]
print(newlist2)