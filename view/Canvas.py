# Canvas.py
# Utilisé pour éviter l'import cyclique de Shape qui importe lui-même Canvas
# Ce package évite de déclarer les types sous forme de chaines de caractères
from __future__ import annotations

#
# Définition d'une classe correspondant à peu près
# à la classe Canvas introduite en TP sur Jupyter...
#
import pygame

# Utilisé pour éviter l'import cyclique de Shape qui importe lui-même Canvas
from typing import TYPE_CHECKING

# Utilisé pour éviter l'import cyclique de Shape qui importe lui-même Canvas
if TYPE_CHECKING:
    from view.Shape import Shape

from view.Color import Color


class CanvasError(Exception):
    def __init__(self, msg: str):
        """
        Initialisation d'une erreur de type CanvasError avec le message msg

        :param msg: Message de l'erreur
        """
        self.message = msg

    def __str__(self) -> str:
        """
        Méthode appelée pour l'affichage de l'objet

        :return: Chaîne de caractères représentant l'objet (ici, le message de l'erreur)
        """
        return self.message


class Canvas:
    """
    Créer une fenêtre

    :param tuple size: Taille de la fenêtre sous la forme (largeur, hauteur) en pixels.
    """
    def __init__(self, size: tuple):
        """
        Initialisation de la fenêtre Canvas

        :param size: Tuple (width, height) déterminant la dimension de la fenêtre
        """
        self.size = size
        self.screen = pygame.display.set_mode(self.size)
        self.backgroundColor = Color(255, 255, 255)
        self.screen.fill(self.backgroundColor)
        self.shapes = []
        self.update = False

    def getWidth(self) -> int:
        """
        Retourne la largeur de la fenêtre

        :return: Largeur de la fenêtre
        """
        return self.size[0]

    def getHeight(self) -> int:
        """
        Retourne la hauteur de la fenêtre

        :return: Hauteur de la fenêtre
        """
        return self.size[1]

    def draw(self, figure: Shape) -> None:
        """
        Dessine la figure sur la fenêtre

        :param figure: figure à dessiner
        """
        if figure.canvas is None:
            figure.canvas = self
        self.shapes.append(figure)
        if not self.update:
            # Dessin de la figure
            figure._draw()
            # Mise à jour de la fenêtre
            pygame.display.flip()

    def undraw(self, figure: Shape) -> None:
        """
        Permet d'effacer une figure du contenu de la fenêtre

        :param figure: Figure à retirer de l'affichage
        """
        if figure in self.shapes:
            self.shapes.remove(figure)
            # Remettre à jour l'affichage complet
            self._refresh()

    def clear(self) -> None:
        """
        Efface tout le contenu de la fenêtre
        """
        if len(self.shapes) > 0:
            self.shapes.clear()
            # Remettre à jour l'affichage
            self._refresh()

    def drawFrame(self, col: Color) -> None:
        """
        Définit la couleur de fond de la fenêtre.

        L'affichage du cadre est inutile ici (contrairement aux TP sur Jupyter)
        puisque le cadre d'affichage est contenu dans une fenêtre

        :param col: Couleur de fond
        """
        if self.backgroundColor != col:
            self.backgroundColor = col
            # Il est nécessaire de tout redessiner
            self._refresh()

    def display(self) -> None:
        """
        Devrait déclencher l'affichage du canvas
        """
        # Ici, il n'y a rien à faire car la fenêtre est affichée dès sa création...
        pass

    def _refresh(self) -> None:
        """
        Usage interne uniquement
        :return: Rien
        """
        if not self.update:
            self.screen.fill(self.backgroundColor)
            # Dessin des figures mémorisées
            for figure in self.shapes:
                figure._draw()
            # Mise à jour de la fenêtre
            # pygame.display.flip()
            pygame.display.update()
            # Vider la liste des événements pour que cela ne plante pas sous Windows...
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

    def begin_update(self):
        """
        Permet de désactiver le rafraichissement graphique pour optimiser l'affichage.

        Cette fonction est à utiliser en couple avec la fonction `end_update()` lorsque vous avez une série de
        modifications graphiques à réaliser sans nécessité de mise à jour graphique à chaque modification.

        Une fois les modifications graphiques faites, appelez la méthode `end_update()` pour mettre à jour l'affichage.

        :return: Rien
        """
        self.update = True

    def end_update(self):
        """
        Permet de réactiver le rafraichissement graphique.

        A utiliser en couple avec la méthode `begin_update()`.

        :return: Rien
        """
        self.update = False
        self._refresh()


def waitClick() -> tuple:
    """
    Attend un click dans la fenêtre puis retourne la position de la souris lors du click
    et le bouton cliqué (1 - bouton gauche, 2 - bouton milieu, 3 - bouton droit)

    Si l'utilisateur ferme la fenêtre, cette fonction provoque l'arrêt du
    script python...

    .. WARNING::
        Avant d'appeler cette fonction, vous devez créer une fenêtre (Canvas). Sinon, une erreur se produit...

    :return: Un Tuple (x, y, button) contenant la position (x,y) de la souris
             et le bouton cliqué.

    """
    waiting = True

    res = None
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                res = (event.pos[0], event.pos[1], event.button)
                waiting = False
    return res


def pause(ms: int) -> None:
    """
    Effectue une pause (temps exprimé en millisecondes)

    :param ms: temps de la pause
    :return: Rien
    """
    pygame.time.wait(ms)
    return None

