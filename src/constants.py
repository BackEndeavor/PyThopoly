import datetime

import arcade

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 1024
SCREEN_TITLE = "PyThopoly"
FULLSCREEN = True
BACKGROUND_COLOR = arcade.color.CELADON_GREEN
UPDATES_PER_FRAME = 5

PLAYER_PATH_CLASS = 'player_path'
DICE_CLASS = 'dice'
COLOR_TILE_CLASS = 'color_tile'
UI_POPUP_CLASS = 'ui_popup'

MOVE_TRANSITION_SPEED = 0.05
DICE_ROLL_DURATION = datetime.timedelta(seconds=1)
