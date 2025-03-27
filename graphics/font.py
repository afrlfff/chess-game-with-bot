# font_manager.py

"""
    This module provides tools for managing and rendering fonts in a Pygame application. 

    It includes `FontBase`, an abstract class for font handling, and `FontManager` 
    for caching and retrieving fonts efficiently. Subclasses like `RussoOneRegular` 
    implement specific font behaviors.
"""

import pygame
from abc import ABC, abstractmethod
from constants import FONTS_PATH, RUSSO_ONE_REGULAR
from .surface import Surface


class FontBase(ABC):
    def __init__(self, font_size: int):
        self.font = self._create_font(font_size)
        self.size = font_size
    
    @abstractmethod
    def _create_font(self, font_size: int) -> pygame.font.Font:
        """ Method should be implemented in a subclasses """
        pass

    def with_size(self, font_size: int):
        return self.__class__(font_size)

    def get_height(self):
        """ Returns height of the font in pixels """
        return self.font.get_height()
    
    def get_linesize(self):
        """ Returns line height in pixels which font takes """
        return self.font.get_linesize()
    
    def get_text_size(self, text: str):
        """ Returns size of the given text in pixels """
        return self.font.size(text)
    
    def to_surface(self, text: str, antialias: bool, color, background=None):
        """ Renders given text as a surface """
        return Surface(self.font.render(text, antialias, color, background))


class FontManager:
    _cache = {}

    @classmethod
    def get_font(cls, font_filename, font_size) -> pygame.font.Font:
        key = cls._create_key(font_filename, font_size)
        if key not in cls._cache:
            cls._cache[key] = pygame.font.Font(FONTS_PATH / font_filename, font_size)
        return cls._cache[key]
    
    @classmethod
    def _create_key(cls, font_filename, font_size):
        return frozenset((font_filename, font_size))


# ========= Font subclasses

class RussoOneRegular(FontBase):
    def _create_font(self, font_size: int) -> pygame.font.Font:
        return FontManager.get_font(RUSSO_ONE_REGULAR, font_size)