import unittest
from Clientes import Clientes
from Facturas import Facturas
from ProductoControl import ProductoControl
from ControlFertilizantes import ControlFertilizantes
from ControlPlagas import ControlPlagas
from Antibiotico import Antibioticos

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.producto1 = ControlFertilizantes()
        self.producto2 = ControlPlagas()
        self.producto3 = Antibioticos()

        self.cliente1 = Clientes()

        self.factura1 = Facturas()
        self.factura2 = Facturas()

    def clientes_guardados_tienda(self):
        cliente_prueba1 = Clientes()
        cliente_prueba2 = Clientes()
        self.assertEqual(2, Clientes.numero_clientes_registrados())

    def test_factura_asociadas_cliente(self):
        self.cliente1.agregar_factura(self.factura1)
        self.cliente1.agregar_factura(self.factura2)
        self.assertEqual(2, self.cliente1.facturas_asociadas())

    def test_agregar_producto_a_factura(self):
        self.factura1.agregar_productos(self.producto1)
        self.factura1.agregar_productos(self.producto2)
        self.factura1.agregar_productos(self.producto3)
        self.assertEqual(3, self.factura1.numero_productos_comprados())

    def test_herencia_producto_control(self):
        #ADVERTENCIA: ¡Para que la prueba sea correcta solo se debe poner 0 en el valor del producto!
        producto_control = ProductoControl()
        self.assertEqual(float(producto_control.obtener_valor()), 0)

        control_plagas = ControlPlagas()
        self.assertIsInstance(control_plagas, ProductoControl)
        self.assertEqual(float(control_plagas.obtener_valor()), 0)

        control_fertilizantes = ControlFertilizantes()
        self.assertIsInstance(control_fertilizantes, ProductoControl)
        self.assertEqual(float(control_fertilizantes.obtener_valor()), 0)


if __name__ == '__main__':
    unittest.main()
