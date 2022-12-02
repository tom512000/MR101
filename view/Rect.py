# view/Rect.py

#
# Classe utilisée uniquement pour
# illustrer les tris
#
# Pour l'illustration des tris,
# La méthode setX est détournée et une pause est insérée.
#
# D'autres méthodes/fonctions sont ajoutées pour simplifier/animer le tri
#

from view.Rectangle import Rectangle
from view.Canvas import Canvas
from view.Color import Color, black, lime
import pygame


class Rect(Rectangle):
    """
    Simplification/modification du constructeur.

    On fixe la largeur à 20 pixels.
    La position en X est déterminée selon un entier représentant la position du rectangle
    dans le tableau.

    :param index: Position/index du rectangle dans la liste.
    :param hauteur: Hauteur du rectangle
    :param cv: Fenêtre dans laquelle va être dessiné le rectangle
    """
    r_width = 20
    # Marge en haut et en bas (TopBottomMargin)
    r_tbm = 20

    def __init__(self, index: int, hauteur: int, cv: Canvas):
        """
        Constructeur simplifié du rectangle.

        :param index: Position/index du rectangle dans la liste.
        :param hauteur: Hauteur du rectangle
        :param cv: Fenêtre dans laquelle va être dessiné le rectangle
        """
        Rectangle.__init__(self, ((index + 1) * Rect.r_width, cv.getHeight() - hauteur - Rect.r_tbm),
                           (Rect.r_width, hauteur))

        self.setFill(Color(122, 128, 255))
        self.setOutline(black)
        self.draw(cv)

    def setX(self, indice: int, tps: float = 0.25) -> None:
        """
        Ajout d'une pause dans le déplacement du rectangle

        :param indice: Position/indice du rectangle dans le tableau
        :param tps: Durée de la pause (en secondes - par défaut : 0.25 s)
        :return: Rien
        """
        Rectangle.setX(self, (indice + 1) * Rect.r_width)
        pygame.time.delay(int(tps*1000))

    def unsetX(self, tps: float = 0.25) -> None:
        """
        Méthode à appeler quand on "retire" le rectangle temporairement de la liste,
        par exemple, pour échanger sa position avec un autre rectangle.

        :param tps: Durée de la pause (en secondes - par défaut : 0.25 s)
        :return: Rien
        """
        self.setX(-10, tps)

    def setPlaced(self) -> None:
        """
        Méthode à appeler lorsqu'un rectangle est à sa bonne position (trié)

        :return: Rien
        """
        self.setFill(lime)

    def getHeight(self) -> float:
        """
        Détournement de la méthode pour rajouter une pause...

        :return: Hauteur du rectangle
        """
        pygame.time.wait(10)
        return Rectangle.getHeight(self)


def getCanvasSizeFrom(lst: list) -> tuple:
    """
    Calcule la taille de la fenêtre devant afficher les rectangles dont les hauteurs sont contenues dans la liste
    passée en paramètre.

    :param lst: Liste des hauteurs (de type int) des rectangles
    :return: (largeur, hauteur) de la fenêtre
    """
    # Calcul de la largeur (deux colonnes vides pour les marges)
    width = (len(lst) + 2)*Rect.r_width
    # Calcul de la hauteur (marge 20 en haut et en bas)
    height = 2*Rect.r_tbm + max(lst)
    return width, height
