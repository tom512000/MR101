# Circle.py

#
# Classe décrivant un cercle
#
from view.Ellipse import Ellipse


class Circle(Ellipse):
    """
    Crée un cercle/disque de centre et de rayon définis par les paramètres.


    :param tuple center: Tuple (x,y) définissant le centre du cercle
    :param int radius: Rayon du cercle
    """
    def __init__(self, center: tuple, radius: int):
        Ellipse.__init__(self, center, (radius, radius))

