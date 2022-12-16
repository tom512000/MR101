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
            if lst[i][j] > a:
                a = lst[i][j]
    return a

























