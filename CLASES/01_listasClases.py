# TIPOS DE LISTAS 
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

thislist = list(("apple", "banana", "cherry","orange", "kiwi", "melon", "mango")) # note the double round-brackets
print(thislist)

print(thislist[1])  # imprimir posicion de una lista
print(thislist[:5]) #imprimir todo hasta la posicion 5

# Para la revision de las un objeto en una lista
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")
    
# para reemplazar una posicion por otro 
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)    

# para reemplazar los items desde la 1 hasta la psoision 3  
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# para Insertar "watermelon" en una posicion especifica como tercer elemento:

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# Usamos el metodo append() para agregar un elemento en la ultima posicion:

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Agregar los elementos de la lista tropical al final a la lista thislist:

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
"['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']"

# Agregar los elementos de una TUPLA a una LISTA:

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
"['apple', 'banana', 'cherry', 'kiwi', 'orange']"

# Para remover un elemento de una lista  "banana":

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
"['apple', 'cherry']"

# Remueve el primer elemento encontrado de "banana":

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
"['apple', 'cherry', 'banana', 'kiwi']"

# Remueve un especifico indice en este caso el segundo elemento:
# si no se especifica el indice remuve el ultimo elemento pop()

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
"['apple', 'cherry']"

# tambien se pude usar la palabra clave "del" para eliminar un elemento especifico.
# si no se especifica  el elemento se eleimnara todo los elementos de la lista
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
"['banana', 'cherry']"

# limpia el contenido de la lista:

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
"[]"

# OTROS
listanumneros=[1,2,3,7,5,8,7,8,9]
print(len(listanumneros))
print(min(listanumneros))
print(max(listanumneros))
print(listanumneros.count(2))  #muestra la cantidad de elementos 2
print(listanumneros.index(9))  # muestra la posicion 

listanumneros.sort()   #ordena la lista de menor a mayor
print(listanumneros)

listanumneros.reverse()  #ordena la lista de mayor a menor
print(listanumneros)