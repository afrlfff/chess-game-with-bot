# game_initializer.py

import pygame

class GameInitializer:
    @staticmethod
    def init():
        pygame.init()

    @staticmethod
    def quit():
        pygame.quit()