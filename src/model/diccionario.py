import random


class Diccionario:
    """
       Clase Diccionario.

       Esta clase se encarga de cargar una lista de palabras desde un archivo y de proporcionar una palabra aleatoria para su uso en el juego del ahorcado.

       Métodos:
           __init__(): Inicializa la instancia y carga las palabras disponibles.
           __cargar_palabras(): Lee el archivo de palabras y retorna una lista con ellas.
           obtener_palabra(): Retorna una palabra seleccionada de forma aleatoria de la lista.
    """
    def __init__(self):
        """
            Inicializa una instancia de la clase Diccionario, cargando las palabras desde un archivo.
        """
        self.palabras: list[str] = self.__cargar_palabras()

    def __cargar_palabras(self) -> list[str]:
        """
                Carga las palabras desde 'assets/palabras.txt' y las retorna en una lista.
                Returns:
                    list[str]: Lista de palabras disponibles.
        """
        palabras = []
        with open("assets/palabras.txt", "r", encoding="utf8") as archivo:
            for line in archivo:
                palabras.append(line.strip())

        return palabras

    def obtener_palabra(self) -> str:
        """
                Selecciona y retorna una palabra aleatoria de la lista.
                Returns:
                    str: Palabra seleccionada.
        """
        indice_aleatorio = random.randint(0, len(self.palabras) - 1)
        return self.palabras[indice_aleatorio]
