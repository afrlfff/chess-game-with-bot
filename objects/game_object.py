# game_object.py

from abc import ABC, abstractmethod
from graphics import Surface
from typing import Tuple


class GameObject(ABC):
    def __init__(self, size: Tuple[int, int], pos: Tuple[int, int]):
        self.size = size
        self.pos = pos

        self._surface = self.create()

    def get_surface(self):
        return self._surface

    def get_size(self):
        return self.size

    def get_pos(self):
        return self.pos
    
    def set_pos(self, pos):
        self.pos = pos

    @abstractmethod
    def create(self) -> Surface:
        pass

    @abstractmethod
    def handle_event(self, event):
        pass

    def handle_events(self, events):
        for event in events:
            self.handle_event(event)
    
    @abstractmethod
    def update(self):
        pass
    
    @abstractmethod
    def render(self, screen: Surface):
        pass