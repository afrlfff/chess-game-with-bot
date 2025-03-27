# surface.py

"""
    This module provides the `Surface` class, which wraps a Pygame surface to provide 
    a simplified and extended interface for common graphical operations.
"""


import pygame
from pygame import surfarray
import numpy as np

class Surface:
    def __init__(self, surface: pygame.Surface):        
        self.surface = surface

    def fill(self, color, rect=None):
        return self.surface.fill(color, rect)

    def blit(self, source: 'Surface', dest, area = None):
        return self.surface.blit(source.surface, dest, area)

    def draw_rect(self, color, rect, width=0):
        pygame.draw.rect(self.surface, color, rect, width)

    def draw_circle(self, color, center, radius, width=0):
        pygame.draw.circle(self.surface, color, center, radius, width)

    def get_pixels(self):
        if self.surface.get_flags() & pygame.SRCALPHA:
            rgb = surfarray.array3d(self.surface)
            alpha = surfarray.array_alpha(self.surface)
            return np.dstack((rgb, alpha))
        else:
            return surfarray.array3d(self.surface)

    def get_size(self):
        """ Returns surface size in pixels """
        return self.surface.get_size()
    
    def get_flags(self):
        return self.surface.get_flags()

    def get_rect(self):
        """ Returns surface rectangle """
        return self.surface.get_rect()
    
    def copy(self):
        """ Returns the copy of the surface """
        return self.surface.copy()
    
    def get_width(self):
        """ Returns width of the surface in pixels """
        return self.surface.get_width()
    
    def get_height(self):
        """ Returns height of the surface in pixels """
        return self.surface.get_height()