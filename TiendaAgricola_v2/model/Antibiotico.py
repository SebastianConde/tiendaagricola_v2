class Antibioticos:
    def __init__(self, nombre_producto, dosis, tipo_animal, valor_producto):
        self.__nombre_producto = nombre_producto
        self.__dosis = dosis
        self.__tipo_animal = tipo_animal
        self.__valor_producto = valor_producto

    def obtener_valor(self):
        return self.__valor_producto

    def mostrar_producto(self):
        print("Nombre del producto: ", self.__nombre_producto)
        print("Dosis: ", self.__dosis)
        print("Tipo de animal: ", self.__tipo_animal)
        print("Valor del producto: ", self.__valor_producto)
        print("-----------------------------")

    def obtener_nombre(self):
        return self.__nombre_producto

    def actualizar_antibiotico(self, nombre_producto_despues, dosis_despues, tipo_animal_despues, valor_producto_despues):
        self.__nombre_producto = nombre_producto_despues
        self.__dosis = dosis_despues
        self.__tipo_animal = tipo_animal_despues
        self.__valor_producto = valor_producto_despues

    def eliminar(self):
        self.__nombre_producto = None
        self.__dosis = None
        self.__tipo_animal = None
        self.__valor_producto = None
        del self
