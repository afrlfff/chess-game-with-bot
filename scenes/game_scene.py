# game_scene.py

from .base_scene import BaseScene


class GameScene(BaseScene):
    def __init__(self):
        self.updated = True

    def handle_events(self, events):
        pass

    def initialize_objects(self):
        pass

    def update(self):
        self.updated = True
    
    def render(self):
        if not self.updated:
            pass
        
        # code here ...
        self.updated = False

