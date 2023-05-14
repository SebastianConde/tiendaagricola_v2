from model.ControlPlagas import ControlPlagas

class CrudControlPlagas():
    __lista_plagas = []

    @classmethod
    def crear_plaga(cls, registro_ICA, nombre_producto, frecuencia_aplicacion, valor_producto, periodo_carencia):
        nueva_plaga = ControlPlagas(registro_ICA, nombre_producto, frecuencia_aplicacion, valor_producto, periodo_carencia)
        cls.__lista_plagas.append(nueva_plaga)
        return nueva_plaga

    @classmethod
    def buscar_plaga(cls, registro_ICA):
        for plaga in cls.__lista_plagas:
            if(plaga.obtener_registro_ICA() == registro_ICA):
                return plaga

    @classmethod
    def actualizar_plaga(cls, registro_ICA_antes, registro_ICA_despues, nombre_producto_despues, frecuencia_aplicacion_despues, valor_producto_despues, periodo_carencia_despues):
        plaga = cls.buscar_plaga(registro_ICA_antes)
        plaga.actualizar_plaga(registro_ICA_despues, nombre_producto_despues, frecuencia_aplicacion_despues, valor_producto_despues, periodo_carencia_despues)

        #Actualizar la lista:
        for i, plaga_lista in enumerate(cls.__lista_plagas):
            if plaga_lista == plaga:
                cls.__lista_plagas[i].actualizar_plaga(registro_ICA_despues, nombre_producto_despues, frecuencia_aplicacion_despues, valor_producto_despues, periodo_carencia_despues)

    @classmethod
    def eliminar_plaga(cls, registro_ICA):
        plaga = cls.buscar_plaga(registro_ICA)
        plaga.eliminar()

        # Eliminar de la lista
        cls.__lista_plagas.remove(plaga)