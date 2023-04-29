from ui import crear_cliente
from Facturas import Facturas

class Clientes:
    __clientes_creados = []

    def __init__(self):
        nombre_cliente, numero_cedula = crear_cliente()

        self.__nombre_cliente = nombre_cliente
        self.__numero_cedula = numero_cedula
        self.__facturas = []
        self.__class__.__clientes_creados.append(self)
        print("-----------------------------")

    def facturas_asociadas(self):
        return len(self.__facturas)

    def mostrar_cliente(self):
        print("Nombre del cliente: ", self.__nombre_cliente)
        print("Número de cedula: ", self.__numero_cedula)

    def agregar_factura(self, factura):
        factura.recibir_datos_cliente(self)
        self.__facturas.append(factura)

    @staticmethod
    def mostrar_clientes():
        print("Clientes registrados:")
        print("------------------------------")
        for cliente_registrado in Clientes.__clientes_creados:
            cliente_registrado.mostrar_cliente()
            print("------------------------------")

    def mostrar_facturas(self):
        print("------------------------------")
        print("Las facturas asociadas al cliente:")
        print("------------------------------")
        for factura_registrada in self.__facturas:
            factura_registrada.mostrar_factura()
            print("------------------------------")


    def numero_clientes_registrados():
        return len(Clientes.__clientes_creados)