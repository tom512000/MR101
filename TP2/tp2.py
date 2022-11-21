def estTrie(liste: list) -> bool:
    bl = True
    for i in range(len(liste)-1):
        if liste[i] > liste[i+1]:
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
        for i in range(len(liste)-1):
            if liste[i] > liste[i+1]:
                echanger(liste, i, i+1)
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


