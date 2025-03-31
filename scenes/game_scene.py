# game_scene.py

from .base_scene import BaseScene

from graphics import SurfaceManager
from graphics.font import RussoOneRegular
from objects import ChessBoard
from constants import SCREEN_SIZE


class GameScene(BaseScene):
    def __init__(self):
        self.updated = True

        super().__init__()

    @staticmethod
    def get_name():
        return "game"

    def handle_events(self):
        pass

    def initialize_objects(self):
        """
            game_text_1 = SurfaceManager.create_text_surface(
                "Game will be",
                (255, 255, 255),
                RussoOneRegular(50),
                False
            )
            game_text_2 = SurfaceManager.create_text_surface(
                "here soon ...",
                (255, 255, 255),
                RussoOneRegular(50),
                False
            )

            self.game_text = SurfaceManager.create_surface(
                (max(game_text_1.get_width(), game_text_2.get_width()), game_text_1.get_height() * 2),
                True
            )
            self.game_text.blit(game_text_1, (0, 0))
            self.game_text.blit(game_text_2, (0, game_text_1.get_height()))

            self.game_text_pos = (
                (self.screen.get_width() - self.game_text.get_width()) // 2, 
                self.screen.get_height() * 0.2
            )
        """
        self.chess_board = ChessBoard(
            (int(SCREEN_SIZE[0] * 0.75), int(SCREEN_SIZE[1] * 0.75)),
            (int(SCREEN_SIZE[0] * 0.125), int(SCREEN_SIZE[1] * 0.125))
        )


    def update(self):
        self.updated = True
    
    def render(self):
        if not self.updated:
            pass
        
        self.screen.fill((59, 59, 59))
        self.chess_board.render(self.screen)
        #self.screen.blit(self.game_text, self.game_text_pos)

        self.updated = False

