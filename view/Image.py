# view/Image.py

#
# Classe Image
# gérant l'affichage d'images

from pygame import image
import pygame
from view.Shape import Shape
import os


class Image(Shape):
    """
    Initialisation de l'image à partir du fichier image.

    :param filename: Nom+chemin du fichier image
    :param pos: Position (x,y) où sera dessinée l'image
    :param size: Taille (w,h) de l'image désiré (si la taille n'est pas définie - None, c'est la taille de l'image source qui est utilisée). None par défaut
    :raise AssertionError: si le fichier n'existe pas
    """

    def __init__(self, filename: str, pos: tuple, size: tuple = None):
        """
        Initialisation de l'image à partir du fichier image.

        :param filename: Nom+chemin du fichier image
        :param pos: Position (x,y) où sera dessinée l'image
        :param size: Taille (w,h) de l'image désiré (si la taille n'est pas définie - None, c'est la taille de l'image source qui est utilisée). None par défaut
        :raise AssertionError: si le fichier n'existe pas
        """
        assert os.path.exists(filename), f"Le fichier {filename} n'existe pas."
        Shape.__init__(self)
        self._surface = image.load(filename)
        if size is not None:
            self._surface = pygame.transform.scale(self._surface, size)
        self.surface = None
        self.pos = pos
        self.noStroke()

    def _draw(self):
        """
        Usage interne uniquement
        """
        Shape._draw(self)
        if self.surface is None:
            self.surface = self._surface.convert_alpha()
        self.canvas.screen.blit(self.surface, self.pos)
        if self.outLineColor is not None:
            x, y = self.pos
            w, h = self.surface.get_size()
            pygame.draw.rect(self.canvas.screen, self.outLineColor, (x, y, w, h), width=self.width)

    def getX(self) -> float:
        """
        Retourne l'abscisse du point supérieur gauche de l'image

        :return: Abscisse du point supérieur gauche de l'image
        """
        return self.pos[0]

    def getY(self) -> float:
        """
        Retourne l'ordonnée du point supérieur gauche de l'image

        :return: Ordonnée du point supérieur gauche de l'image
        """
        return self.pos[1]

    def getWidth(self) -> float:
        """
        Retourne la largeur de l'image

        :return: Largeur de l'image
        """
        return self.surface.get_width() if self.size is None else self.size[0]

    def getHeight(self) -> float:
        """
        Retourne la hauteur de l'image

        :return: Hauteur de l'image
        """
        return self.surface.get_height() if self.size is None else self.size[1]

    def moveTo(self, pos: tuple) -> None:
        """
        Déplace le rectangle en positionnant le point supérieur gauche

        :param pos: Position (x,y) du point supérieur gauche
        :return: Rien
        """
        if self.pos != pos:
            self.pos = pos
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






