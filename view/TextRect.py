# view/TextRect.py
from view.Rectangle import Rectangle
from view.Text import Text
from view.Color import Color, black
from view.Shape import Shape


#
# Classe permettant de dessiner un texte dans un rectangle.
# Il n'y a pas de clipping : si le rectangle est trop petit, le texte débordera.
#
# Pour l'instant, il est uniquement prévu de centrer le texte dans le rectangle.
# Si le rectangle n'est pas défini, utilisation du rectangle de base d'affichage du texte (voir Surface)...
#
# Pour mettre en place cette classe, il faut détourner certaines méthodes et en rajouter :
# - les méthodes noFill(), noStroke(), setFill() et setOutline() vont correspondre au rectangle.
# - Pour modifier la couleur du texte, on rajoutera les méthodes setTextColor()/getTextColor() ainsi que
#   l'attribut text_color
#
# La classe va hériter des classes Rectangle et Text pour utiliser au maximum le code
# déjà écrit...
# L'affichage du texte posera problème si la taille du rectangle est définie par l'utilisateur.
# En revanche, la taille du rectangle posera problème si la taille n'est pas définie par l'utilisateur...
# Pour différencier les deux cas (rectangle défini par l'utilisateur ou non), on utilisera un booléen rect_defined.
#

class TextRect(Rectangle, Text):
    """
    Constructeur de la classe permettant de définir le texte à afficher, la taille du texte, la fonte,
    le style du texte (italique et/ou gras) ainsi que le rectangle encadrant le texte.

    Par défaut, la couleur du texte est noire (voir ``setTextColor()``)

    :param start: Position du rectangle encadrant le texte
    :param text: Texte à afficher
    :param size: Taille du texte (par défaut : 32)
    :param font: Fonte utilisée pour afficher le texte (voir la classe ``Text`` - par défaut : 'Calibri')
    :param bold: Gras si le paramètre vaut True (False par défaut).
    :param italic: Italique si le paramètre vaut True (False par défaut).
    :param rect: Taille (width, height) du rectangle encadrant le texte.
    """

    def __init__(self, start: tuple, text: str, size: int = 32, font: str = 'Calibri', bold: bool = False,
                 italic: bool = False, rect: tuple = None):
        """
        Constructeur de la classe permettant de définir le texte à afficher, la taille du texte, la fonte,
        le style du texte (italique et/ou gras) ainsi que le rectangle encadrant le texte.

        Par défaut, la couleur du texte est noire (voir setTextColor())

        :param start: Position du rectangle encadrant le texte
        :param text: Texte à afficher
        :param size: Taille du texte (par défaut : 32)
        :param font: Fonte utilisée pour afficher le texte (voir la classe Text - par défaut : 'Calibri')
        :param bold: Gras si le paramètre vaut True (False par défaut).
        :param italic: Italique si le paramètre vaut True (False par défaut).
        :param rect: Taille (width, height) du rectangle encadrant le texte.
        """
        Text.__init__(self, start=start, text=text, size=size, font=font, bold=bold, italic=italic)
        # Premier problème : si rect = None !
        self.rect_defined = True
        if rect is None:
            self.rect_defined = False
        Rectangle.__init__(self, start=start, size=rect if self.rect_defined else self.font.size(self.text))
        self.text_color = black

    def moveTo(self, pos: tuple) -> None:
        """
        Déplace le rectangle contenant le texte en positionnant le point supérieur gauche

        :param pos: Position (x,y) du point supérieur gauche
        :return: Rien
        """
        Rectangle.moveTo(self, pos)
        return None

    def noFill(self) -> None:
        """
        Supprime le remplissage du rectangle

        :return: Rien
        """
        Rectangle.noFill(self)
        return None

    def noStroke(self) -> None:
        """
        Supprime le contour de la forme

        :return: Rien
        """
        Rectangle.noStroke(self)
        return None

    def setFill(self, col: Color) -> None:
        """
        Définit la couleur de remplissage

        :param col: Couleur de remplissage
        :return: Rien
        """
        Rectangle.setFill(self, col)
        return None

    def setOutline(self, col: Color) -> None:
        """
        Définit la couleur du contour de la forme

        :param col: Couleur du contour
        :return: Rien
        """
        Rectangle.setOutline(self, col)
        return None

    def setTextColor(self, col: Color) -> None:
        """
        Définit la couleur du texte

        :param col: Couleur du texte
        :return: Rien
        """
        if col != self.text_color:
            self.text_color = col
            Shape._refresh(self)
        return None

    def _draw(self):
        """
        Dessine le rectangle et le texte

        Usage interne uniquement

        :return: Rien
        """
        Shape._draw(self)
        Rectangle._draw(self)
        if self.text_color is not None:
            if self.surface is None:
                self.surface = self.font.render(self.text, True, self.text_color)
            # Détermination de la position du texte
            start = self.start
            if self.rect_defined:
                w, h = self.surface.get_size()
                start = start[0] + (self.size[0] - w)/2, start[1] + (self.size[1] - h)/2
            self.canvas.screen.blit(self.surface, start)
        return None



