# window_manager.py

"""
    This module provides the `WindowManager` class, which simplifies the creation 
    and management of Pygame windows and display-related operations.
"""

import pygame
from .surface import Surface

class WindowManager:
    SRCALPHA = pygame.SRCALPHA  # Enables alpha channel (transparency) support for the surface.
    DOUBLEBUF = pygame.DOUBLEBUF  # Enables double buffering to prevent flickering during rendering.
    RESIZABLE = pygame.RESIZABLE  # Allows the window to be resized during runtime.
    FULLSCREEN = pygame.FULLSCREEN  # Switches the window to fullscreen mode.
    OPENGL = pygame.OPENGL  # Creates a surface compatible with OpenGL for graphics rendering.
    NOFRAME = pygame.NOFRAME  # Creates a borderless window without a title bar or interface elements.

    _screen = None

    @staticmethod
    def init():
        return pygame.init()

    @staticmethod
    def quit():
        pygame.quit()

    @classmethod
    def create_window(cls, size, flags=0, title="Pygame Window"):
        pygame.display.set_caption(title)
        cls._screen = Surface(pygame.display.set_mode(size, flags))

    @classmethod
    def get_screen(cls) -> Surface:
        return cls._screen

    @staticmethod
    def render():
        pygame.display.flip()
    
    @staticmethod
    def get_title():
        return pygame.display.get_caption()[0]
