# base_scene.py

from abc import ABC, abstractmethod

class BaseScene(ABC):
    @abstractmethod
    def handle_events(self):
        raise ValueError("Scene classes should define hanlde_events method")

    @abstractmethod
    def update(self):
        raise ValueError("Scene classes should define update method")

    @abstractmethod
    def render(self):
        raise ValueError("Scene classes should define render method")