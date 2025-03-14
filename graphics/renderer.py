# renderer.py
"""
    Defines base methods od screen drawing
"""


import pygame
from typing import Tuple

from assets import Assets

class Renderer:
    def __init__(self, game):
        self.game = game
        self.assets = Assets()
    
    def render(self):
        self.draw_chess_board()
        self.draw_chess_piece()

    def draw_chess_board(self):
        pass

    def draw_chess_piece(self, piece):
        pass

    def draw_image(self, img, size: Tuple[int, int]):
        pass
