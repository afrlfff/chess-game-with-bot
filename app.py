# app.py

from constants import SCREEN_SIZE, FPS
from graphics import WindowManager, GameClock, EventManager, InputManager
from scenes import SceneManager, MainMenuScene, GameScene
from utils import singleton


@singleton
class App:
    def __init__(self):
        WindowManager.init()
        WindowManager.create_window(size=SCREEN_SIZE, title="Chess game")
        self.clock = GameClock(FPS)
        self.running = True

        self.scene_manager = SceneManager(self.quit)
        self.scene_manager.register_scene(MainMenuScene)
        self.scene_manager.register_scene(GameScene)
        self.scene_manager.set_scene(GameScene.get_name())

    def quit(self):
        self.running = False

    def run(self):
        while self.running:
            events = EventManager.get_events()
            for event in events:
                if event.type == EventManager.QUIT:
                    self.running = False
 
            InputManager.update_frame()
            EventManager.update_frame()

            self.scene_manager.handle_events()
            self.scene_manager.update()
            self.scene_manager.render()

            WindowManager.render()
            self.clock.tick()

        WindowManager.quit()