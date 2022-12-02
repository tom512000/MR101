# view/Chrono.py

import pygame


class Chrono:
    """
    Classe gérant un chronomètre simple
    """
    def __init__(self):
        self._start = None
        self._end = None

    def start(self) -> None:
        """
        Démarre le chronomètre.
        """
        self._end = None
        self._start = pygame.time.get_ticks()

    def stop(self) -> int:
        """
        Stoppe le chrono et retourne le nombre de millisecondes écoulées
        depuis l'appel de la fonction start()

        :return: Nombre de millisecondes écoulées
        :raise: RuntimeError si le chronomètre n'a pas été démarré (méthode start())
        """
        if self._start is None:
            raise RuntimeError("La méthode start() n'a pas été appelée.")
        self._end = pygame.time.get_ticks()
        return self._end - self._start

    def getTime(self) -> str:
        """
        Retourne le temps écoulé sous la forme [jj] jours - hh:mm:ss.ms

        :return: Temps écoulé formaté
        :raise: RuntimeError si le chronomètre n'a pas été lancé et arrêté.
        """
        if self._start is None or self._end is None:
            raise RuntimeError("La méthode stop() n'a pas été appelée.")
        t = self._end - self._start
        ms = t % 1000
        t = t // 1000
        s = t % 60
        t = t // 60
        m = t % 60
        t = t // 60
        h = t % 24
        j = t // 24
        res = ""
        if j > 0:
            res = str(j) + " jours - "
        res += f"{h:02d}:{m:02d}:{s:02d}.{ms:03d}"
        return res

