from vahiculo import vehiculo

class Coche(vehiculo):
    def __init__(self,marca,modelo,año,puertas): #ANADIMOS PUERTA
        super().__init__(marca,modelo,año) # SUEPER HEREDA DE CLASE CREADA
        self.puertas=puertas
        
    def mostrar_info(self):
        super().mostrar_info()  # SUEPER HEREDA DE CLASE CREADA
        print(f'N° de Puerta del vehiculo:{self.puertas}')
    



