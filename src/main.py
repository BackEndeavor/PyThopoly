import arcade
from src import constants


class PyThopoly(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title, fullscreen=False):
        super().__init__(width, height, title, fullscreen)

        arcade.set_background_color(constants.BACKGROUND_COLOR)

    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        pass

    def on_draw(self):
        """
        Render the screen.
        """
        self.clear()

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
        """
        Called whenever the mouse moves.
        """
        pass

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
