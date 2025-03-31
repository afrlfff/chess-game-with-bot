from pathlib import Path


ROOT_PATH = Path(__file__).parent
IMG_PATH = ROOT_PATH / 'resources' / 'img'
FONTS_PATH = ROOT_PATH / 'resources' / 'fonts'
GRAPHICS_PATH = ROOT_PATH / 'graphics'


SCREEN_SIZE = (600, 600)
FPS = 60

RUSSO_ONE_REGULAR = 'RussoOne-Regular.ttf'



CHESS_BOARD = IMG_PATH / 'chess-boards' / 'chess-board-main.jpg'

CHESS_GRID_CELL_WHITE = IMG_PATH / 'chess-grids' / 'chess-grid-cell-white.png'
CHESS_GRID_CELL_BLACK = IMG_PATH / 'chess-grids' / 'chess-grid-cell-black.png'
CHESS_GRID_CELL_GREEB = IMG_PATH / 'chess-grids' / 'chess-grid-cell-green.png'
CHESS_GRID_CELL_RED = IMG_PATH / 'chess-grids' / 'chess-grid-cell-red.png'

CHESS_PIECES_PATH = IMG_PATH / 'chess-pieces'
CHESS_PIECES = {
    'white_pawn': CHESS_PIECES_PATH / 'pawn-white.png',
    'black_pawn': CHESS_PIECES_PATH / 'pawn-black.png',
    'white_rock': CHESS_PIECES_PATH / 'rock-white.png',
    'black_rock': CHESS_PIECES_PATH / 'rock-black.png',
    'white_knight': CHESS_PIECES_PATH / 'knight-white.png',
    'black_knight': CHESS_PIECES_PATH / 'knight-black.png',
    'white_bishop': CHESS_PIECES_PATH / 'bishop-white.png',
    'black_bishop': CHESS_PIECES_PATH / 'bishop-black.png',
    'white_king': CHESS_PIECES_PATH / 'king-white.png',
    'black_king': CHESS_PIECES_PATH / 'king-black.png',
    'white_queen': CHESS_PIECES_PATH / 'queen-white.png',
    'black_queen': CHESS_PIECES_PATH / 'queen-black.png'
}