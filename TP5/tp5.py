def getPrix(p: dict, a: str) -> float:
    return p.get(a, 0.0)


def getPrixTotal(p: dict) -> float:
    total = 0
    for element in p:
        total += p[element]
    return total


def afficherPanier(p: dict) -> None:
    print(f"{'Articles':^20}{'Prix':^9}")
    print('-'*29)
    for element in p:
        print(f"{element:<19}:{p[element]:>9}")
    print('-' * 29)
    print(f"{'Prix total ':>19}:{round(getPrixTotal(p), 2):>9}")
    return None


def supprimerArticle(p: dict, a: str) -> bool:
    booleen = False
    a = a.title()
    if a in p:
        test1 = len(p)
        p.pop(a)
        test2 = len(p)
        if test1 != test2:
            booleen = True
    return booleen


def ajouterArticle(p: dict, a: str, px: float) -> None:
    a = a.title()
    p[a] = px
    return None
