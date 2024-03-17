import arcade

from src.misc.position import RectanglePosition, Placement


class Board(RectanglePosition):
    def __init__(self, center_x, center_y, tiles, border_color=arcade.color.BISTRE):
        self.tiles = tiles
        self.tile_size = self.tiles[0].size
        self.tiles_per_edge = int((len(tiles) / 4) - 1)
        self.board_size = self.tiles_per_edge * self.tile_size / 2 + (2 * self.tile_size)  # Edge size + corner size
        super().__init__(center_x, center_y, self.board_size, self.board_size, Placement.CENTER)

        self.center_x = center_x
        self.center_y = center_y
        self.border_color = border_color

        self.corners = list(map(lambda pos: pos.with_size(self.tile_size, self.tile_size), [
            self.with_placement(Placement.LEFT_BOTTOM),
            self.with_placement(Placement.RIGHT_TOP),
            self.with_placement(Placement.RIGHT_BOTTOM),
            self.with_placement(Placement.LEFT_TOP),
        ]))

    def draw(self):
        arcade.draw_rectangle_outline(self.center_x, self.center_y, self.board_size, self.board_size, self.border_color)

        # Drawing corners
        for i in range(4):
            tile = self.tiles[i * int(self.tiles_per_edge)]
            tile.draw(self.corners[i])

        half_tile_size = self.tile_size / 2

        left_top = self.corners[3].copy()
        left_top.resize(half_tile_size, self.tile_size)
        left_top.move(Placement.CENTER)
        left_top.x += half_tile_size
        # Drawing top part of the board
        for i in range(self.tiles_per_edge):
            left_top.x += half_tile_size
            arcade.draw_circle_filled(left_top.x, left_top.y, 4, arcade.color.BABY_BLUE)

        right_top = self.corners[1].copy()
        right_top.resize(self.tile_size, half_tile_size)
        right_top.move(Placement.CENTER)
        right_top.y -= half_tile_size
        # Drawing right part of the board
        for i in range(self.tiles_per_edge):
            right_top.y -= half_tile_size
            arcade.draw_circle_filled(right_top.x, right_top.y, 4, arcade.color.BABY_BLUE)

        right_bottom = self.corners[2].copy()
        right_bottom.resize(half_tile_size, self.tile_size)
        right_bottom.move(Placement.CENTER)
        right_bottom.x -= half_tile_size
        # Drawing bottom part of the board
        for i in range(self.tiles_per_edge):
            right_bottom.x -= half_tile_size
            arcade.draw_circle_filled(right_bottom.x, right_bottom.y, 4, arcade.color.BABY_BLUE)

        left_bottom = self.corners[0].copy()
        left_bottom.resize(self.tile_size, half_tile_size)
        left_bottom.move(Placement.CENTER)
        left_bottom.y += half_tile_size
        # Drawing left part of the board
        for i in range(self.tiles_per_edge):
            left_bottom.y += half_tile_size
            arcade.draw_circle_filled(left_bottom.x, left_bottom.y, 4, arcade.color.BABY_BLUE)




# Height of the "Color" bar for tile
TILE_COLOR_HEIGHT = 1 / 3


class BoardTile:
    def __init__(self, size, color, text, sprite=None, font_size=12):
        self.size = size
        self.color = color
        self.text = text
        self.sprite = sprite
        self.font_size = font_size

    def draw(self, position: RectanglePosition):
        tile_center = position.with_placement(Placement.CENTER)
        arcade.draw_rectangle_outline(tile_center.x, tile_center.y, self.size, self.size, arcade.color.BOSTON_UNIVERSITY_RED)
        if self.sprite is None:
            # Draw text and color as tile
            height = self.size * TILE_COLOR_HEIGHT
            center_y = tile_center.y - (self.size / 2) + (height / 2)
            arcade.draw_rectangle_filled(tile_center.x, center_y, self.size, height, self.color)
            arcade.draw_text(self.text, tile_center.x, center_y + self.size / 2, arcade.color.BLACK, font_size=self.font_size, anchor_x='center')
        else:
            # Draw sprite itself
            pass
