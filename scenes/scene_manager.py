# scene_manager.py

from .main_menu_scene import MainMenuScene
from .game_scene import GameScene

class SceneManager:
    @staticmethod
    def load_scenes(app):
        return {
            "menu": MainMenuScene(app),
            "game": GameScene(app)
        }