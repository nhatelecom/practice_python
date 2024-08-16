import numpy as np

class Board:

    def __init__(self, screen, height=20, width=10):
        self.height = height
        self.width = width
        self._screen = screen
        self._matrix = np.zeros([width,height], dtype=int)
        self._current_tile = None
        self._score = 0
        