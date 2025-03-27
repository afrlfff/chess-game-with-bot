# surface_manager.py
"""
    This module provides the `SurfaceManager` class, which offers utility methods 
    for creating and managing Pygame surfaces in various ways.
"""

import pygame
import numpy as np
from pygame import surfarray
from typing import Tuple
from .font import FontBase
from .surface import Surface

class SurfaceManager:
    @staticmethod
    def create_surface(size: Tuple[int, int], is_alpha: bool = False) -> Surface:
        if is_alpha:
            return Surface(pygame.Surface(size=size, flags=pygame.SRCALPHA))
        else:
            return Surface(pygame.Surface(size=size))
        
    @staticmethod
    def create_surface_from_pixels(pixels: np.ndarray) -> Surface:
        return Surface(surfarray.make_surface(pixels))

    @staticmethod
    def create_surface_from_image(filepath) -> Surface:
        if filepath.suffix == '.jpg':
            return Surface(pygame.image.load(filepath))
        if filepath.suffix == '.png':
            return Surface(pygame.image.load(filepath).convert_alpha())

    @staticmethod
    def create_text_surface(text: str, color, font: FontBase, antialias=True, background=None) -> Surface:
        return font.to_surface(text, antialias, color, background)