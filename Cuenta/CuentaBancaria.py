from ui import inicio

class CuentaBancaria:
    #lista donde se guardarán todas las cuentas bancarias:
    __cuentas_clientes = []


    def __init__(self):
        print("Nueva Cuenta: \n")
        # Abstrae los valores de las variables del ui:
        numero_cuenta, documento_identidad, nombre_cliente, saldo_actual = inicio()

        self.__numero_cuenta = numero_cuenta
        self.__documento_identidad = documento_identidad
        self.__nombre_cliente = nombre_cliente
        self.__saldo_actual = saldo_actual
        self.__class__.__cuentas_clientes.append(self)

        print("-----------------------------")


    def depositarDinero(self):
        monto = float(input("¿Cuál es el monto que desea depositar a la cuenta?: "))

        monto_retenido = monto*0.19
        monto_depositado = monto - monto_retenido
        self.__saldo_actual += monto_depositado

        print("Se ha depositado a la cuenta: $", monto_depositado, " Valor retenido (19%): $", monto_retenido)
        print("Saldo actual: $", self.__saldo_actual)
        print("------------------------------")

        #actualizar la lista:
        for cuenta in CuentaBancaria.__cuentas_clientes:
            if cuenta.__numero_cuenta == self.__numero_cuenta:
                cuenta.__saldo_actual = self.__saldo_actual


    def mostrarCuenta(self):
        print("Numero de cuenta: ", self.__numero_cuenta)
        print("Numero de documento: ", self.__documento_identidad)
        print("Nombre del cliente: ", self.__nombre_cliente)
        print("Saldo actual: ", self.__saldo_actual)
        print("-----------------------------")


    def retirarDinero(self, saldo_retiro):
        print("Estos son los datos de su cuenta: \n")
        self.mostrarCuenta()
        continuar_retiro = input("¿Desea continuar con el retiro? [S/N]: ")

        if continuar_retiro == "S":
            if self.__saldo_actual >= saldo_retiro:
                self.__saldo_actual -= saldo_retiro
                print("Se ha retirado $", saldo_retiro, "pesos de la cuenta bancaria. Su saldo actual es de: $", self.__saldo_actual)
            else:
                print("Lo sentimos, los fondos no son suficientes para cubrir el monto de retiro")
        else:
            print("Transacción cancelada, gracias por usar este servicio")

        print("------------------------------")

        # actualizar la lista:
        for cuenta in CuentaBancaria.__cuentas_clientes:
            if cuenta.__numero_cuenta == self.__numero_cuenta:
                cuenta.__saldo_actual = self.__saldo_actual



    @staticmethod
    def mostrarCuentas():
        print("Cuentas bancarias:")
        print("------------------------------")
        for cuenta in CuentaBancaria.__cuentas_clientes:
            cuenta.mostrarCuenta()
            print("------------------------------")