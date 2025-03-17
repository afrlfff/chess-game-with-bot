# game_scene.py

from .base_scene import BaseScene


class GameScene(BaseScene):
    def __init__(self, app):
        self.app = app
        self.updated = True

    def handle_events(self, events):
        pass

    def update(self):
        self.updated = True
    
    def render(self):
        if not self.updated:
            pass
        
        # code here ...
        self.updated = False

