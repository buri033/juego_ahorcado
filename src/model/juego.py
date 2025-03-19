from src.model.diccionario import Diccionario
from src.model.adivinanza import Adivinanza
from src.model.error_intentos_insuficientes import ErrorIntentosInsuficientes


class Juego:
    """
        Clase que encapsula la lógica principal del juego del ahorcado.

        Atributos de clase:
            DIFICULTAD_BAJA (str): Constante que representa la dificultad baja.
            DIFICULTAD_MEDIA (str): Constante que representa la dificultad media.
            DIFICULTAD_ALTA (str): Constante que representa la dificultad alta.
    """
    DIFICULTAD_BAJA = "DIFICULTAD_BAJA"
    DIFICULTAD_MEDIA = "DIFICULTAD_MEDIA"
    DIFICULTAD_ALTA = "DIFICULTAD_ALTA"

    def __init__(self):
        """
            Inicializa el juego con dificultad baja por defecto y sin una palabra generada.
        """
        self.__dificultad = Juego.DIFICULTAD_BAJA
        self.__intentos_realizados: int = 0
        self.__diccionario = Diccionario()
        self.__adivinanza: Adivinanza = None

    def obtener_intentos_realizados(self):
        """
                Retorna la cantidad de intentos actuales disponibles.
        """
        return self.__intentos_realizados

    def obtener_adivinanza(self) -> Adivinanza:
        """
                Retorna la instancia de Adivinanza que contiene la palabra oculta y su estado.
        """
        return self.__adivinanza

    def __generar_palabra(self) -> str:
        """
                Genera una palabra aleatoria utilizando el Diccionario.
        """
        return self.__diccionario.obtener_palabra()

    def calcular_intentos_permitidos(self) -> int:
        """
                Calcula y retorna el número de intentos permitidos según la dificultad:
                    - 20 para DIFICULTAD_BAJA
                    - 10 para DIFICULTAD_MEDIA
                    - 5 para DIFICULTAD_ALTA
        """
        if self.__dificultad == self.DIFICULTAD_BAJA:
            return 20
        if self.__dificultad == self.DIFICULTAD_MEDIA:
            return 10
        if self.__dificultad == self.DIFICULTAD_ALTA:
            return 5

        return 0

    def modificar_dificultad(self, dificultad: str) -> None:
        """
             Modifica la dificultad actual del juego.
               Args:
                   dificultad (str): Nueva dificultad a establecer.
        """
        self.__dificultad = dificultad

    def iniciar_partida(self) -> int:
        """
                Inicia una nueva partida:
                    - Genera la palabra oculta.
                    - Crea la instancia de Adivinanza.
                    - Asigna los intentos permitidos según la dificultad.
                Returns:
                    int: Cantidad de letras (posiciones) de la palabra.
        """
        palabra = self.__generar_palabra()
        self.__adivinanza: Adivinanza = Adivinanza(palabra)
        self.__intentos_realizados = self.calcular_intentos_permitidos()
        return self.__adivinanza.obtener_cantidad_posiciones()

    def adivinar(self, letra: str) -> [int]:
        """
            Intenta adivinar una letra de la palabra.

            Args:
                letra (str): Letra que el jugador quiere adivinar.

            Returns:
                list[int]: Lista con las posiciones donde aparece la letra en la palabra. Vacía si la letra no está.

            Raises:
                ErrorIntentosInsuficientes: Si no quedan intentos disponibles.
        """
        if self.__intentos_realizados < 0:
            raise ErrorIntentosInsuficientes()
        self.__intentos_realizados -= 1
        return self.__adivinanza.adivinar(letra)

    def verificar_si_hay_intentos(self) -> bool:
        """
                Verifica si aún quedan intentos disponibles.
                Returns:
                    bool: True si quedan intentos, False en caso contrario.
        """
        return self.__intentos_realizados >= 0

    def verificar_triunfo(self) -> bool:
        """
               Verifica si el jugador ha adivinado todas las letras.
               Returns:
                   bool: True si se ha ganado, False de lo contrario.
        """
        return self.__adivinanza.verificar_si_hay_triunfo()