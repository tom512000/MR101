import random


def getRandomList(taille: int, mn: int, mx: int) -> list:
    liste = []
    for i in range(taille):
        liste += [random.randint(mn, mx)]
    return liste


def compter(lst: list, elmt: int) -> int:
    iter = 0
    for i in range(len(lst)):
        if lst[i] == elmt:
            iter += 1
    return iter


def contient(liste: list, entier: int) -> bool:
    bl = False
    for i in range(len(liste)):
        if liste[i] == entier:
            bl = True
    return bl

