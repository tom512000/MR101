def estTrie(liste: list) -> bool:
    bl = True
    for i in range(len(liste)-1):
        if liste[i] > liste[i+1]:
            bl = False
    return bl

