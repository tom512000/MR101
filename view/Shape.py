# Shape.py

#
# Classe Shape : classe mère de toutes les formes possibles
#
from view.Canvas import Canvas, CanvasError
from view.Color import Color


class Shape:
    def __init__(self):
        self.canvas = None
        self.fillColor = Color(178, 0, 255)
        self.outLineColor = Color(0, 0, 0)
        self.width = 1

    def draw(self, cv: Canvas) -> None:
        """
        Dessine la figure sur la fenêtre passée en paramètre.

        :param cv: Fenêtre où dessiner la figure
        :return: Rien
        :raise CanvasError: Si on essaie de dessiner la même figure sur plusieurs fenêtres
        """
        if self.canvas is not None and self.canvas != cv:
            raise CanvasError("Une figure ne peut être dessinée que sur une seule fenêtre à la fois.")
        self.canvas = cv
        cv.draw(self)

    def undraw(self) -> None:
        """
        Efface la figure

        :return: Rien
        """
        if self.canvas is not None:
            self.canvas.undraw(self)

    def setFill(self, col: Color) -> None:
        """
        Définit la couleur de remplissage

        :param col: Couleur de remplissage
        :return: Rien
        """
        self.fillColor = col
        # Mettre à jour l'affichage
        self._refresh()

    def getFill(self) -> Color:
        """
        Retourne la couleur de remplissage de la figure

        :return: Couleur de remplissage
        """
        return self.fillColor

    def noFill(self) -> None:
        """
        Supprime le remplissage de la forme

        :return: Rien
        """
        self.fillColor = None
        self._refresh()

    def setOutline(self, col: Color) -> None:
        """
        Définit la couleur du contour de la forme

        :param col: Couleur du contour de la forme
        """
        self.outLineColor = col
        self._refresh()

    def setWidth(self, pixels: int) -> None:
        """
        Définit l'épaisseur du contour de la forme

        :param pixels: épaisseur du contour en pixel
        """
        self.width = pixels
        self._refresh()

    def noStroke(self) -> None:
        """
        Supprime le contour de la forme

        :return: Rien
        """
        self.outLineColor = None
        self._refresh()

    def moveTo(self, pos: tuple) -> None:
        """
        Déplace la figure à la position donnée en paramètre

        :param pos: Position où la figure doit être déplacée. Sa signification dépend de la figure
        :return: Rien
        """
        # A redéfinir dans les classes héritées
        self._refresh()

    def _draw(self):
        """
        Usage interne uniquement

        :return: Rien
        """
        if self.canvas is None:
            raise CanvasError("La figure ne peut être dessinée car la fenêtre n'est pas définie")

    def _refresh(self):
        """
        Usage interne uniquement

        :return: Rien
        """
        if self.canvas is not None:
            self.canvas._refresh()

