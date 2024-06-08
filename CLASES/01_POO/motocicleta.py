from vahiculo import vehiculo

class Motocicleta(vehiculo):
    def __init__(self,marca,modelo,año,precio):
        super().__init__(marca,modelo,año)
        self.precio=precio
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f'EL Precio es: ´{self.precio}')
        