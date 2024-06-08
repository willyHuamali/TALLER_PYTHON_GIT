from coche import Coche
from motocicleta import Motocicleta

def main():
    coche1= Coche("audi","R8 coupe", 2022, 2)
    motocicleta1= Motocicleta("yamaha","ymaaaa",2019,20.5)
    
    print("Mostrar informacion de coche:")
    #vehicculo.mostrar_info()
    coche1.mostrar_info()
    #print(coche1.mostrar_info)
    
    print("\nMostrar informacion de motocicleta:")
    #vehiculo.mostrar_info()
    motocicleta1.mostrar_info()
if __name__== "__main__":
    main()  