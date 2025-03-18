# surface_manager.py
"""
    Contains Surface and SurfaceManager classes.
    
    Surface class defines surface object with base surface methods
    
    SurfaceManager class defines methods of creating a surfaces.
"""


import pygame
from typing import Tuple


class Surface:
    def __init__(self, surface: pygame.Surface):
        self.surface = surface

    def get_size(self):
        return self.surface.get_size()

    def get_rect(self):
        return self.surface.get_rect()
    
    def copy(self):
        return self.surface.copy()

class SurfaceManager:
    @staticmethod
    def create_surface(size: Tuple[int, int], alpha=False):
        if alpha:
            return pygame.Surface(size, pygame.SRCALPHA)
        else:
            return pygame.Surface(size)

    @staticmethod
    def create_text_surface(text, color, font, antialiasing=True) -> pygame.Surface:
        return font.render(text, antialiasing, color)