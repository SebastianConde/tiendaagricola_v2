from model.Facturas import Facturas

class CrudFacturas():
    @classmethod
    def crear_Factura(cls):
        nueva_factura = Facturas()
        return nueva_factura

    @classmethod
    def buscar_factura(cls, cliente, fecha):
        lista_facturas_cliente = cliente.lista_facturas_asociadas()

        for factura_cliente in lista_facturas_cliente:
            if(factura_cliente.obtener_fecha() == fecha):
                return factura_cliente

    @classmethod
    def actualizar_factura(cls, factura, producto, cantidad):
        factura.agregar_productos(producto, cantidad)

    @classmethod
    def eliminar_factura(cls, cliente, fecha):
        factura = cls.buscar_factura(cliente, fecha)

        cliente.eliminar_factura(factura)
