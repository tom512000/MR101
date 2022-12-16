# main_tp4.py
from TP4.tp4 import *
import random


def test_getRegularArray2D() -> None:
    lst = getRegularArray2D(4, 5, -10, 10)
    print("Tableau de 4 lignes et 5 colonnes :", lst, sep="\n")
    return None


print("\nFonction getRegularArray2D :")
test_getRegularArray2D()


def test_getMinMax() -> None:
    for i in range(5):
        lst = getRegularArray2D(random.randint(1, 5), random.randint(1, 5), -10, 10)
        print(f"{lst} : Min = {getMin(lst)}, max = {getMax(lst)}")
    return None


print("\nFonction getMin et getMax :")
test_getMinMax()
