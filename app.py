# app.py

from constants import SCREEN_SIZE, FPS
from scenes import SceneManager
from graphics import WindowManager, GameClock, WindowManager, EventManager, InputManager
from assets import Assets


class App:
    def __init__(self):
        WindowManager.init()
        WindowManager.create_window(size=SCREEN_SIZE, title="Chess game")
        self.clock = GameClock(FPS)
        Assets.load_assets()
        SceneManager.load_scenes()

        self.current_scene = SceneManager.get_current_scene()

    def stop(self):
        WindowManager.quit()

    def run(self):
        running = True
        while running:
            events = EventManager.get_events()
            for event in events:
                if event.type == EventManager.QUIT:
                    running = False
 
            InputManager.update_frame()
            EventManager.update_frame()
            self.current_scene = SceneManager.get_current_scene()
            self.current_scene.handle_events()
            self.current_scene.update()
            self.current_scene.render()

            WindowManager.render()
            self.clock.tick()

        WindowManager.quit()