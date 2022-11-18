import random


def getRandomList(taille: int, mn: int, mx: int) -> list:
    liste = []
    for i in range(taille):
        liste += [random.randint(mn, mx)]
    return liste

