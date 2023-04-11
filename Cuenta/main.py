from CuentaBancaria import CuentaBancaria
import ui

ui.bienvenida()

cuenta1 = CuentaBancaria()
cuenta1.retirarDinero(50000)
cuenta1.depositarDinero()

cuenta2 = CuentaBancaria()
cuenta2.depositarDinero()
cuenta2.depositarDinero()
cuenta2.retirarDinero(60000)

cuenta1.retirarDinero(30000)

#CuentaBancaria.mostrarCuentas()