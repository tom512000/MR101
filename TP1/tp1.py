from random import randint


def getRandomList(taille: int, mn: int, mx: int) -> list:
    liste = []
    for i in range(taille):
        liste += [randint(mn, mx)]
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
    while i != len(liste) and j == -1:
        if liste[i] == entier:
            j = i
        i += 1
    return j


def lastIndexOf(liste: list, entier: int) -> int:
    j = -1
    for i in range(len(liste)):
        if liste[i] == entier:
            j = i
    return j


def nthIndexOf(liste: list, n: int, elmt: int) -> int:
    i = 0
    a = -1
    while i != len(liste) and n != 0:
        if liste[i] == elmt:
            n -= 1
        if n == 0:
            a = i
        i += 1
    return a


def creerListeSansDoublon(liste: list) -> list:
    i = 0
    liste2 = []
    while i != len(liste):
        if liste[i] not in liste2:
            liste2 += [liste[i]]
        i += 1
    return liste2


