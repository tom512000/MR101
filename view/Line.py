# view/Line.py

from view.Shape import Shape
from view.Color import Color, black
import pygame


#
# Classe dessinant une ligne droite
#


class Line(Shape):
    """
     Définit un segment délimité par deux points start (tuple (x1,y1))
     et end (tuple (x2,y2))

     :param start: point (x,y) de départ du segment
     :param end: point (x,y) de fin du segment
     :param color: Couleur du trait (par défaut black)
     :param width: Largeur du trait (par défaut 1)
     """

    def __init__(self, start: tuple, end: tuple, color: Color = black, width: int = 1):
        """
        Définit un segment délimité par deux points start (tuple (x1,y1))
        et end (tuple (x2,y2))

        :param start: point (x,y) de départ du segment
        :param end: point (x,y) de fin du segment
        :param color: Couleur du trait (par défaut black)
        :param width: Largeur du trait (par défaut 1)
        """
        Shape.__init__(self)
        self.start = start
        self.end = end
        if color != black:
            self.setOutline(color)
        if width != 1:
            self.setWidth(width)

    def _draw(self):
        """
        Usage interne uniquement
        """
        Shape._draw(self)
        pygame.draw.line(self.canvas.screen, self.outLineColor, self.start, self.end, self.width)

    def moveTo(self, pos: tuple) -> None:
        """
        Méthode permettant de déplacer la ligne telle que son point de départ soit égal à `pos`

        :param pos: Nouveau point de départ (x, y)
        :return: Rien
        """
        self.end = self.end[0] + pos[0] - self.start[0], self.end[1] + pos[1] - self.start[1]
        self.start = pos
