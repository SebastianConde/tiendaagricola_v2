from .ProductoControl import ProductoControl

class ControlFertilizantes(ProductoControl):
    def __init__(self, registro_ICA, nombre_producto, frecuencia_aplicacion, valor_producto, ultima_aplicacion):
        super().__init__(registro_ICA, nombre_producto, frecuencia_aplicacion, valor_producto)
        self.__ultima_aplicacion = ultima_aplicacion

    def obtener_registro_ICA(self):
        return super().obtener_registro_ICA()

    def actualizar_fertilizante(self, registro_ICA_despues, nombre_producto_despues, frecuencia_aplicacion_despues, valor_producto_despues, ultima_aplicacion_despues):
        self.actualizar_producto_control(registro_ICA_despues, nombre_producto_despues, frecuencia_aplicacion_despues, valor_producto_despues)
        self.__ultima_aplicacion = ultima_aplicacion_despues

    def eliminar(self):
        self.actualizar_producto_control(None, None, None, None)
        self.__ultima_aplicacion = None
        del self

    def mostrar_producto(self):
        super().mostrar_producto()
        print("Fecha de última aplicación: ", self.__ultima_aplicacion)
        print("-----------------------------")

