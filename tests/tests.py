# tests/tests.py

import unittest
import sys

# Pour pouvoir l'exécuter depuis le répertoire tests/
sys.path.insert(0, "..")

# Inclusion des tests à faire
from tests_tp1 import TestTP1

# Eviter l'exécution depuis un environnement comme Jupyter
if __name__ == "__main__":
    unittest.main()

