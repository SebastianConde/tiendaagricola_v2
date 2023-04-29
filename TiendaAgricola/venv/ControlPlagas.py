from ProductoControl import ProductoControl

class ControlPlagas(ProductoControl):
    __lista_plagas = []
    def __init__(self):
        producto_control = super().__init__()
        self.__periodo_carencia = str(input("Ingrese el periodo de carencia del control de plagas: "))
        self.__class__.__lista_plagas.append(self)
        print("-----------------------------")

    def mostrar_producto(self):
        super().mostrar_producto()
        print("Periodo de carencia: ", self.__periodo_carencia)
        print("-----------------------------")
