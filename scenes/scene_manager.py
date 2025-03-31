# scene_manager.py

from .base_scene import BaseScene
from utils import singleton


@singleton
class SceneManager:
    def __init__(self, app_quit_callback):
        self._scenes = {}
        self._current_scene = None
        self.app_quit_callback = app_quit_callback

    def register_scene(self, scene_class: BaseScene):
        self._scenes[scene_class.get_name()] = scene_class()

    def set_scene(self, scene_name):
        self._current_scene = self._scenes[scene_name]

    def quit(self):
        self.app_quit_callback()

    def get_current_scene(self) -> BaseScene:
        if self._current_scene is None:
            raise AttributeError("No scene was set. Call 'set_scene' method before")
        return self._current_scene

    def handle_events(self):
        if self._current_scene is None:
            raise AttributeError("No scene was set. Call 'set_scene' method before")
        self._current_scene.handle_events()

    def update(self):
        if self._current_scene is None:
            raise AttributeError("No scene was set. Call 'set_scene' method before")
        self._current_scene.update()

    def render(self):
        if self._current_scene is None:
            raise AttributeError("No scene was set. Call 'set_scene' method before")
        self._current_scene.render()