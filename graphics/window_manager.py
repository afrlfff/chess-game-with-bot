# window_manager.py

import pygame

class WindowManager:
    def __init__(self, size, title="Pygame Window"):
        self.size = size
        self.title = title
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption(title)

    def render(self):
        pygame.display.flip()
    
    def get_size(self):
        return self.screen.get_size()
