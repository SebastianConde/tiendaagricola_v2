from ui import crear_antibiotico

class Antibioticos:
    __antibioticos = []

    def __init__(self):
        nombre_producto, dosis, tipo_animal, valor_producto = crear_antibiotico()

        self.__nombre_producto = nombre_producto
        self.__dosis = dosis
        self.__tipo_animal = tipo_animal
        self.__valor_producto = valor_producto
        self.__class__.__antibioticos.append(self)
        print("-----------------------------")

    def obtener_valor(self):
        return self.__valor_producto

    def mostrar_producto(self):
        print("Nombre del producto: ", self.__nombre_producto)
        print("Dosis: ", self.__dosis)
        print("Tipo de animal: ", self.__tipo_animal)
        print("Valor del producto: ", self.__valor_producto)
        print("-----------------------------")

    def obtener_nombre_valor(self):
        print("Producto: {1} Valor: {0}.".format(self.__nombre_producto, self.obtener_valor()))

