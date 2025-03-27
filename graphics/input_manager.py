# input_manager.py
"""
    This module provides the `InputManager` class, which is designed to manage 
    and retrieve user input data in a game application.

    It supports efficient access to input data by caching it on a per-frame basis 
    and updating only when necessary.

    Use 'update_frame()' on every game frame.
"""

import pygame

class InputManager:
    _mouse_pos = None
    _frame_updated = False

    @classmethod
    def get_mouse_pos(cls):
        if not cls._frame_updated:
            cls._mouse_pos = pygame.mouse.get_pos()
            cls._frame_updated = True
        return cls._mouse_pos
    
    @classmethod
    def update_frame(cls):
        cls._frame_updated = False