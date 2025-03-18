# surface_manager.py
"""
    Contains Surface and SurfaceManager classes.
    
    Surface class defines surface object with base surface methods
    
    SurfaceManager class defines methods of creating a surfaces.
"""


import pygame
from typing import Tuple
from .font import FontBase


class Surface:
    def __init__(self, size, flags=0, depth=0, masks=None):
        self.surface = pygame.Surface(size, flags, depth, masks)

    def get_size(self):
        """ Returns surface size in pixels """
        return self.surface.get_size()

    def get_rect(self):
        """ Returns surface rectangle """
        return self.surface.get_rect()
    
    def copy(self):
        """ Returns the copy of teh surface """
        return self.surface.copy()
    
    def get_width(self):
        """ Returns width of the surface in pixels """
        return self.surface.get_width()
    
    def get_height(self):
        """ Returns height of the surface in pixels """
        return self.surface.get_height()

class SurfaceManager:
    @staticmethod
    def create_surface(size: Tuple[int, int], alpha=False) -> Surface:
        if alpha:
            return Surface(size, pygame.SRCALPHA)
        else:
            return Surface(size)

    @staticmethod
    def create_text_surface(text: str, color, font: FontBase, antialias=True, background=None) -> Surface:
        return font.render(text, antialias, color, background)