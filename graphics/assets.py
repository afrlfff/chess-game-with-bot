# assets.py

import pygame

from constants import IMG_PATH
from utils import singleton

@singleton
class Assets:
    def __init__(self):
        self.chess_piece_images = {}
        self.chess_board_images = {}

    def load_assets(self):
        self.load_chess_piece_images()
        self.load_chess_board_images()

    def load_chess_piece_images(self):
        for filepath in (IMG_PATH / 'chess-pieces').iterdir():
            filename = filepath.stem
            self.chess_piece_images[filename] = pygame.image.load(filepath).convert_alpha()
    
    def load_chess_board_images(self):
        for filepath in (IMG_PATH / 'chess-boards').iterdir():
            filename = filepath.stem
            self.chess_board_images[filename] = pygame.image.load(filepath).convert_alpha()

    