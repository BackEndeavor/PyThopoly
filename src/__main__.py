import arcade

from src import constants
from src.constants import DICE_CLASS
from src.entity import board, dice
from src.entity.player import Player


class PyThopoly(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title, fullscreen=False):
        super().__init__(width, height, title, fullscreen)

        arcade.set_background_color(constants.BACKGROUND_COLOR)

        self.board = None
        self.player = None
        self.first_dice = None
        self.second_dice = None

    def setup(self):
        self.board = board.Board("../assets/tilemaps/monopoly.json", self.width, self.height)
        self.player = Player(board=self.board, radius=20)
        self.first_dice = dice.Dice("../assets/images/dices/", "../assets/images/animated_dices/", self.board.find_position(DICE_CLASS, "1"))
        self.second_dice = dice.Dice("../assets/images/dices/", "../assets/images/animated_dices/", self.board.find_position(DICE_CLASS, "2"))

    def on_draw(self):
        """
        Render the screen.
        """
        self.clear()
        self.board.draw()
        self.player.draw()
        self.first_dice.draw()
        self.second_dice.draw()

    def on_update(self, delta_time):
        self.first_dice.update(delta_time)
        self.second_dice.update(delta_time)
        self.player.update()

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.D:
            self.player.next_step(1)
        if key == arcade.key.R:
            self.first_dice.select_random_dice()
            self.second_dice.select_random_dice()
        if key == arcade.key.B:
            house = self.board.houses.get(str(self.player.position_index))
            if house is not None:
                house.has_owner = True

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass


def main():
    """ Main function """
    game = PyThopoly(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE, constants.FULLSCREEN)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
