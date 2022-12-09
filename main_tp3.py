# main_tp3.py
from TP3.tp3 import *

print("Fonction test_IndexOf :")


def test_indexOf() -> None:
    lst = [4, 2, 8, 5, 6, 5, 3, 1]
    print(f"Recherche de 5 dans {lst} : index = {indexOf(lst, 5)}")
    print(f"Recherche de 9 dans {lst} : index = {indexOf(lst, 9)}")
    return None


test_indexOf()

print("\nFonction test_indexOfSorted :")


def test_indexOfSorted() -> None:
    lst = [4, 2, 8, 5, 6, 5, 4, 1]
    lst.sort()
    print(f"Recherche de 5 dans {lst} : index, nombre itérations = {indexOfSorted(lst, 5)}")
    print(f"Recherche de 3 dans {lst} : index, nombre itérations = {indexOfSorted(lst, 3)}")
    return None


test_indexOfSorted()
