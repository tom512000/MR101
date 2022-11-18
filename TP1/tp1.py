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


def firstIndexOf(liste: list, entier: int) -> int:
    j = -1
    i = 0
    while i != len(liste):
        if liste[i] == entier:
            j = i
            break
        i += 1
    return j


def lastIndexOf(liste: list, entier: int) -> int:
    j = -1
    for i in range(len(liste)):
        if liste[i] == entier:
            j = i
    return j

