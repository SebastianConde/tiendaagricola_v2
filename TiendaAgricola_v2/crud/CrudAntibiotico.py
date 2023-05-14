from model.Antibiotico import Antibioticos

class CrudAntibiotico():
    __lista_antibioticos = []

    @classmethod
    def crear_antibiotico(cls, nombre_producto, dosis, tipo_animal, valor_producto):
        nuevo_antibiotico = Antibioticos(nombre_producto, dosis, tipo_animal, valor_producto)
        cls.__lista_antibioticos.append(nuevo_antibiotico)
        return nuevo_antibiotico

    @classmethod
    def buscar_antibiotico(cls, nombre_producto):
        for antibiotico in cls.__lista_antibioticos:
            if(antibiotico.obtener_nombre() == nombre_producto):
                return antibiotico

    @classmethod
    #Solo se actualiza nombre porque la cedula no es actualizable
    def actualizar_antibiotico(cls, nombre_producto, dosis, tipo_animal, valor_producto):
        antibiotico = cls.buscar_antibiotico(nombre_producto)
        antibiotico.actualizar_antibiotico(nombre_producto, dosis, tipo_animal, valor_producto)

        # Actualizar la lista:
        for i, antibiotico_lista in enumerate(cls.__lista_antibioticos):
            if antibiotico_lista == antibiotico:
                cls.__lista_antibioticos[i].actualizar_antibiotico(nombre_producto, dosis, tipo_animal, valor_producto)


    @classmethod
    def eliminar_antibiotico(cls, nombre_producto):
        antibiotico = cls.buscar_antibiotico(nombre_producto)
        antibiotico.eliminar()

        #Eliminar de la lista
        cls.__lista_antibioticos.remove(antibiotico)