"""listanumneros=[1,2,3,7,5,8,7,8,9]
print(len(listanumneros))
print(min(listanumneros))
print(max(listanumneros))
print(listanumneros.count(2))  #muestra la cantidad de elementos 2
print(listanumneros.index(9))  # muestra la posicion """


# REPETIDOR

while True:
  palabra=input("ingrese palabra: ")
  if palabra=="salir":
      break
  if palabra=="nada":
      continue
  print(palabra)