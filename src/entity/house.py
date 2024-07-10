import arcade

from src.constants import COLOR_TILE_CLASS


class House:
    def __init__(self, index, board_map):
        self.index = index
        self.board_map = board_map
        self.level = 1
        self.sold = False
        self.owner = None

    def draw(self):
        if self.owner is None:
            return
        rectangle_x, rectangle_y, width, height = self.board_map.find_position(COLOR_TILE_CLASS, str(self.index))
        arcade.draw_rectangle_filled(rectangle_x + width / 2, rectangle_y - height / 2, width, height, self.owner.color)
