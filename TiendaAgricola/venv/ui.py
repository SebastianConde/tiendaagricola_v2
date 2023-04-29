def menu():
    print("!BIENVENIDO!")
              

def crear_cliente():
    print("Cree el nuevo cliente: ")
    nombre_cliente = str(input("Nombre del cliente: "))
    numero_cedula = str(input("Número de cedula del cliente: "))
    
    return nombre_cliente, numero_cedula

def crear_producto_control():
    print("Cree el nuevo producto de control (Fertilizante o de Control de plagas): ")
    registro_ICA = str(input("Número de registro ICA: "))
    nombre_producto = str(input("Nombre del producto: "))
    frecuencia_aplicacion = str(input("Frecuencia de aplicación: "))
    valor_producto = validar_float("Valor del producto: $")
    
    return registro_ICA, nombre_producto, frecuencia_aplicacion, valor_producto


def crear_antibiotico():
    print("Cree el nuevo antibiotico: ")
    nombre_producto = str(input("Nombre del producto: "))
    dosis = str(input("Ingrese la dosis especificada: "))
    tipo_animal = str(input("Ingrese el tipo de animal (Bovino, Caprino o Porcino): "))
    valor_producto = validar_float("Valor del producto: $")
    
    return nombre_producto, dosis, tipo_animal, valor_producto


def validar_float(mensaje):
    valor = input(mensaje)
    while not es_numero(valor):
        print("Error: el valor ingresado no es un número válido.")
        valor = input(mensaje)
    return valor

def es_numero(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False