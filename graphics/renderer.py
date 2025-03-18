# renderer.py
"""
    Defines base methods od screen drawing
"""

import pygame
from typing import Optional, Union, Tuple
from .surface_manager import Surface


class Renderer:
    def __init__(self, surface: Surface):
        self.surface = surface

    def blit(self,
        source: Surface,
        dest: Union[Tuple[int, int], pygame.rect.RectType],
        area: Optional[pygame.rect.RectType] = None
    ):
        self.surface.blit(source, dest, area)

    def fill(self, color: Union[Tuple[int, int, int], Tuple[int, int, int, int]]):
        """
            Fills the screen by a given color.
            :param color: tuple (R, G, B) / (R, G, B, A).
        """
        self.surface.fill(color)
    
    def draw_rect(self, color, rect, width=0):
        """
            Draws a rectangle.
            :param color: tuple (R, G, B)
            :param rect: tuple (x, y, width, height)
            :param width: int.
        """
        pygame.draw.rect(self.surface, color, rect, width)
    
    def draw_circle(self, color, center, radius, width=0):
        """
            Draws a circle.
            :param color: tuple (R, G, B).
            :param center: tuple (x, y).
            :param radius: int.
            :param width: int.
        """
        pygame.draw.circle(self.surface, color, center, radius, width)
    
    def draw_image(self, image, pos):
        """
            Draws an image on a given position
        """
        self.surface.blit(image, pos)
    

