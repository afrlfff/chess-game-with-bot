# chess_board.py

from .game_object import GameObject
from .chess_grid import ChessGrid
from .chess_piece import ChessPiece
from graphics import SurfaceManager, Surface
from constants import CHESS_BOARD


class ChessBoard(GameObject):
    def __init__(self, size, pos):
        super().__init__(size, pos)

    def initialize_board(self):
        self.board_surface = SurfaceManager.copy_surface_with_resize(
            SurfaceManager.create_surface_from_image(CHESS_BOARD), 
            self.size
        )
    
    def initialize_grid(self):
        self.grid = ChessGrid(
            (int(self.size[0] * 0.9), int(self.size[1] * 0.9)), 
            (self.pos[0] + int(self.size[0] * 0.05), self.pos[1] + int(self.size[1] * 0.05))
        )

    def initialize_pieces(self):
        self.pieces = [None for _ in range(32)]
        for i in range(8):
            self.pieces[8 + i] = ChessPiece(
                self.grid.get_cell(1, i).get_size(),
                self.grid.get_cell(1, i).get_pos(),
                0, 'p'
            )
            self.pieces[16 + i] = ChessPiece(
                self.grid.get_cell(6, i).get_size(),
                self.grid.get_cell(6, i).get_pos(),
                1, 'p'
            )
        
        for i, type in enumerate(['R', 'N', 'B']):
            self.pieces[i] = ChessPiece(
                self.grid.get_cell(0, i).get_size(),
                self.grid.get_cell(0, i).get_pos(),
                0, type
            )
            self.pieces[7 - i] = ChessPiece(
                self.grid.get_cell(0, 7 - i).get_size(),
                self.grid.get_cell(0, 7 - i).get_pos(),
                0, type
            )
            self.pieces[24 + i] = ChessPiece(
                self.grid.get_cell(7, i).get_size(),
                self.grid.get_cell(7, i).get_pos(),
                1, type
            )
            self.pieces[31 - i] = ChessPiece(
                self.grid.get_cell(7, 7 - i).get_size(),
                self.grid.get_cell(7, 7 - i).get_pos(),
                1, type
            )

        for i, type in enumerate(['K', 'Q']):
            self.pieces[3 + i] = ChessPiece(
                self.grid.get_cell(0, 3 + i).get_size(),
                self.grid.get_cell(0, 3 + i).get_pos(),
                0, type
            )
            self.pieces[24 + 3 + i] = ChessPiece(
                self.grid.get_cell(7, 3 + i).get_size(),
                self.grid.get_cell(7, 3 + i).get_pos(),
                1, type
            )

    def create(self):
        self.initialize_board()
        self.initialize_grid()
        self.initialize_pieces()
        return None

    def get_piece(self, type, color) -> ChessPiece:
        pass

    def handle_event(self, event):
        pass
    
    def update(self):
        pass
    
    def render(self, screen: Surface):
        screen.blit(self.board_surface, self.pos)
        self.grid.render(screen)

        k = 1
        for piece in self.pieces:
            if piece is not None:
                piece.render(screen)
                k += 1