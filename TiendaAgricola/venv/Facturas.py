from ControlFertilizantes import ControlFertilizantes
from ControlPlagas import ControlPlagas
from Antibiotico import Antibioticos
from datetime import datetime

class Facturas:
    def __init__(self):
        self.__productos_control = []
        self.__antibioticos = []
        self.__datos_cliente = None
        self.__fecha = datetime.now()
        self.__total = 0.00

    def recibir_datos_cliente(self, cliente):
        self.__datos_cliente = cliente

    def clasificar_productos_registrados(self, producto):
        if (type(producto) == ControlFertilizantes or type(producto) == ControlPlagas):
            self.__productos_control.append(producto)
        elif (type(producto) == Antibioticos):
            self.__antibioticos.append(producto)
        
    def agregar_productos(self, producto):
        self.__total += float(producto.obtener_valor())
        self.clasificar_productos_registrados(producto)


    def mostrar_productos_comprados(self):
        for producto in self.__productos_control:
            producto.obtener_nombre_valor()
        for producto in self.__antibioticos:
            producto.obtener_nombre_valor()

    def numero_productos_comprados(self):
        return len(self.__productos_control) + len(self.__antibioticos)


    def mostrar_factura(self):
        print(self.__datos_cliente.mostrar_cliente())
        print("Fecha de facturación: ",self.__fecha)
        Facturas.mostrar_productos_comprados(self)
        print("Total de la factura: ",self.__total)
        print("-----------------------------")