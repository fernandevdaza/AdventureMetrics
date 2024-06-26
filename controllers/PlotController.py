class PlotController:

    def __init__(self, plot_model) -> None:
        self.plot_model = plot_model()
    
    def _is_valid_limit(self, limit):
        """
        Valida si el límite proporcionado es un número entero válido y menor o igual a 10.
        :param limit: Límite a validar.
        :return: True si el límite es un número entero válido, False en caso contrario.
        """
        try:
            if limit is not None:
                limit = int(limit)
                if limit <= 0 or limit > 10:
                    return False
            return True
        except Exception as e:
            print(f"Error al validar el límite: {e}")
            return False
        
