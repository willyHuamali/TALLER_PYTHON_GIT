#BUCLES LOOP
#Print all items in the list, one by one:

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)


# Break  -- rompe  el ciclo del for

lista=range(1,11)

for i in lista:
  if i>7:
    break
  print(i)
  
  
# continue  -- quita una parte de la condicion y continua el resto el ciclo del for  

lista =range(1,50,3)
for num in lista:
  if num >30 and num<=39:   # este rango quitara de la inpresion
    continue
  print(num)


# REPETIDOR
while True:
  palabra=input("ingrese palabra: ")
  if palabra=="salir":
      break
  if palabra=="nada":
      continue
  print(palabra)