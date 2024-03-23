import arcade
from arcade.gui import UIManager

from src import constants
from src.constants import DICE_CLASS
from src.entity import dice
from src.entity.board import Board
from src.entity.board_map import BoardTileMap
from src.entity.player import Player
from src.gui.popup.board_popup import ThrowDicePopup, BuyHousePopup


class PyThopoly(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title, fullscreen=False):
        super().__init__(width, height, title, fullscreen)

        arcade.set_background_color(constants.BACKGROUND_COLOR)

        self.ui_manager = None

        self.board_map = None
        self.board = None
        self.player = None
        self.first_dice = None
        self.second_dice = None

        self.throw_dice_popup = None
        self.buy_house_popup = None

    def setup(self):
        self.ui_manager = UIManager()
        self.ui_manager.enable()

        self.board_map = BoardTileMap("../assets/tilemaps/monopoly.json", self.width, self.height)
        self.player = Player(board_map=self.board_map, radius=20)
        self.first_dice = dice.Dice("../assets/images/dices/", "../assets/images/animated_dices/", self.board_map.find_position(DICE_CLASS, "1"))
        self.second_dice = dice.Dice("../assets/images/dices/", "../assets/images/animated_dices/", self.board_map.find_position(DICE_CLASS, "2"))

        self.throw_dice_popup = ThrowDicePopup(self.ui_manager, self.board_map)

        self.board = Board(self)
        self.board.start_game()

    def on_draw(self):
        """
        Render the screen.
        """
        self.clear()
        self.ui_manager.draw()
        self.board_map.draw()
        self.player.draw()
        self.first_dice.draw()
        self.second_dice.draw()

    def on_update(self, delta_time):
        self.first_dice.update(delta_time)
        self.second_dice.update(delta_time)
        self.player.update()

    def on_key_release(self, key, key_modifiers):
        pass


def main():
    """ Main function """
    game = PyThopoly(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE, constants.FULLSCREEN)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
