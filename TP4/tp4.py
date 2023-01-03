import random


def getRegularArray2D(nl: int, nc: int, mn: int, mx: int) -> list:
    liste = []
    for i in range(nl):
        ligne = []
        for j in range(nc):
            ligne += [random.randint(mn, mx)]
        liste += [ligne]
    return liste


def isRegular(lst: list) -> bool:
    a = True
    i = 0
    while i != len(lst) - 1 and a != False:
        if len(lst[i]) != len(lst[i + 1]):
            a = False
        i += 1
    return a


def getMin(lst: list) -> int:
    a = lst[0][0]
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] < a:
                a = lst[i][j]
    return a


def getMax(lst: list) -> int:
    a = lst[0][0]
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] >= a:
                a = lst[i][j]
    return a


def getSize2D(liste: list) -> tuple:
    return len(liste), len(liste[0])


def getCarre2D(n: int) -> list:
    somme = n * (n ** 2 + 1) / 2
    nombres = []
    for i in range(1, (n ** 2) + 1):
        nombres += [i]
    random.shuffle(nombres)
    tab = []
    for i in range(n):
        ligne = []
        for j in range(n):
            ligne += [nombres[0]]
            del nombres[0]
        tab += [ligne]
    return tab


def getSommeLignes(liste: list) -> list:
    totlignes = len(liste) * [0]
    for i in range(len(liste)):
        for j in range(len(liste[i])):
            totlignes[i] += liste[i][j]
    return totlignes


def getSommeColonnes(liste: list) -> list:
    totcolonnes = len(liste[0]) * [0]
    nb = -1
    for j in range(len(totcolonnes)):
        nb += 1
        for i in range(len(liste)):
            totcolonnes[nb] += liste[i][nb]
    return totcolonnes


def getSommeDiagonale1(liste: list) -> int:
    totdiag1 = 0
    nb = -1
    for i in range(len(liste)):
        nb += 1
        totdiag1 += liste[i][nb]
    return totdiag1


def getSommeDiagonale2(liste: list) -> int:
    totdiag2 = 0
    nb = -1
    for i in range(len(liste)-1, -1, -1):
        nb += 1
        totdiag2 += liste[i][nb]
    return totdiag2
