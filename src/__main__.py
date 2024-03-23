import arcade
from arcade.gui import UIManager

from src import constants
from src.constants import DICE_CLASS
from src.entity import board, dice
from src.entity.player import Player
from src.gui.popup.board_popup import ThrowDicePopup


class PyThopoly(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title, fullscreen=False):
        super().__init__(width, height, title, fullscreen)

        arcade.set_background_color(constants.BACKGROUND_COLOR)

        self.ui_manager = None

        self.board = None
        self.player = None
        self.first_dice = None
        self.second_dice = None

        self.throw_dice_popup = None
        self.buy_home_popup = None

    def setup(self):
        self.ui_manager = UIManager()
        self.ui_manager.enable()

        self.board = board.Board("../assets/tilemaps/monopoly.json", self.width, self.height)
        self.player = Player(board=self.board, radius=20)
        self.first_dice = dice.Dice("../assets/images/dices/", "../assets/images/animated_dices/", self.board.find_position(DICE_CLASS, "1"))
        self.second_dice = dice.Dice("../assets/images/dices/", "../assets/images/animated_dices/", self.board.find_position(DICE_CLASS, "2"))

        self.throw_dice_popup = ThrowDicePopup(self.ui_manager, self.board, self.throw_dice)

        self.throw_dice_popup.show()
        self.first_dice.dice_callback = self.dice_fall

    def on_draw(self):
        """
        Render the screen.
        """
        self.clear()
        self.ui_manager.draw()
        self.board.draw()
        self.player.draw()
        self.first_dice.draw()
        self.second_dice.draw()

    def on_update(self, delta_time):
        self.first_dice.update(delta_time)
        self.second_dice.update(delta_time)
        self.player.update()

    def dice_fall(self):
        self.player.next_step(self.first_dice.current_number() + self.second_dice.current_number())
        self.throw_dice_popup.show()

    def throw_dice(self):
        self.first_dice.select_random_dice()
        self.second_dice.select_random_dice()

    def on_key_release(self, key, key_modifiers):
        pass


def main():
    """ Main function """
    game = PyThopoly(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE, constants.FULLSCREEN)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
