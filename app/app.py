# app.py

import pygame
from constants import SCREEN_SIZE
from scenes import MainMenu


class App:
    def __init__(self):
        pygame.init()
        
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.clock = pygame.time.Clock()

        self.scenes = {}
        self.initialize_scenes()
        self.current_scene = self.scenes["menu"]

    def initialize_scenes(self):
        self.scenes["menu"] = MainMenu(self)

    def change_scene(self, scene_name):
        self.current_scene = self.scenes[scene_name]

    def run(self):
        running = True
        while running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    running = False

            # self.current_scene.handle_events(events)
            # self.current_scene.update()
            # self.current_scene.render(self.screen)

            #pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()