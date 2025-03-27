# label_button.py

from graphics import EventManager, InputManager, SurfaceManager, Surface
from graphics.font import FontBase
from .ui_object import UIObject

class LabelButton(UIObject):
    def __init__(self, pos, size, color, font: FontBase, text="", text_color=(0, 0, 0)):        
        super().__init__(pos, size)
        self.color = color
        self.text_surface = SurfaceManager.create_text_surface(text, text_color, font, False)
        self.text_pos = (
            self.pos[0] + (self.size[0] - self.text_surface.get_width()) // 2, 
            self.pos[1] + (self.size[1] - self.text_surface.get_height()) // 2
        )
        
        self.main_pos = pos
        self.main_size = size
        self.main_color = color
        self.main_text_pos = self.text_pos
        self.main_text_surface = self.text_surface

        self.color_on_hover = (
            int(color[0] * 0.8),
            int(color[1] * 0.8),
            int(color[2] * 0.8)
        )
        self.size_on_click = (size[0] * 0.85, size[1] * 0.85)
        self.pos_on_click = (
            pos[0] + (size[0] - self.size_on_click[0]) // 2, 
            pos[1] + (size[1] - self.size_on_click[1]) // 2
        )
        self.text_surface_on_click = SurfaceManager.create_text_surface(
            text, text_color, font.with_size(int(font.size * 0.85)), False
        )
        self.text_pos_on_click = (
            self.main_text_pos[0] + (self.main_text_surface.get_width() - self.text_surface_on_click.get_width()) // 2, 
            self.main_text_pos[1] + (self.main_text_surface.get_height() - self.text_surface_on_click.get_height()) // 2
        )

    def is_hovered(self, mouse_pos):
        return (self.pos[0] <= mouse_pos[0] <= self.pos[0] + self.size[0]) \
            and (self.pos[1] <= mouse_pos[1] <= self.pos[1] + self.size[1])

    def on_hover(self):
        self.color = self.color_on_hover

    def click(self):
        self.size = self.size_on_click
        self.pos = self.pos_on_click
        self.text_surface = self.text_surface_on_click
        self.text_pos = self.text_pos_on_click

    def release(self):
        self.size = self.main_size
        self.pos = self.main_pos
        self.text_surface = self.main_text_surface
        self.text_pos = self.main_text_pos

    def handle_event(self, event: EventManager.Event):
        if event.type == EventManager.MOUSEBUTTONDOWN:
            if self.is_hovered(InputManager.get_mouse_pos()):
                self.click()

        elif event.type == EventManager.MOUSEBUTTONUP:
            self.release()

    def update(self):
        if self.is_hovered(InputManager.get_mouse_pos()):
            self.on_hover()
        else:
            self.color = self.main_color

    def render(self, surface: Surface):
        surface.draw_rect(self.color, (*self.pos, *self.size))        
        surface.blit(self.text_surface, self.text_pos)