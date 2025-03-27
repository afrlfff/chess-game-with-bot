# assets.py

from graphics import SurfaceManager
from constants import IMG_PATH


class Assets:
    chess_piece_surfaces = {}
    chess_board_surfaces = {}

    @classmethod
    def load_assets(cls):
        cls._load_chess_piece_images()
        cls._load_chess_board_images()

    @classmethod
    def _load_chess_piece_images(cls):
        try:
            for filepath in (IMG_PATH / 'chess-pieces').iterdir():
                if filepath.is_file():
                    filename = filepath.stem
                    Assets.chess_piece_surfaces[filename] = SurfaceManager.create_surface_from_image(filepath)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Error while loading chess piece images: {e}")
    
    @classmethod
    def _load_chess_board_images(cls):
        try:
            for filepath in (IMG_PATH / 'chess-boards').iterdir():
                if filepath.is_file():
                    filename = filepath.stem
                    Assets.chess_board_surfaces[filename] = SurfaceManager.create_surface_from_image(filepath)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Error while loading chess board images: {e}")

    