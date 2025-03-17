# ui_object.py

from abc import ABC, abstractmethod

class UIObject(ABC):
    @abstractmethod
    def __init__(self, pos, size):
        self.pos = pos
        self.size = size

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
    def render(self):
        pass