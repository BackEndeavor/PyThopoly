import arcade
from src import constants
from src.entity import board


class PyThopoly(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title, fullscreen=False):
        super().__init__(width, height, title, fullscreen)

        arcade.set_background_color(constants.BACKGROUND_COLOR)

        self.board = None


    def setup(self):
        tiles = [board.BoardTile(75, arcade.color.CARDINAL, "Test") for _ in range(40)]
        self.board = board.Board(self.width / 2, self.height / 2, tiles)

    def on_draw(self):
        """
        Render the screen.
        """
        self.clear()
        self.board.draw()

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        pass

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.
        """
        pass

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """ User moves mouse """

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass


def main():
    """ Main function """
    game = PyThopoly(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE, constants.FULLSCREEN)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
