from model.ControlFertilizantes import ControlFertilizantes

class CrudControlFertilizantes():
    __lista_fertilizantes = []

    @classmethod
    def crear_fertilizante(cls, registro_ICA, nombre_producto, frecuencia_aplicacion, valor_producto, ultima_aplicacion):
        nuevo_fertilizante = ControlFertilizantes(registro_ICA, nombre_producto, frecuencia_aplicacion, valor_producto, ultima_aplicacion)
        cls.__lista_fertilizantes.append(nuevo_fertilizante)
        return nuevo_fertilizante

    @classmethod
    def buscar_fertilizante(cls, registro_ICA):
        for fertilizante in cls.__lista_fertilizantes:
            if(fertilizante.obtener_registro_ICA() == registro_ICA):
                return fertilizante

    @classmethod
    def actualizar_fertilizante(cls, registro_ICA_antes, registro_ICA_despues, nombre_producto_despues, frecuencia_aplicacion_despues, valor_producto_despues, ultima_aplicacion_despues):
        fertilizante = cls.buscar_fertilizante(registro_ICA_antes)
        fertilizante.actualizar_fertilizante(registro_ICA_despues, nombre_producto_despues, frecuencia_aplicacion_despues, valor_producto_despues, ultima_aplicacion_despues)

        #Actualizar la lista:
        for i, fertilizante_lista in enumerate(cls.__lista_fertilizantes):
            if fertilizante_lista == fertilizante:
                cls.__lista_fertilizantes[i].actualizar_fertilizante(registro_ICA_despues, nombre_producto_despues, frecuencia_aplicacion_despues, valor_producto_despues, ultima_aplicacion_despues)

    @classmethod
    def eliminar_fertilizante(cls, registro_ICA):
        fertilizante = cls.buscar_fertilizante(registro_ICA)
        fertilizante.eliminar()

        # Eliminar de la lista
        cls.__lista_fertilizantes.remove(fertilizante)