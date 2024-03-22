import arcade

from src import constants
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
        self.dice = None

    def setup(self):
        self.board = board.Board("../assets/tilemaps/monopoly.json", self.width, self.height)
        self.player = Player(board=self.board, radius=20)
        self.dice = dice.Dice("../assets/images/dices/","../assets/images/animated_dices/", self.board.center())

    def on_draw(self):
        """
        Render the screen.
        """
        self.clear()
        self.board.draw()
        self.player.draw()
        self.dice.draw()

    def on_update(self, delta_time):
        self.dice.update(delta_time)

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.D:
            self.player.next_step(1)
        if key == arcade.key.R:
            self.dice.select_random_dice()

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
