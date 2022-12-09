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
    while i != len(lst)-1 and a != False:
        if len(lst[i]) != len(lst[i + 1]):
            a = False
        i += 1
    return a


