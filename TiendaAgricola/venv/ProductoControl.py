from ui import crear_producto_control

class ProductoControl:
    __productos_control = []

    def __init__(self):
        registro_ICA, nombre_producto, frecuencia_aplicacion, valor_producto = crear_producto_control()

        self.__registro_ICA = registro_ICA
        self.__nombre_producto = nombre_producto
        self.__frecuencia_aplicacion = frecuencia_aplicacion
        self.__valor_producto = valor_producto
        self.__class__.__productos_control.append(self)


    def mostrar_producto(self):
        print("Registro ICA: ", self.__registro_ICA)
        print("Nombre del producto: ", self.__nombre_producto)
        print("Frecuencia de aplicación: ", self.__frecuencia_aplicacion)
        print("Valor del producto: ", self.__valor_producto)

    def obtener_valor(self):
        return self.__valor_producto

    def obtener_nombre_valor(self):
        print("Producto: {0} Valor: {1}.".format(self.__nombre_producto, self.obtener_valor()))

