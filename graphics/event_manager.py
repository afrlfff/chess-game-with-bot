# event_manager.py
"""
    This module contains the EventManager class, which provides a centralized 
    way to handle and manage Pygame events in a game application.

    Use 'update_frame()' on every game frame.
"""


import pygame

class EventManager:
    Event = pygame.event.Event # Just varaible type to use

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
            cls._events = pygame.event.get()
            cls._frame_updated = True
        return cls._events 
    
    @classmethod
    def update_frame(cls):
        cls._frame_updated = False