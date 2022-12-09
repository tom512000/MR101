# tests/tests_tp2.py

import unittest
from TP3.tp3 import *
from random import randint


class TestTP3(unittest.TestCase):

    @staticmethod
    def get_rnd_list(n: int, mn: int, mx: int) -> list:
        return [randint(mn, mx) for i in range(n)]

    @unittest.skipIf('indexOf' not in globals(),
                     "Il manque la fonction indexOf")
    def test_indexOf(self):
        for i in range(10_000):
            lst = TestTP3.get_rnd_list(randint(0, 20), -randint(1, 10), randint(1, 10))
            v = randint(-10, 10)
            id = indexOf(lst, v)
            id_r = lst.index(v) if v in lst else -1
            self.assertEqual(id_r, id, f"La fonction indexOf pour lst={lst} et val={v} devrait retourner {id_r} et non {id}")

    @unittest.skipIf('indexOfSorted' not in globals(),
                     "Il manque la fonction indexOfSorted")
    def test_indexOfSorted(self):
        for i in range(10_000):
            l1 = sorted(TestTP3.get_rnd_list(randint(1, 20), -randint(1, 10), randint(1, 10)))
            v = randint(-10, 10)
            id, iter = indexOfSorted(l1, v)
            id_r = l1.index(v) if v in l1 else -1
            self.assertEqual(id_r, id, f"La position de {v} dans {l1} devrait être {id_r} au lieu de {id}")
            iter_r = len([e for e in l1 if e < v])
            self.assertTrue(abs(iter_r - iter) <= 1, f"Le nombre d'itérations devrait être à peu près égal à {iter_r} et non {iter}")

    @unittest.skipIf('binarySearch' not in globals(),
                     "Il manque la fonction binarySearch")
    def test_binarySearch(self):
        for i in range(10_000):
            lst = sorted(TestTP3.get_rnd_list(randint(1, 20), -randint(1, 10), randint(1, 10)))
            v = randint(-10, 10)
            id = binarySearch(lst, v)
            self.assertTrue(lst[id] == v if v in lst else id == -1, f"Erreur sur la liste {lst} : indice de {v} donne {id} ??")


