# event_manager.py
"""
    Contains Event and EventManager classes.
    
    Event class defines event objects containinig event type
    
    EventManager class defines get_event() method to get all the available events.
    Also uses caching so call EventManager.updae_frame() method on every frame.
"""


import pygame


class Event:
    def __init__(self, event: pygame.event.Event):
        self.event = event
        self.type = event.type

class EventManager:
    QUIT = pygame.QUIT
    KEYDOWN = pygame.KEYDOWN
    KEYUP = pygame.KEYUP
    MOUSEBUTTONDOWN = pygame.MOUSEBUTTONDOWN
    MOUSEBUTTONUP = pygame.MOUSEBUTTONUP
    MOUSEMOTION = pygame.MOUSEMOTION
    WINDOWRESIZED = pygame.WINDOWRESIZED
    WINDOWMOVED = pygame.WINDOWMOVED
    WINDOWFOCUSGAINED = pygame.WINDOWFOCUSGAINED
    WINDOWFOCUSLOST = pygame.WINDOWFOCUSLOST

    _frame_updated = False
    _events = []

    @classmethod
    def get_events(cls):
        if not cls._frame_updated:
            cls._events = [Event(event) for event in pygame.event.get()]
            cls._frame_updated = True
        return cls._events 
    
    @classmethod
    def update_frame(cls):
        cls._frame_updated = False