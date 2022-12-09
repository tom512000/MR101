def indexOf(liste: list, val: int) -> int:
    i = 0
    a = -1
    b = False
    while b != True and i != len(liste):
        if liste[i] == val:
            b = True
            a = i
        i += 1
    return a


def indexOfSorted(liste: list, val: int) -> tuple:
    i = 0
    while i != len(liste) and liste[i] < val:
        i += 1
    return indexOf(liste, val), i


def binarySearch(lst: list, val: list) -> int:
    return indexOf(lst, val)


def getReponse(val: int) -> None:
    ideb = 0
    ifin = val
    imilieu = (ideb + ifin) // 2
    a = ''
    while imilieu != val and a != 'E':
        print(f"Proposition de l'ordinateur : {imilieu}")
        a = input("Votre nombre est-il (E)gal, plus (G)rand ou plus (P)etit ? (tapez E, G ou P) : ")
        if a == 'P':
            ifin = val
        elif a == 'G':
            ideb = val
        imilieu = (ideb + ifin) // 2
    print(f"Proposition de l'ordinateur : {imilieu}")
    return None


def devinerNombre(mn: int, mx: int) -> None:
    justeprix = int(input(f"Choisissez un nombre entre {mn} et {mx} :"))
    n = 100000
    a = 1
    b = n
    nbre_reponses = 0
    while b - a >= 0:
        rep = (a + b) // 2
    nbre_reponses += 1
    if rep == justeprix:
        print(f"la bonne réponse est : {rep}")
    elif rep > justeprix:
        b = rep - 1
    else:
        a = rep + 1
    print("le nombre de réponses est : {nbre_reponses}")
    return justeprix

