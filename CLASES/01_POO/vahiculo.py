class vehiculo:  #CLASE
    def __init__(self,marca,modelo,año): #CONSTRUCTOR
        self.marca1=marca
        self.modelo1=modelo
        self.año1=año

    def mostrar_info(self):
        print(f"Marca:{self.marca1} \nModelo: {self.modelo1} \nAño: {self.año1}")