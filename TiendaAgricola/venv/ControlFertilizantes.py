from ProductoControl import ProductoControl

class ControlFertilizantes(ProductoControl):
    __lista_fertilizantes = []
    def __init__(self):
        super().__init__()
        self.__ultima_aplicacion = str(input("Ingrese la fecha de la ultima aplicación: "))
        self.__class__.__lista_fertilizantes.append(self)
        print("-----------------------------")

    def mostrar_producto(self):
        super().mostrar_producto()
        print("Fecha de última aplicación: ", self.__ultima_aplicacion)
        print("-----------------------------")

