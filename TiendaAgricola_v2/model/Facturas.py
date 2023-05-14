from .ControlFertilizantes import ControlFertilizantes
from .ControlPlagas import ControlPlagas
from .Antibiotico import Antibioticos

class Facturas:
    def __init__(self):
        self.__productos_comprados = []
        self.__datos_cliente = None
        self.__fecha = None
        self.__total = 0.00

    def recibir_datos_cliente(self, cliente):
        self.__datos_cliente = cliente

    def obtener_fecha(self):
        return self.__fecha

    def agregar_productos(self, producto, cantidad):
        self.__total += (cantidad * float(producto.obtener_valor()))
        for _ in range(cantidad):
            self.__productos_comprados.append(producto)

    def numero_productos_comprados(self):
        return len(self.__productos_comprados)


    def mostrar_factura(self):
        print(self.__datos_cliente.mostrar_cliente())
        print("Fecha de facturación: ",self.__fecha)
        print("Total de la factura: ",self.__total)
        print("-----------------------------")

    def mostrar_productos_comprados(self):
        print("------------------------------")
        print("Los productos comprados en esta factura:")
        print("------------------------------")
        for producto_comprado in self.__productos_comprados:
            producto_comprado.mostrar_producto()
            print("------------------------------")

