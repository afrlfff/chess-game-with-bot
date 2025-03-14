# base_scene.py

from abc import ABC, abstractmethod

class BaseScene(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def render(self):
        pass