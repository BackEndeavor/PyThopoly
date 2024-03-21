import arcade
import pyglet


class Board:
    def __init__(self, tilemap_path, width, height):
        self.map = arcade.load_tilemap(tilemap_path)
        board_map_pixel_size = (self.map.tile_width * self.map.width, self.map.tile_height * self.map.height)
        self.center_offset = pyglet.math.Vec2((width - board_map_pixel_size[0]) / 2, (height - board_map_pixel_size[1]) / 2)
        self.map = arcade.load_tilemap(tilemap_path, offset=self.center_offset)
        self.scene = arcade.Scene.from_tilemap(self.map)
        self.width = self.map.width - 2
        self.height = self.map.height - 2

    def draw(self):
        self.scene.draw()

    def index_to_position(self, index):
        row, column = self.index_to_board_position(index)
        offset_x, offset_y = 0, 0
        edge = self.edge(index)
        if edge == -1:
            offset_x = 0.5
            offset_y = 0.5
        if edge == 0:
            offset_x = 0.5
            offset_y = 0.5
        if edge == 1:
            offset_x = 0.5
            offset_y = 0.5
        if edge == 2:
            offset_x = -0.5
            offset_y = -0.5
        if edge == 3:
            offset_y = 0.5

        left_top_x, left_top_y = self.center_offset.x + self.map.tile_width, self.center_offset.y + self.map.tile_height * (self.map.width - 1)
        return left_top_x + ((row + offset_x) * self.map.tile_width), left_top_y + ((column + offset_y) * self.map.tile_height)

    def center(self):
        left_bottom_x, left_bottom_y = self.center_offset.x, self.center_offset.y
        width = self.map.tile_width * (self.map.width / 2)
        height = self.map.tile_height * (self.map.height / 2)
        return left_bottom_x + width, left_bottom_y + height

    def is_corner(self, index):
        return self.edge(index) == -1

    def edge(self, index):
        grid_size = self.width
        per_edge = grid_size - 1
        if index % per_edge == 0:
            return -1
        return index // per_edge

    def index_to_board_position(self, index):
        grid_size = self.width
        per_edge = grid_size - 1
        edge = index // per_edge
        pos = index % per_edge

        if edge == 0:
            return pos, 0
        elif edge == 1:
            return grid_size, -pos - 1
        elif edge == 2:
            return per_edge - pos + 1, -grid_size
        elif edge == 3:
            return 0, -per_edge + pos - 1
        else:
            return 0, 0
