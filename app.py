from src.model.juego import Juego

from src.view.menu import Menu

if __name__ == "__main__":
    """
       Punto de entrada de la aplicación.
       Instancia el juego y el menú, e inicia la ejecución.
       """
    juego: Juego = Juego()
    menu: Menu = Menu(juego)
    menu.iniciar()
