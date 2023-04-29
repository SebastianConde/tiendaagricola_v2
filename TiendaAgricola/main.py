from ui import menu
from Clientes import Clientes
from Facturas import Facturas
from ControlFertilizantes import ControlFertilizantes
from ControlPlagas import ControlPlagas
from Antibiotico import Antibioticos

#-----------------------------------------------------------------

menu()
producto1 = ControlFertilizantes()
producto2 = ControlPlagas()
producto3 = Antibioticos()

#-----------------------------------------------------------------

cliente1 = Clientes()
factura1 = Facturas()
factura1.agregar_productos(producto1)
factura1.agregar_productos(producto2)
cliente1.agregar_factura(factura1)
factura1.mostrar_factura()

factura2 = Facturas()
factura2.agregar_productos(producto3)
cliente1.agregar_factura(factura2)

cliente1.mostrar_facturas()

