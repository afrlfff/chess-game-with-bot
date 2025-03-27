# base_scene.py

from abc import ABC, abstractmethod
from graphics import WindowManager


class BaseScene(ABC):
    def __init__(self):
        self.screen = WindowManager.get_screen()

        self.initialize_objects()

    @abstractmethod
    def handle_events(self):
        raise ValueError("Scene classes should define hanlde_events method")

    @abstractmethod
    def initialize_objects(self):
        raise ValueError("Scene classes should define initialize_objects method")

    @abstractmethod
    def update(self):
        raise ValueError("Scene classes should define update method")

    @abstractmethod
    def render(self):
        raise ValueError("Scene classes should define render method")