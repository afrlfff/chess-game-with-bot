# scene_manager.py

from .main_menu_scene import MainMenuScene
from .game_scene import GameScene
from .base_scene import BaseScene

class SceneManager:
    _scenes = {}
    _current_scene = ""

    @classmethod
    def load_scenes(cls):
        cls._scenes = {
            "menu": MainMenuScene(),
            "game": GameScene()
        }
        cls._current_scene = cls._scenes['menu']
    
    @classmethod
    def change_scene(cls, scene_name):
        if scene_name not in cls._scenes.keys():
            raise ValueError(f"Unknown scene name: {scene_name}")
        cls._current_scene = cls._scenes[scene_name]
    
    @classmethod
    def get_current_scene(cls) -> BaseScene:
        return cls._current_scene
