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

