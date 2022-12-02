# Rectangle.py

#
# Classe définissant un rectangle
#
from view.Shape import Shape
import pygame


class Rectangle(Shape):
    """
    Définit un rectangle de taille size=(width, height) et dont
    le point en haut à gauche se trouve aux coordonnées start=(x,y)

    :param start: Position (abscisse, ordonnée) du point en haut à gauche
    :param size: dimensions (largeur, hauteur) du rectangle
    """
    def __init__(self, start: tuple, size: tuple):
        """
        Définit un rectangle de taille size=(width, height) et dont
        le point en haut à gauche se trouve aux coordonnées start=(x,y)

        :param start: Position (abscisse, ordonnée) du point en haut à gauche
        :param size: dimensions (largeur, hauteur) du rectangle
        """
        Shape.__init__(self)
        self.start = start
        self.size = size

    def getStart(self) -> tuple:
        """
        Retourne le coin supérieur gauche du rectangle sous la forme
        d'un Tuple (x,y)

        :return: Coordonnées du point supérieur gauche du rectangle
        """
        return self.start

    def getX(self) -> float:
        """
        Retourne l'abscisse du point supérieur gauche du rectangle

        :return: Abscisse du point supérieur gauche du rectangle
        """
        return self.start[0]

    def getY(self) -> float:
        """
        Retourne l'ordonnée du point supérieur gauche du rectangle

        :return: Ordonnée du point supérieur gauche du rectangle
        """
        return self.start[1]

    def getWidth(self) -> float:
        """
        Retourne la largeur du rectangle

        :return: Largeur du rectangle
        """
        return self.size[0]

    def getHeight(self) -> float:
        """
        Retourne la hauteur du rectangle

        :return: Hauteur du rectangle
        """
        return self.size[1]

    def moveTo(self, pos: tuple) -> None:
        """
        Déplace le rectangle en positionnant le point supérieur gauche

        :param pos: Position (x,y) du point supérieur gauche
        :return: Rien
        """
        if self.start != pos:
            self.start = pos
            # Mise à jour de l'affichage
            Shape.moveTo(self, pos)

    def setX(self, x: float) -> None:
        """
        Déplace l'abscisse du point supérieur gauche du rectangle

        :param x: Nouvelle abscisse
        :return: Rien
        """
        self.moveTo((x, self.getY()))

    def setY(self, y: float) -> None:
        """
        Déplace l'ordonnée du point supérieur gauche du rectangle

        :param y: Nouvelle ordonnée
        :return: Rien
        """
        self.moveTo((self.getX(), y))

    def _draw(self):
        """
        Dessine la figure - Usage interne uniquement

        :return: Rien
        """
        Shape._draw(self)
        # Remplissage du rectangle si nécessaire
        (x, y) = self.start
        (w, h) = self.size
        if self.fillColor is not None:
            self.canvas.screen.fill(self.fillColor, (x, y, w, h))
        # Dessin du contour si nécessaire
        if self.outLineColor is not None:
            pygame.draw.rect(self.canvas.screen, self.outLineColor, (x, y, w, h), width=self.width)

