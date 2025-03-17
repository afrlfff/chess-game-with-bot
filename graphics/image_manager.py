# image_manager.py

import pygame

class ImageManager:
    @staticmethod
    def load(filepath) -> pygame.Surface:
        if filepath.suffix == '.jpg':
            return pygame.image.load(filepath)
        if filepath.suffix == '.png':
            return pygame.image.load(filepath).convert_alpha()