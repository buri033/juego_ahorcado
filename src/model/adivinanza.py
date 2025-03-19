class Adivinanza:
    """
        Representa una palabra a adivinar en el juego del ahorcado.

        Attributes:
            __letras (list[str]): Lista de caracteres que conforman la palabra a adivinar.
            __posiciones (list[bool]): Lista de booleanos que indican si cada letra ha sido adivinada.
    """

    def __init__(self, palabra: str):
        """
        Inicializa la Adivinanza con la palabra oculta.
        Args:
            palabra (str): La palabra que se debe adivinar.
        """

        self.__letras: list[str] = list(palabra)
        self.__posiciones: list[bool] = [False] * len(self.__letras)

    def adivinar(self, letra: str) -> [int]:
        """
                Intenta adivinar una letra en la palabra.
                Args:
                    letra (str): Letra que se intenta adivinar.
                Returns:
                    list[int]: Lista de índices donde se encuentra la letra; lista vacía si no se encuentra.
        """
        if letra not in self.__letras:
            return []

        posiciones_donde_esta_la_letra = []
        for i in range(len(self.__letras)):
            if self.__letras[i] == letra:
                posiciones_donde_esta_la_letra.append(i)
                self.__posiciones[i] = True
        return posiciones_donde_esta_la_letra

    def obtener_letras(self) -> [str]:
        """
                Retorna la lista completa de letras de la palabra.
        """
        return self.__letras

    def obtener_posiciones(self) -> [bool]:
        """
               Retorna el estado (True/False) de cada posición de la palabra.
        """
        return self.__posiciones

    def obtener_cantidad_posiciones(self) -> int:
        """
                Retorna la cantidad total de letras en la palabra.
        """
        return len(self.__letras)

    def verificar_si_hay_triunfo(self) -> bool:
        """
                Verifica si todas las letras han sido adivinadas.
                Returns:
                    bool: True si se adivinó la palabra completa, False de lo contrario.
        """
        return all(self.__posiciones)
