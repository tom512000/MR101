from view.Canvas import *
from view.Rect import *


def estTrie(liste: list) -> bool:
    bl = True
    for i in range(len(liste) - 1):
        if liste[i] > liste[i + 1]:
            bl = False
    return bl


def echanger(liste: list, i1: int, i2: int) -> None:
    a = liste[i1]
    liste[i1] = liste[i2]
    liste[i2] = a
    return None


def triBulles(liste: list) -> None:
    etape = 1
    modif = True
    while modif:
        modif = False
        for i in range(len(liste) - 1):
            if liste[i] > liste[i + 1]:
                echanger(liste, i, i + 1)
                modif = True
        etape += 1
    return None


def getMin(liste: list) -> int:
    min = liste[0]
    for i in range(1, len(liste)):
        if liste[i] < min:
            min = liste[i]
    return min


def getIndexMin(liste: list) -> int:
    min = liste[0]
    idmin = 0
    for i in range(1, len(liste)):
        if liste[i] < min:
            min = liste[i]
            idmin = i
    return idmin


def getIndexMinFrom(liste: list, depart: int) -> int:
    min = liste[depart]
    idmin = depart
    for i in range(depart + 1, len(liste)):
        if liste[i] < min:
            min = liste[i]
            idmin = i
    return idmin


def triSelection(liste: list) -> None:
    n = len(liste)
    for i in range(0, n):
        min = i
        for j in range(i + 1, n):
            if liste[j] < liste[min]:
                min = j
        if min is not i:
            temp = liste[i]
            liste[i] = liste[min]
            liste[min] = temp
    return None


def deplacerCase(liste: list, i: int) -> None:
    j = i
    while j != 0:
        if liste[j] < liste[j - 1]:
            echanger(liste, j, j - 1)
        j -= 1
    return None


def triInsertion(liste: list) -> None:
    for i in range(1, len(liste)):
        x = liste[i]
        j = i
        while j > 0 and liste[j - 1] > x:
            deplacerCase(liste, j)
            j -= 1
    return None


def triSelectionRect(liste: list, tps: float) -> None:
    for i in range(0, len(liste)):
        min = i
        for j in range(i + 1, len(liste)):
            if liste[j].getHeight() < liste[min].getHeight():
                min = j
        if min is not i:
            tmp = liste[i]
            tmp.unsetX(tps)
            liste[i] = liste[min]
            liste[i].setX(i, tps)
            liste[min] = tmp
            liste[min].setX(min, tps)
            liste[i].setPlaced()
    return None


def triBullesRect(liste: list, tps: float) -> None:
    etape = 1
    modif = True
    while modif:
        modif = False
        for i in range(len(liste) - 1):
            if liste[i].getHeight() > liste[i + 1].getHeight():
                tmp = liste[i]
                tmp.unsetX(tps)
                liste[i] = liste[i + 1]
                liste[i].setX(i, tps)
                liste[i + 1] = tmp
                liste[i + 1].setX(i + 1, tps)
                liste[i].setPlaced()
                modif = True
        etape += 1
    return None


def triInsertionRect(liste: list, tps: float) -> None:
    for i in range(1, len(liste)):
        x = liste[i].getHeight()
        j = i
        while j > 0 and liste[j - 1].getHeight() > x:
            # Déplacer case
            a = i
            while a != 0:
                if liste[a].getHeight() < liste[a - 1].getHeight():
                    tmp = liste[a]
                    tmp.unsetX(tps)
                    liste[a] = liste[a - 1]
                    liste[a].setX(a, tps)
                    liste[a - 1] = tmp
                    liste[a - 1].setX(a - 1, tps)
                    liste[a].setPlaced()
                a -= 1
            j -= 1
    return None


def doQuickSort(liste: list, ideb: int, ifin: int) -> None:
    pivot = liste[ideb]
    i = ifin - 1
    for j in range(ifin, ideb):
        if liste[j] <= pivot:
            i = i + 1
            (liste[i], liste[j]) = (liste[j], liste[i])
    (liste[i + 1], liste[ideb]) = (liste[ideb], liste[i + 1])
    return i + 1


def quickSort(liste: list) -> None:
    for i in range(len(liste) - 1):
        doQuickSort(liste, i, i + 1)
        return None
