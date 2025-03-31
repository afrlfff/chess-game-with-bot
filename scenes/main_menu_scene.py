# main_menu_scene.py

from .base_scene import BaseScene
from .scene_manager import SceneManager
from graphics import EventManager, SurfaceManager
from graphics.font import RussoOneRegular
from ui import LabelButton
from constants import SCREEN_SIZE


class MainMenuScene(BaseScene):
    @staticmethod
    def get_name():
        return "main menu"
    
    def __init__(self):
        self.background_color = (0, 0, 0)
        self.updated = True

        self.scene_manager = SceneManager()

        super().__init__()

    def initialize_objects(self):
        self.title_surface = SurfaceManager.create_text_surface(
            text="Chess game", 
            color=(255, 255, 255), 
            font=RussoOneRegular(75),
            antialias=False
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
                text_color= (0, 0, 0),
                callback= lambda: self.scene_manager.set_scene("game")
            ),
            LabelButton(
                pos= (SCREEN_SIZE[0] // 2 - 125, SCREEN_SIZE[1] // 2 - 37 + 75 + 37),
                size= (250, 75),
                color= (255, 255, 255),
                font= RussoOneRegular(40),
                text= "Выход",
                text_color= (0, 0, 0),
                callback= lambda: self.scene_manager.app_quit_callback()
            )
        ]

    def handle_events(self):
        for event in EventManager.get_events():
            for button in self.buttons:
                button.handle_event(event)

    def update(self):
        self.updated = True # think about how to optimize class using 'self.updated'

        for button in self.buttons:
            button.update()
    
    def render(self):
        if not self.updated:
            pass
        
        self.screen.fill(self.background_color)
        self.screen.blit(self.title_surface, self.title_pos)
        for button in self.buttons:
            button.render(self.screen)

        self.updated = False