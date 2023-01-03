# main_tp4.py
from TP4.tp4 import *
import random

print("\nFonction getRegularArray2D :")


def test_getRegularArray2D() -> None:
    lst = getRegularArray2D(4, 5, -10, 10)
    print("Tableau de 4 lignes et 5 colonnes :", lst, sep="\n")
    return None


test_getRegularArray2D()

print("\nFonction getMin et getMax :")


def test_getMinMax() -> None:
    for i in range(5):
        lst = getRegularArray2D(random.randint(1, 5), random.randint(1, 5), -10, 10)
        print(f"{lst} : Min = {getMin(lst)}, max = {getMax(lst)}")
    return None


test_getMinMax()

print("\nFonction test_getRegularArray2D :")


def test_getRegularArray2D() -> None:
    for i in range(10000):
        nl = random.randint(1, 10)
        nc = random.randint(1, 10)
        mn = random.randint(-20, -5)
        mx = random.randint(5, 20)
        tab = getRegularArray2D(nl, nc, mn, mx)
        mn_tab = getMin(tab)
        mx_tab = getMax(tab)
        assert isRegular(tab) == True, "Toutes les lignes du tableau 2D ne contiennent pas le même nombre d’éléments !"
        assert ((nl, nc) == getSize2D(tab)), "Les dimensions du tableau 2D sont incorrectes !"
        assert mn_tab >= mn, "La valeur minimale du tableau 2D est incorrecte !"
        assert mn <= mx_tab, "Le valeur minimale du tableau 2D est supérieur à la valeur maximale !"
        assert mx_tab <= mx, "La valeur maximale du tableau 2D est incorrecte !"
    print("La fonction getRegularArray2D est correcte !")
    return None


test_getRegularArray2D()

print("\nFonction getCarre2D :")


def test_getCarre2D() -> None:
    for i in range(5):
        liste = getCarre2D(random.randint(3, 6))
        print(liste)
    return None


test_getCarre2D()

print("\nFonction getSommeLignes :")


def test_getSommeLignes() -> None:
    for i in range(4):
        liste = getCarre2D(3)
        print(f"{liste}, somme des lignes : {getSommeLignes(liste)}")
    return None


test_getSommeLignes()

print("\nFonction getSommeColonnes :")


def test_getSommeColonnes() -> None:
    for i in range(4):
        liste = getCarre2D(3)
        print(f"{liste}, somme des colonnes : {getSommeColonnes(liste)}")
    return None


test_getSommeColonnes()

print("\nFonction getSommeDiagonale1 :")


def test_getSommeDiagonale1() -> None:
    for i in range(4):
        liste = getCarre2D(3)
        print(f"{liste}, somme de la diagonale principale : {getSommeDiagonale1(liste)}")
    return None


test_getSommeDiagonale1()
