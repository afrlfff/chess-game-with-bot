# surface_manager.py
"""
    This module provides the `SurfaceManager` class, which offers utility methods 
    for creating and managing Pygame surfaces in various ways.
"""

import pygame
import numpy as np
from pathlib import Path
from pygame import surfarray
from typing import Tuple
from .font import FontBase
from .surface import Surface
from utils import resize_image

class SurfaceManager:
    @staticmethod
    def create_surface(size: Tuple[int, int], is_alpha: bool = False) -> Surface:
        if is_alpha:
            return Surface(pygame.Surface(size=size, flags=pygame.SRCALPHA))
        else:
            return Surface(pygame.Surface(size=size))
        
    @staticmethod
    def create_surface_from_pixels(pixels: np.ndarray) -> Surface:
        if pixels.shape[2] == 3:
            return Surface(surfarray.make_surface(pixels))
        elif pixels.shape[2] == 4:
            # transpose because numpy ans pygame interpret pixels in different ways
            pixels_transposed = np.transpose(pixels, axes=(1, 0, 2))
            return Surface(pygame.image.frombuffer(
                pixels_transposed.tobytes(), pixels.shape[:2], 'RGBA'
            ))
        else:
            raise ValueError("Pixel's dimensions should be either (N, M, 3) or (N, M, 4).")

    @staticmethod
    def create_surface_from_image(filepath: Path) -> Surface:
        if filepath.suffix == '.jpg':
            return Surface(pygame.image.load(filepath))
        if filepath.suffix == '.png':
            return Surface(pygame.image.load(filepath).convert_alpha())

    @staticmethod
    def create_text_surface(text: str, color, font: FontBase, antialias=True, background=None) -> Surface:
        return font.to_surface(text, antialias, color, background)

    @staticmethod
    def copy_surface_with_resize(source_surface: Surface, new_size: Tuple[int, int]):
        new_pixels = resize_image(source_surface.get_pixels(), new_size, interpolation_radius=1)
        return SurfaceManager.create_surface_from_pixels(new_pixels)
