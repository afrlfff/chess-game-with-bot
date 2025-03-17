# event.py

import pygame

class Event:
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

    @staticmethod
    def get_events():
        return [Event(event) for event in pygame.event.get()]
    
    def __init__(self, event: pygame.event.Event):
        self.event = event
        self.type = event.type