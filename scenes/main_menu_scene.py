# main_menu_scene.py

from .base_scene import BaseScene
from graphics import Event, Renderer
from ui import Button
from constants import SCREEN_SIZE, BTN_FONT_PATH


class MainMenuScene(BaseScene):
    def __init__(self, app):
        self.app = app
        self.updated = True
        self.background_color = (255, 0, 0)
        self.renderers = {}
        self.buttons = []
        self.fonts = {}

        self.initialize_scene()

    def initialize_scene(self):
        self.renderers = {
            "main": Renderer(self.app.window.screen),
            "title": Renderer(Renderer.create_surface(self.app.window.get_size())),
            "buttons": Renderer(Renderer.create_surface(self.app.window.get_size()))
        }
        self.fonts = {
            "button": Renderer.create_font(size=50, path=BTN_FONT_PATH)
        }
        self.buttons = [
            Button(
                renderer= self.renderers["buttons"], 
                pos= (SCREEN_SIZE[0] // 2 - 100, SCREEN_SIZE[1] // 2 - 50),
                size= (100, 50),
                color= (0, 0, 255),
                font= self.fonts["button"],
                text= "Играть",
                text_color= (255, 255, 255)
            )
        ]

    def handle_events(self, events):
        for event in events:
            if event.type == Event.MOUSEBUTTONDOWN:
                pass
            if event.type == Event.MOUSEBUTTONUP:
                pass

    def update(self):
        self.updated = True
    
    def render(self):
        if not self.updated:
            pass
        
        self.renderers['main'].fill(self.background_color)
        for button in self.buttons:
            button.render()

        self.updated = False