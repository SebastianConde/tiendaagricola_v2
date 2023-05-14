from .ProductoControl import ProductoControl

class ControlPlagas(ProductoControl):
    def __init__(self, registro_ICA, nombre_producto, frecuencia_aplicacion, valor_producto, periodo_carencia):
        super().__init__(registro_ICA, nombre_producto, frecuencia_aplicacion, valor_producto)
        self.__periodo_carencia = periodo_carencia

    def obtener_registro_ICA(self):
        return super().obtener_registro_ICA()

    def actualizar_plaga(self, registro_ICA_despues, nombre_producto_despues, frecuencia_aplicacion_despues, valor_producto_despues, periodo_carencia_despues):
        self.actualizar_producto_control(registro_ICA_despues, nombre_producto_despues, frecuencia_aplicacion_despues, valor_producto_despues)
        self.__periodo_carencia = periodo_carencia_despues

    def eliminar(self):
        self.actualizar_producto_control(None, None, None, None)
        self.__periodo_carencia = None
        del self

    def mostrar_producto(self):
        super().mostrar_producto()
        print("Periodo de carencia: ", self.__periodo_carencia)
        print("-----------------------------")
