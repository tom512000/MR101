def getPrix(p: dict, a: str) -> float:
    return p.get(a, 0.0)


def getPrixTotal(p: dict) -> float:
    total = 0
    for element in p:
        total += p[element]
    return total
