# Text.py

#
# Classe permettant de dessiner du texte
#
import pygame
from view.Shape import Shape
from view.Color import Color


class Text(Shape):
    """
    Définit un texte

    :param start: Position (x, y) où dessiner le texte
    :param text: Texte à dessiner
    :param size: Taille du texte (par défaut: 32)
    :param font: Fonte utilisée pour dessiner le texte (par défaut: 'Calibri')
    :param bold: Détermine si la fonte est en gras ou non (par défaut: non)
    :param italic: Détermine si la fonte est en italique ou non (par défaut: non)
    """
    def __init__(self, start: tuple, text: str, size: int = 32, font: str = 'Calibri', bold: bool = False,
                 italic: bool = False):
        """
        Définit un texte

        :param start: Position (x, y) où dessiner le texte
        :param text: Texte à dessiner
        :param size: Taille du texte
        :param font: Fonte utilisée pour dessiner le texte
        :param bold: Détermine si la fonte est en gras ou non
        :param italic: Détermine si la fonte est en italique ou non
        """
        Shape.__init__(self)
        self.start = start
        self.text = text
        pygame.font.init()
        # Initialisation de la fonte
        self.font = pygame.font.SysFont(font, size, bold=bold, italic=italic)
        # Stockage du rendu du texte pour optimiser l'affichage
        self.surface = None
        self.color = self.outLineColor if self.outLineColor is not None else self.fillColor
        # La surface du texte ne peut être définie qu'au moment de la dessiner...

    def _draw(self):
        Shape._draw(self)
        if self.color is not None:
            if self.surface is None:
                self.surface = self.font.render(self.text, True, self.color)
            self.canvas.screen.blit(self.surface, self.start)

    # Redéfinition des méthodes qui nécessitent de redessiner le texte
    def setOutline(self, col: Color) -> None:
        if col is not None and self.color != col:
            self.color = col
            self.surface = None
        # Il faut appeler la méthode de la classe mère en dernier
        # car elle met à jour l'affichage !
        Shape.setOutline(self, col)

    def setFill(self, col: Color) -> None:
        # La couleur fixée par setOutLine prédomine
        # d'où le tests self.color is None
        if self.color is None or self.color != col:
            self.color = col
            self.surface = None
        # Il faut appeler la méthode de la classe mère en dernier
        # car elle met à jour l'affichage !
        Shape.setFill(self, col)

    def noStroke(self) -> None:
        # On se rabat sur la couleur de remplissage
        if self.color != self.fillColor:
            self.color = self.fillColor
            self.surface = None
        # Il faut appeler la méthode de la classe mère en dernier
        # car elle met à jour l'affichage !
        Shape.noStroke(self)

    def noFill(self) -> None:
        # On vérifie si la couleur était celle du remplissage
        if self.outLineColor is None and self.color is not None:
            self.color = None
            self.surface = None
        # Il faut appeler la méthode de la classe mère en dernier
        # car elle met à jour l'affichage !
        Shape.noFill(self)

    def moveTo(self, pos: tuple) -> None:
        """
        Déplace le texte au point (x,y) donné en paramètre

        :param pos: Nouvelle position (x,y) du texte
        :return: Rien
        """
        if pos != self.start:
            self.start = pos
            Shape.moveTo(self, pos)

    def getSize(self) -> tuple:
        """
        Retourne la taille (en pixels) du rectangle encadrant le texte sous la forme
        d'un tuple (width, height)

        :return: Taille du texte
        """
        return self.font.size(self.text)


