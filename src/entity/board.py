from typing import cast

import arcade
import pyglet
from pytiled_parser import ObjectLayer
from pytiled_parser.tiled_object import Point

from src.constants import PLAYER_PATH_CLASS


class Board:
    def __init__(self, tilemap_path, width, height):
        self.map = arcade.load_tilemap(tilemap_path)
        board_map_pixel_size = (self.map.tile_width * self.map.width, self.map.tile_height * self.map.height)
        self.offset = pyglet.math.Vec2((width - board_map_pixel_size[0]) / 2, (height - board_map_pixel_size[1]) / 2)
        self.map = arcade.load_tilemap(tilemap_path, offset=self.offset)
        self.scene = arcade.Scene.from_tilemap(self.map)
        self.width = self.map.width - 2
        self.height = self.map.height - 2

        alignments = cast(ObjectLayer, self.map.get_tilemap_layer('Alignments'))
        self.positions = {}
        for tiled_object in alignments.tiled_objects:
            if isinstance(tiled_object, Point):
                x, y = tiled_object.coordinates
                # We are converting from top left coordinate orientation to the bottom left
                object_type = tiled_object.class_
                if object_type not in self.positions:
                    self.positions[object_type] = {}
                self.positions[object_type][tiled_object.name] = (x, board_map_pixel_size[1] - y - 1)

    def draw(self):
        self.scene.draw()

    def index_to_position(self, index):
        tile_offset_x, tile_offset_y = self.positions[PLAYER_PATH_CLASS][str(index)]
        return self.offset.x + tile_offset_x, self.offset.y + tile_offset_y

    def center(self):
        left_bottom_x, left_bottom_y = self.offset.x, self.offset.y
        width = self.map.tile_width * (self.map.width / 2)
        height = self.map.tile_height * (self.map.height / 2)
        return left_bottom_x + width, left_bottom_y + height
