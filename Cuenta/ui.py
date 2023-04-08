def bienvenida():
    print("¡BIENVENIDO!\n")

def inicio():
    numero_cuenta = int(input("¿Cuál es su número de cuenta?: "))
    documento_identidad = int(input("¿Cuál es su número de documento de identidad?: "))
    nombre_cliente = str(input("¿Cuál es el nombre del cliente?: "))
    saldo_actual = float(input("¿Cuál es el saldo actual de la cuenta?: "))

    return numero_cuenta, documento_identidad, nombre_cliente, saldo_actual


