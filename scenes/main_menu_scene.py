# main_menu_scene.py

from .base_scene import BaseScene
from graphics import EventManager, Renderer, SurfaceManager
from graphics.font import RussoOneRegular
from ui import LabelButton
from constants import SCREEN_SIZE


class MainMenuScene(BaseScene):
    def __init__(self, app):
        self.app = app
        self.updated = True
        self.background_color = (0, 0, 0)
        self.renderer = Renderer(self.app.window.screen)
        self.buttons = []
        self.title_surface = None
        self.title_pos = (-1, -1)

        self.initialize_scene()

    def initialize_scene(self):
        self.title_surface = SurfaceManager.create_text_surface(
            "Chess game", 
            (255, 255, 255), 
            RussoOneRegular(75),
            False
        )
        self.title_pos = (
            (SCREEN_SIZE[0] - self.title_surface.get_width()) // 2,
            int(SCREEN_SIZE[1] * 0.15)
        )
        self.buttons = [
            LabelButton(
                pos= (SCREEN_SIZE[0] // 2 - 125, SCREEN_SIZE[1] // 2 - 37),
                size= (250, 75),
                color= (255, 255, 255),
                font= RussoOneRegular(40),
                text= "Играть",
                text_color= (0, 0, 0)
            ),
            LabelButton(
                pos= (SCREEN_SIZE[0] // 2 - 125, SCREEN_SIZE[1] // 2 - 37 + 75 + 37),
                size= (250, 75),
                color= (255, 255, 255),
                font= RussoOneRegular(40),
                text= "Выход",
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
        self.renderer.blit(self.title_surface, self.title_pos)
        for button in self.buttons:
            button.render(self.renderer)

        self.updated = False