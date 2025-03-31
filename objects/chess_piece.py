# chess_grid.py

from .game_object import GameObject

from graphics import Surface, SurfaceManager

from constants import CHESS_PIECES


class ChessPiece(GameObject):
    def __init__(self, size, pos, color, type):
        if (color != 0) and (color != 1):
             raise ValueError(f"Piece color should be either 0 (black) or 1 (white).")

        if type not in 'pRNBKQ':
            raise ValueError(f"Piece type should be one of the 'p', 'R', 'N', 'B', 'K', 'Q'")

        self.color = color
        self.type = type
        super().__init__(size, pos)

    def create(self):
        if self.type == 'p':
            key = 'white_pawn' if (self.color == 1) else 'black_pawn'
        if self.type == 'R':
            key = 'white_rock' if (self.color == 1) else 'black_rock'
        if self.type == 'N':
            key = 'white_knight' if (self.color == 1) else 'black_knight'
        if self.type == 'B':
            key = 'white_bishop' if (self.color == 1) else 'black_bishop'
        if self.type == 'K':
            key = 'white_king' if (self.color == 1) else 'black_king'
        if self.type == 'Q':
            key = 'white_queen' if (self.color == 1) else 'black_queen'

        return SurfaceManager.copy_surface_with_resize(
            SurfaceManager.create_surface_from_image(CHESS_PIECES[key]), 
            self.size
        )

    def handle_event(self, event):
        pass

    def update(self):
        pass

    def render(self, screen: Surface):
        screen.blit(self._surface, self.pos)
