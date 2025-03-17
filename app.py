# app.py

from constants import SCREEN_SIZE
from scenes import SceneManager
from graphics import GameInitializer, GameClock, WindowManager, Event
from assets import Assets


class App:
    def __init__(self):
        GameInitializer.init()
        self.window = WindowManager(SCREEN_SIZE, "Chess game with bot")
        self.clock = GameClock()

        Assets.load_assets()
        self.scenes = SceneManager.load_scenes(self)
        self.current_scene = self.scenes.get("menu") 

    def change_scene(self, scene_name):
        self.current_scene = self.scenes.get_scene(scene_name)

    def run(self):
        running = True
        while running:
            events = Event.get_events()
            for event in events:
                if event.type == Event.QUIT:
                    running = False
 
            self.current_scene.handle_events(events)
            self.current_scene.update()
            self.current_scene.render()

            self.window.render()
            self.clock.tick()

        GameInitializer.quit()