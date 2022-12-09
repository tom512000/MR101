# main_tp4.py
from TP4.tp4 import getRegularArray2D


def test_getRegularArray2D() -> None:
    lst = getRegularArray2D(4, 5, -10, 10)
    print("Tableau de 4 lignes et 5 colonnes :", lst, sep="\n")
    return None


test_getRegularArray2D()
