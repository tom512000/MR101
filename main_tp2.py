# main_tp2.py

from TP1.tp1 import getRandomList
from TP2.tp2 import *

print("Fonction estTrie :")
print(estTrie([1]))
print(estTrie([2, 1]))

print("\nFonction echanger :")
a = [1, 2, 3, 4, 5, 6, 7]
print(a)
print(echanger(a, 1, 2))
print(a)

print("\nFonction triBulles :")
b = [0, -1, 8, 5, 21, -18, 2, 1]
print(b)
print(triBulles(b))
print(b)

print("\nFonction deplacerCase :")
print("   Test 1 :")
c = [1, 3, 3, 4, 6, 8, 2, 6, 4, 9]
print(c)
deplacerCase(c, 6)
print(c)

print("   Test 2 :")
d = [1, 3, 3, 4, 6, 8, 0, 6, 4, 9]
print(d)
deplacerCase(d, 6)
print(d)

print("\nFonction: triInsertion :")
e = [1, 3, 3, 4, 6, 8, 0, 6, 4, 9]
print(e)
triInsertion(e)
print(e)
