# main_tp2.py

from TP1.tp1 import *
from TP2.tp2 import *
from view.Canvas import *
from view.Rect import *

print("\nFonction estTrie :")
print(estTrie([1]))
print(estTrie([2, 1]))

print("\nFonction echanger :")
a = [1, 2, 3, 4, 5, 6, 7]
print(a)
echanger(a, 1, 2)
print(a)

print("\nFonction triBulles :")
b = [0, -1, 8, 5, 21, -18, 2, 1]
print(b)
triBulles(b)
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

print("\nFonction: triSelectionRect / triBullesRect / triInsertionRect :")
nb = 20
tps = 0.5
f = []
for i in range(nb):
    f += [randint(20, 300)]
cv = Canvas((getCanvasSizeFrom(f)))
g = []
for j in range(len(f)):
    g += [Rect(j, f[j], cv)]
print("Lancement du tri : cliquez dans la fenêtre", waitClick())
# triSelectionRect(g, tps)
triBullesRect(g, tps)
# triSelectionRect(g, tps)
print("Fin du tri : cliquez pour finir", waitClick())
