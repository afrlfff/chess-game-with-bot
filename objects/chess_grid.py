# chess_grid.py

from .game_object import GameObject
from .chess_grid_cell import ChessGridCell

from graphics import Surface


class ChessGrid(GameObject):
    def __init__(self, size, pos):
        if size[0] != size[1]:
            raise ValueError(f"Size should be square: (x, x)")

        super().__init__(size, pos)

        self.cells = self.initialize_cells()

    def create(self):
        return None

    def initialize_cells(self):
        cells = [[None for _ in range(8)] for _ in range(8)]

        current_pos = [self.pos[0], self.pos[1]]
        light = True
        for i in range(8):
            for j in range(8):
                cell_size = (self.size[0] // 8, self.size[0] // 8)
                if (i < self.size[0] % 8) and (j < self.size[0] % 8):
                    cell_size = (self.size[0] // 8 + 1, self.size[0] // 8 + 1)
                elif (i < self.size[0] % 8): 
                    cell_size = (self.size[0] // 8, self.size[0] // 8 + 1)
                elif (j < self.size[0] % 8): 
                    cell_size = (self.size[0] // 8 + 1, self.size[0] // 8)

                cells[i][j] = ChessGridCell(cell_size, (current_pos[0], current_pos[1]), light)
                light = not(light)
                current_pos[0] += cell_size[0]
            
            light = not(light)
            current_pos[0] = self.pos[0]
            current_pos[1] += cell_size[1]
        
        return cells

    def get_cell(self, row, col) -> ChessGridCell:
        return self.cells[row][col]

    def handle_event(self, event):
        pass

    def update(self):
        pass

    def render(self, screen: Surface):
        for row in self.cells:
            for cell in row:
                cell.render(screen)
