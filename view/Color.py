# Color.py

#
# Définition des couleurs - La classe hérite de la classe Color de PyGame
#
import pygame


class Color(pygame.Color):
    """
    Création d'une couleur en fonction de ses composantes rouges, vert et bleu.

    :param r: Composante en rouge
    :param g: Composante en vert
    :param b: Composante en bleu
    :param a: Transparence de la couleur
    """
    def __init__(self, r: int, g: int, b: int, a: int = 255):
        """
        Création d'une couleur en fonction de ses composantes rouges, vert et bleu.

        :param r: Composante en rouge
        :param g: Composante en vert
        :param b: Composante en bleu
        :param a: Transparence de la couleur
        """
        # Appel du constructeur de la classe mère
        pygame.Color.__init__(self, r, g, b, a)

    def getRed(self) -> int:
        """
        Retourne la composante rouge de la couleur

        :return: Composante rouge
        """
        return self.r

    def getGreen(self) -> int:
        """
        Retourne la composante verte de la couleur

        :return: Composante verte
        """
        return self.g

    def getBlue(self) -> int:
        """
        Retourne la composante bleue de la couleur

        :return: Composante bleue
        """
        return self.b

    def getAlpha(self) -> int:
        """
        Retourne la composante transparence de la couleur

        :return: Transparence
        """
        return self.a

    def setRed(self, r: int):
        """
        Modifie la composante rouge de la couleur

        :param r: Nouvelle valeur pour la composante rouge
        """
        self.r = r

    def setGreen(self, g: int):
        """
        Modifie la composante verte de la couleur

        :param g: Nouvelle valeur pour la composante verte
        """
        self.g = g

    def setBlue(self, b: int):
        """
        Modifie la composante bleue de la couleur

        :param b: Nouvelle valeur pour la composante bleue
        """
        self.b = b

    def setAlpha(self, a: int):
        """
        Modifie la composante transparence de la couleur

        :param a: Nouvelle valeur pour la composante transparence
        """
        self.a = a


# Déclaration de quelques couleurs communes
black = Color(0, 0, 0)
white = Color(255, 255, 255)
red = Color(255, 0, 0)
lime = Color(0, 255, 0)
blue = Color(0, 0, 255)
cyan = Color(0, 255, 255)
yellow = Color(255, 255, 0)
orange = Color(255, 128, 0)
magenta = Color(255, 0, 255)
pink = Color(253, 108, 158)
silver = Color(192, 192, 192)
gray = Color(128, 128, 128)
maroon = Color(128, 0, 0)
green = Color(0, 128, 0)
olive = Color(128, 128, 0)
navy = Color(0, 128, 128)
teal = Color(0, 0, 128)
purple = Color(128, 0, 128)
