class ProductoControl:
    __productos_control = []

    def __init__(self, registro_ICA, nombre_producto, frecuencia_aplicacion, valor_producto):

        self.__registro_ICA = registro_ICA
        self.__nombre_producto = nombre_producto
        self.__frecuencia_aplicacion = frecuencia_aplicacion
        self.__valor_producto = valor_producto
        self.__class__.__productos_control.append(self)

    def actualizar_producto_control(self, registro_ICA_despues, nombre_producto_despues, frecuencia_aplicacion_despues, valor_producto_despues):
        self.__registro_ICA = registro_ICA_despues
        self.__nombre_producto = nombre_producto_despues
        self.__frecuencia_aplicacion = frecuencia_aplicacion_despues
        self.__valor_producto = valor_producto_despues

    def obtener_registro_ICA(self):
        return self.__registro_ICA

    def mostrar_producto(self):
        print("Registro ICA: ", self.__registro_ICA)
        print("Nombre del producto: ", self.__nombre_producto)
        print("Frecuencia de aplicación: ", self.__frecuencia_aplicacion)
        print("Valor del producto: ", self.__valor_producto)

    def obtener_valor(self):
        return self.__valor_producto

