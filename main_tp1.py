# main_tp1.py

from TP1.tp1 import *


for i in range(5):
    print(getRandomList(10, -20, 20))


print(compter(getRandomList(10, -20, 20), 0))
print(compter(getRandomList(10, -20, 20), 10))


liste = [5, 2, 4, 2, 7, 5, 6, 2, 7, 4, 5, 7, 9]
supprimerDoublons(liste)
print(liste)

