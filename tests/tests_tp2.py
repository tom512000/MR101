# tests/tests_tp2.py

import unittest
from TP1.tp1 import getRandomList
from TP2.tp2 import *
from random import randint


class TestTP2(unittest.TestCase):

    @unittest.skipIf('estTrie' not in globals(),
                     "Il manque la fonction estTrie")
    def test_estTrie(self):
        lst = getRandomList(randint(1, 20), -randint(1, 10), randint(1, 10))
        lst.sort()
        self.assertTrue(estTrie(lst), f"La fonction devrait retourner True pour la liste {lst}")
        n = 0
        b = False
        while not(b) and n<10:
            n += 1
            i1 = randint(0, len(lst) - 1)
            i2 = randint(0, len(lst) - 1)
            if i1 != i2 and lst[i1] != lst[i2]:
                lst[i1], lst[i2] = lst[i2], lst[i1]
                self.assertFalse(estTrie(lst), f"La fonction dervait retourner False pour la liste {lst}")
                b = True

    @unittest.skipIf('triBulles' not in globals(),
                     "Il manque la fonction triBulles")
    def test_triBulles(self):
        for i in range(10_000):
            l1 = getRandomList(randint(1, 20), -randint(1, 10), randint(1, 10))
            l2 = l1.copy()
            triBulles(l1)
            l2.sort()
            self.assertEqual(l2, l1, f"La liste {l1} n'est pas triÃ©e, on devrait avoir {l2}")

    @unittest.skipIf('getMin' not in globals(),
                     "Il manque la fonction getMin")
    def test_getMin(self):
        for i in range(1000):
            lst = getRandomList(randint(1, 20), -randint(1, 1_000_000), randint(1, 1_000_000))
            mn = getMin(lst)
            self.assertEqual(min(lst), mn, f"La liste getMin devrait retourner {min(lst)} sur {lst} au lieu de {mn}")

    @unittest.skipIf('getIndexMin' not in globals(),
                     "Il manque la fonction getIndexMin")
    def test_getIndexMin(self):
        for i in range(1000):
            lst = getRandomList(randint(1, 20), -randint(1, 1_000_000), randint(1, 1_000_000))
            idx = getIndexMin(lst)
            self.assertEqual(min(lst), lst[idx],
                             f"l'indice {idx} dans la liste {lst} ne correspond pas Ã  la valeur minimale {min(lst)}")

    @unittest.skipIf('getIndexMinFrom' not in globals(),
                     "Il manque la fonction getIndexMinFrom")
    def test_getIndexMinFrom(self):
        for i in range(1000):
            lst = getRandomList(randint(1, 20), -randint(1, 1_000_000), randint(1, 1_000_000))
            dep = randint(0, len(lst) - 1)
            idx = getIndexMinFrom(lst, dep)
            self.assertTrue(min(lst[dep:]) == lst[idx] and idx >= dep,
    f"l'indice {idx} dans la liste {lst} ne correspond pas Ã  la valeur minimale {min(lst[dep:])} ou la position {idx} est infÃ©rieur au dÃ©but de la recherche {dep}")

    @unittest.skipIf('triSelection' not in globals(),
                     "Il manque la fonction triSelection")
    def test_triSelection(self):
        for i in range(1000):
            l1 = getRandomList(randint(1, 20), -randint(1, 100), randint(1, 100))
            l2 = l1.copy()
            triSelection(l1)
            l2.sort()
            self.assertEqual(l2, l1, f"La liste {l1} n'est pas triÃ©e, on devrait avoir {l2}")

    @unittest.skipIf('deplacerCase' not in globals(),
                     "Il manque la fonction deplacerCase")
    def test_deplacerCase(self):
        for i in range(1000):
            l1 = getRandomList(randint(2, 20), -randint(1, 100), randint(1, 100))
            pos = randint(1, len(l1)-1)
            l1 = sorted(l1[0:pos]) + l1[pos:]
            l2 = l1.copy()
            deplacerCase(l2, pos)
            l3 = sorted(l1[0:pos+1]) + l1[pos+1:] if pos < len(l1) else []
            self.assertEqual(l3, l2, f"Le dÃ©placement de la case d'indice {pos} de la liste {l1} aurait dÃ» donner {l3} au lieu de {l2}")

    @unittest.skipIf('triInsertion' not in globals(),
                     "Il manque la fonction triInsertion")
    def test_triInsertion(self):
        for i in range(1000):
            l1 = getRandomList(randint(1, 20), -randint(1, 100), randint(1, 100))
            l2 = l1.copy()
            triInsertion(l1)
            l2.sort()
            self.assertEqual(l2, l1, f"La liste {l1} n'est pas triÃ©e, on devrait avoir {l2}")

    @unittest.skipIf('quickSort' not in globals(),
                     "Il manque la fonction quickSort")
    def test_quickSort(self):
        for i in range(1000):
            l1 = getRandomList(randint(1, 20), -randint(1, 100), randint(1, 100))
            l2 = l1.copy()
            quickSort(l1)
            l2.sort()
            self.assertEqual(l2, l1, f"La liste {l1} n'est pas triÃ©e, on devrait avoir {l2}")

