# chess_grid_cell.py

from .game_object import GameObject
from graphics import SurfaceManager, Surface


class ChessGridCell(GameObject):
    def __init__(self, size, pos, light=True):
        self.light = light
        super().__init__(size, pos)

    def create(self):
        surface = SurfaceManager.create_surface(self.size)
        if self.light:
            surface.fill((255, 255, 255))
        else:
            surface.fill((109, 109, 109))
        return surface

    def mark_as_valid(self):
        self.surface.fill((0, 255, 0))

    def mark_as_capture(self):
        self.surface.fill((255, 0, 0))

    def mark_as_threat(self):
        self.surface.fill((255, 0, 0))

    def handle_event(self, event):
        pass

    def update(self):
        pass

    def render(self, screen: Surface):
        screen.blit(self._surface, self.pos)