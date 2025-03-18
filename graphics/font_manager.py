# font_manager.py

"""
    Contains class FontManager, made to create and store fonts in cache.
    
    Maybe will store some font manipulations in future
"""

import pygame
from constants import FONTS_PATH


class FontManager:
    _cache = {}

    @classmethod
    def get_font(cls, font_filename, font_size):
        key = cls._create_key(font_filename, font_size)
        if key not in cls._cache:
            cls._cache[key] = pygame.font.Font(FONTS_PATH / font_filename, font_size)
        return cls._cache[key]
    
    @classmethod
    def _create_key(cls, font_filename, font_size):
        return frozenset((font_filename, font_size))