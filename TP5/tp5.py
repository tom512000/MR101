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
    print(f"{'Prix total ':>19}:{getPrixTotal(p):>9}")
    return None
