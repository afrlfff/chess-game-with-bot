# main_menu_scene.py

from .base_scene import BaseScene
from graphics import EventManager, Renderer, FontManager
from ui import LabelButton
from constants import SCREEN_SIZE, RUSSO_ONE_REGULAR


class MainMenuScene(BaseScene):
    def __init__(self, app):
        self.app = app
        self.updated = True
        self.background_color = (0, 0, 0)
        self.renderer = Renderer(self.app.window.screen)
        self.buttons = []
        self.fonts = {}

        self.initialize_scene()

    def initialize_scene(self):
        self.fonts = {
            "title": FontManager.get_font(font_filename=RUSSO_ONE_REGULAR, font_size=50),
            "button": FontManager.get_font(font_filename=RUSSO_ONE_REGULAR, font_size=40)
        }
        self.buttons = [
            LabelButton(
                pos= (SCREEN_SIZE[0] // 2 - 125, SCREEN_SIZE[1] // 2 - 37),
                size= (250, 75),
                color= (255, 255, 255),
                font= self.fonts["button"],
                text= "Играть",
                text_color= (0, 0, 0)
            )
        ]

    def handle_events(self):
        for event in EventManager.get_events():
            for button in self.buttons:
                button.handle_event(event)

    def update(self):
        self.updated = True

        for button in self.buttons:
            button.update()
    
    def render(self):
        if not self.updated:
            pass
        
        self.renderer.fill(self.background_color)
        for button in self.buttons:
            button.render(self.renderer)

        self.updated = False