"""Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta
por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el 
peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada
muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último
pedido y calcule el peso total del paquete que será enviado."""

print("Bienvenido a nuestro mundo de videojuegos")

cant_payasos = int(input("¿Cuántos payasos vas a vender? "))
cant_muñecas = int(input("¿Cuántas muñecas vas a vender? "))

mercaderia={'pasayos':112, 'muñecas':75}
total_peso=0
for producto,peso in mercaderia.items():
    
    print(producto, 'pesa: ', peso, 'kilos')
    total_peso += peso
   #total_peso+=peso*mercaderia[producto]*(payasos+muñecas)
print(f"El peso total del paquete es de gramos",total_peso)
        


