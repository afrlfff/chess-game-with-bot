# game_clock.py

import pygame
from constants import FPS

class GameClock:
    def __init__(self):
        self.clock = pygame.time.Clock()

    def tick(self):
        return self.clock.tick(FPS)