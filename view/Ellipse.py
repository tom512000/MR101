# Ellipse.py

#
# Classe définissant une ellipse
#
import pygame
from view.Shape import Shape
from view.Canvas import CanvasError


class Ellipse(Shape):
    """
    Définit une ellipse en fonction de son centre et de ses rayons

    :param center: Centre (x, y) de l'ellipse
    :param radii: rayons (r_x, r_y) de l'ellipse
    """
    def __init__(self, center: tuple, radii: tuple):
        """
        Définit une ellipse en fonction de son centre et de ses rayons

        :param center: Centre (x, y) de l'ellipse
        :param radii: rayons (r_x, r_y) de l'ellipse
        """
        # L'ellipse est dessinée en fonction du rectangle englobant
        # Calcul du rectangle englobant
        Shape.__init__(self)
        self.rect = [center[0] - radii[0], center[1] - radii[1], 2*radii[0], 2*radii[1]]

    def moveTo(self, pos: tuple) -> None:
        """
        Déplace l'ellipse en définissant le nouveau centre

        :param pos: Nouveau centre de l'ellipse
        :return: Rien
        """
        # Calcul du point supérieur gauche correspondant
        (x, y) = (pos[0] - self.rect[2]//2, pos[1] - self.rect[3]//2)
        if x != self.rect[0] or y != self.rect[1]:
            self.rect[0] = x
            self.rect[1] = y
            Shape.moveTo(self, pos)

    def _draw(self):
        """
        Usage interne uniquement

        :return: Rien
        """
        Shape._draw(self)
        # On commence par remplir la figure
        if self.fillColor is not None:
            pygame.draw.ellipse(self.canvas.screen, self.fillColor, self.rect)
        # On trace ensuite le contour
        if self.outLineColor is not None:
            pygame.draw.ellipse(self.canvas.screen, self.outLineColor, self.rect, width=self.width)
        # Mise à jour de la fenêtre
        pygame.display.flip()
