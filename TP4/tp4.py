import random


def getRegularArray2D(nl: int, nc: int, mn: int, mx: int) -> list:
    liste = []
    for i in range(nl):
        ligne = []
        for j in range(nc):
            ligne += [random.randint(mn, mx)]
        liste += [ligne]
    return liste


