# game_scene.py

from .base_scene import BaseScene


class GameScene(BaseScene):
    def __init__(self):
        self.updated = True

    def update(self):
        self.updated = True
    
    def render(self):
        if self.updated:
            # ...
            pass
        
        self.updated = False



