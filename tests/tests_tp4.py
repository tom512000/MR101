# tests/tests_tp4.py

import unittest
from TP4.tp4 import *
from random import randint


class TestTP4(unittest.TestCase):

    @staticmethod
    def get_rnd_list(n: int, mn: int, mx: int) -> list:
        return [randint(mn, mx) for i in range(n)]

    @unittest.skipIf('isRegular' not in globals(),
                     "Il manque la fonction isRegular")
    def test_isRegular(self):
        # n = 0
        for i in range(10_000):
            lst = [[randint(-10, 10) for j in range(randint(1, 10))] for i in range(randint(1, 10))]
            r_e = [len(l) for l in lst].count(len(lst[0])) == len(lst)
            r_g = isRegular(lst)
        #    if r_e:
        #        n += 1
            self.assertEqual(r_e, r_g, f"La fonction isRegular pour lst={lst} devrait retourner {r_e} et non {r_g}")
        # print(n, "tableaux réguliers...")

    @unittest.skipIf('getMin' not in globals() or 'getMax' not in globals(),
                     "Il manque la fonction getMin ou la fonction getMax")
    def test_getMinMax(self):
        # n = 0
        for i in range(10_000):
            lst = [[randint(-10, 10) for j in range(randint(1, 10))] for i in range(randint(1, 10))]
            mn = min([min(l) for l in lst])
            mx = max([max(l) for l in lst])
            _mn = getMin(lst)
            self.assertEqual(mn, _mn, f"La fonction getMin pour lst={lst} devrait retourner {mn} et non {_mn}")
            _mx = getMax(lst)
            self.assertEqual(mx, _mx, f"La fonction getMax pour lst={lst} devrait retourner {mx} et non {_mx}")
        # print(n, "tableaux réguliers...")

    @unittest.skipIf('getCarre2D' not in globals(),
                     "Il manque la fonction getCarre2D")
    def test_getCarre2D(self):
        for i in range(100):
            dim = randint(3, 10)
            tab = getCarre2D(dim)
            self.assertEqual(dim, len(tab), f"Le nombre de lignes de {tab} devrait être de {dim} et non de {len(tab)}")
            self.assertTrue([len(l) for l in tab].count(dim) == dim,
                            f"Le tableau {tab} n'est pas régulier ou ne possède pas {dim} colonnes")
            for n in range(1, dim*dim + 1):
                nb = sum([ 1 if n in l else 0 for l in tab])
                self.assertEqual(1, nb, f"Le carré {tab} contient {nb} fois le nombre {n} au lieu de 1 fois.")

    @unittest.skipIf('getSommeLignes' not in globals() or 'getCarre2D' not in globals(),
                     "Il manque la fonction getCarre2D ou la fonction getSommeLignes")
    def test_getSommeLignes(self):
        for i in range(1000):
            dim = randint(3, 10)
            tab = getCarre2D(dim)
            s_l_e = [sum(l) for l in tab]
            s_l_g = getSommeLignes(tab)
            self.assertEqual(s_l_e, s_l_g, f"Les sommes de lignes de {tab} devrait être {s_l_e} et non {s_l_g}")

    @unittest.skipIf('getSommeColonnes' not in globals() or 'getCarre2D' not in globals(),
                     "Il manque la fonction getCarre2D ou la fonction getSommeColonnes")
    def test_getSommeColonnes(self):
        for i in range(1000):
            dim = randint(3, 10)
            tab = getCarre2D(dim)
            s_c_e = [sum([tab[j][i] for j in range(dim)]) for i in range(dim)]
            s_c_g = getSommeColonnes(tab)
            self.assertEqual(s_c_e, s_c_g, f"Les sommes de colonnes de {tab} devrait être {s_c_e} et non {s_c_g}")

    @unittest.skipIf('getSommeDiagonale1' not in globals() or 'getCarre2D' not in globals(),
                     "Il manque la fonction getCarre2D ou la fonction getSommeDiagonale1")
    def test_getSommeDiagonale1(self):
        for i in range(1000):
            dim = randint(3, 10)
            tab = getCarre2D(dim)
            s_d_e = sum([l[i] for i, l in enumerate(tab)])
            s_d_g = getSommeDiagonale1(tab)
            self.assertEqual(s_d_e, s_d_g, f"La somme de la diagonale principale de {tab} devrait être {s_d_e} et non {s_d_g}")

    @unittest.skipIf('getSommeDiagonale2' not in globals() or 'getCarre2D' not in globals(),
                     "Il manque la fonction getCarre2D ou la fonction getSommeDiagonale2")
    def test_getSommeDiagonale2(self):
        for i in range(1000):
            dim = randint(3, 10)
            tab = getCarre2D(dim)
            dim -= 1
            s_d_e = sum([l[dim - i] for i, l in enumerate(tab)])
            s_d_g = getSommeDiagonale2(tab)
            self.assertEqual(s_d_e, s_d_g, f"La somme de la diagonale secondaire de {tab} devrait être {s_d_e} et non {s_d_g}")

    @unittest.skipIf('getArray2D' not in globals(),
                     "Il manque la fonction getArray2D")
    def test_getArray2D(self):
        for i in range(100):
            lst = [randint(0, 10) for i in range(randint(1, 10))]
            tab = getArray2D(lst)
            # Vérification du nombre d'éléments
            self.assertEqual(sum(lst), sum([l.count(0) for l in tab]),
                             f"Le nombre d'éléments de {tab} ne correspond pas aux dimensions données {lst}")
            # Vérification du nombre d'éléments par ligne
            self.assertEqual(lst, [len(l) for l in tab],
                             f"Le nombre d'éléments dans chaque ligne de {tab} ne correspond pas aux dimensions données {lst}")
            # Vérification de la non redondance des lignes...
            for n in range(100):
                _i = randint(0, len(lst) - 1)
                if lst[_i] > 0:
                    _j = randint(0, lst[_i] - 1)
                    tab[_i][_j] = 1
                    self.assertEqual(1, sum([sum(l) for l in tab]),
                                     f"L'élément [{_i}][{_j}] est dupliqué dans {tab}")
                    tab[_i][_j] = 0

    @unittest.skipIf('getArray2D' not in globals() or 'getNbParLigne' not in globals(),
                     "Il manque la fonction getArray2D ou la fonction getNbParLigne")
    def test_getNbParLigne(self):
        for i in range(1000):
            lst = [randint(0, 10) for i in range(randint(1, 10))]
            tab = getArray2D(lst)
            res = getNbParLigne(tab)
            # Vérification du nombre d'éléments
            self.assertEqual(lst, res,
                             f"Le nombre d'éléments par ligne de {tab} devrait être {lst} et non {res}")

    @unittest.skipIf('getArray2D' not in globals() or 'remplir2D' not in globals() or 'transforme2D1D' not in globals(),
                     "Il manque la fonction getArray2D ou la fonction remplir2D ou la fonction transforme2D1D")
    def test_transforme2D1D(self):
        for i in range(1000):
            lst = [randint(0, 10) for i in range(randint(1, 10))]
            tab = getArray2D(lst)
            remplir2D(tab, -10, 10)
            res = transforme2D1D(tab)
            # Vérification du nombre d'éléments
            _i = 0
            for li in tab:
                for e in li:
                    self.assertEqual(e, res[_i],
                                     f"Transformation de {tab}: l'élément n°{_i} devrait être {e} et non {res[_i]} dans {res} ")
                    _i += 1

    @unittest.skipIf('transforme1D2D' not in globals(),
                     "Il manque la fonction transforme1D2D")
    def test_transforme1D2D(self):
        for i in range(10000):
            lst = [randint(-1, 5) for i in range(randint(1, 20))]
            tab = transforme1D2D(lst, -1)
            # Utilisation de la fonction split pour tester
            s = " ".join([str(e) for e in lst])
            arr = s.split("-1")
            try:
                tab2 = [[int(e) for e in s.strip().split(" ")] if len(s.strip()) > 0 else [] for s in arr]
            except ValueError as err:
                print()
                print(s, arr)
                raise err
            # Test sur le nombre de lignes
            self.assertEqual(len(tab2), len(tab),
                             f"La transformation de {lst} devrait donner {tab2} et non {tab}")
            # Vérification des éléments
            for i in range(len(tab)):
                self.assertEqual(tab2[i], tab[i],
                                 f"La transformation de {lst} devrait donner {tab2} et non {tab}")
