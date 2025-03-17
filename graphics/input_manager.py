# input_manager.py
"""
    Contains class InputManager, made to receive data from input devices.
    
    Uses caching for already calculated data in the current frame, 
    so call ImageManager.update_frame() on every frame  
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