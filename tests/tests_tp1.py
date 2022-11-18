# tests/tests_tp1.py

import unittest
from TP1.tp1 import *
from random import randint


class TestTP1(unittest.TestCase):

    @unittest.skipIf('compter' not in globals() or 'getRandomList' not in globals(),
                     "Il manque une des fonctions getRandomList ou compter")
    def test_compter(self):
        # Test de la fonction compte
        lst = getRandomList(randint(0, 100), -10, 10)
        for j in range(1000):
            v = randint(-10, 10)
            n = compter(lst, v)
            self.assertEqual(lst.count(v), n, f"Le nombre d'occurrences de {v} dans {lst} devrait Ãªtre {lst.count(v)} au lieu de {n}")

    @unittest.skipIf('contient' not in globals() or 'getRandomList' not in globals(),
                     "Il manque une des fonctions getRandomList ou contient")
    def test_contient(self):
        # Test de la fonction contient
        for i in range(1000):
            lst = getRandomList(randint(0, 10), -100, 100)
            for j in range(100):
                v = randint(-100, 100)
                self.assertEqual(contient(lst, v), v in lst,
                                 f"{lst} contient {v} devrait retourner {v in lst}.")

    @unittest.skipIf('firstIndexOf' not in globals() or 'getRandomList' not in globals(),
                     "Il manque une des fonctions getRandomList ou firstIndexOf")
    def test_firstIndexOf(self):
        # Test de la fonction contient
        for i in range(1000):
            lst = getRandomList(randint(0, 10), -100, 100)
            for j in range(100):
                v = randint(-100, 100)
                n1 = firstIndexOf(lst, v)
                n2 = lst.index(v) if v in lst else -1
                self.assertEqual(n2, n1,
                                 f"firstIndexOf({lst}, {v}) devrait retourner {n2} au lieu de {n1}.")

    @unittest.skipIf('lastIndexOf' not in globals() or 'getRandomList' not in globals(),
                     "Il manque une des fonctions getRandomList ou lastIndexOf")
    def test_lastIndexOf(self):
        # Test de la fonction contient
        for i in range(1000):
            lst = getRandomList(randint(0, 10), -100, 100)
            for j in range(100):
                v = randint(-100, 100)
                n1 = lastIndexOf(lst, v)
                lst.reverse()
                n2 = len(lst) - 1 - lst.index(v) if v in lst else -1
                lst.reverse()
                self.assertEqual(n2, n1,
                                 f"lastIndexOf({lst}, {v}) devrait retourner {n2} au lieu de {n1}.")

    @unittest.skipIf('nthIndexOf' not in globals() or 'getRandomList' not in globals(),
                     "Il manque une des fonctions getRandomList ou nthIndexOf")
    def test_nthIndexOf(self):
        for i in range(1000):
            lst = getRandomList(randint(0, 10), -2, 2)
            for j in range(100):
                v = randint(-2, 2)
                n = randint(0, len(lst))
                n1 = nthIndexOf(lst, n, v)
                vals = [i for i, _v in enumerate(lst) if _v == v]
                n2 = vals[n - 1] if len(vals) >= n > 0 else -1
                self.assertEqual(n2, n1,
                                 f"{n}Ã¨me position de {v} dans {lst} devrait retourner {n2} au lieu de {n1}.")

    @unittest.skipIf('creerListeSansDoublon' not in globals() or 'getRandomList' not in globals(),
                     "Il manque une des fonctions creerListeSansDoublon ou getRandomList")
    def test_creerListeSansDoublon(self):
        for i in range(10_000):
            lst = getRandomList(randint(0, 10), -2, 2)
            lst1 = creerListeSansDoublon(lst)
            lst2 = [v for i, v in enumerate(lst) if v not in lst[:i]]
            self.assertEqual(lst2, lst1, f"{lst} sans doublon devrait donner {lst2} au lieu de {lst1}")

    @unittest.skipIf('supprimerDoublons' not in globals() or 'getRandomList' not in globals(),
                     "Il manque une des fonctions supprimerDoublons ou getRandomList")
    def test_supprimerDoublons(self):
        for i in range(10_000):
            lst = getRandomList(randint(0, 10), -2, 2)
            lst1 = lst.copy()
            supprimerDoublons(lst1)
            lst2 = [v for i, v in enumerate(lst) if v not in lst[:i]]
            self.assertEqual(lst2, lst1, f"{lst} sans doublon devrait donner {lst2} au lieu de {lst1}")