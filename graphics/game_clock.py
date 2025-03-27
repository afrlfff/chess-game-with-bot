# game_clock.py

"""
    This module contains the GameClock class, which is designed to manage 
    the frame rate (FPS) in a game loop.
"""

import pygame

class GameClock:
    def __init__(self, fps=60):
        self.fps = fps
        self.clock = pygame.time.Clock()

    def set_fps(self, fps):
        self.fps = fps

    def tick(self):
        return self.clock.tick(self.fps)