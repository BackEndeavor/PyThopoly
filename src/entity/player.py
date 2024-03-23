import arcade

from src.animation.easing import ease_in_out_quad
from src.animation.transition import MoveTransition
from src.constants import PLAYER_PATH_CLASS, MOVE_TRANSITION_SPEED


class Player(MoveTransition):
    def __init__(self, board_map, radius, position_index=0, money=0):
        super().__init__(MOVE_TRANSITION_SPEED, easing=ease_in_out_quad)
        self.board_map = board_map
        self.radius = radius
        self.money = money
        self.position_index = position_index

        x, y = self.board_map.index_to_position(self.position_index)
        self.current_x = x
        self.current_y = y
        self._set_start_position(x, y)

    def draw(self):
        arcade.draw_circle_filled(self.current_x, self.current_y, self.radius, arcade.color.GOLD)

    def update(self):
        self.update_animation()

        x, y = self.board_map.index_to_position(self.position_index)

        if self.current_x == x and self.current_y == y:
            return

        if self.is_animating():
            return

        self.move(x, y)

    def next_step(self, amount):
        new_position = self.position_index + amount
        if new_position not in self.board_map.positions[PLAYER_PATH_CLASS]:
            self.position_index = new_position % len(self.board_map.positions[PLAYER_PATH_CLASS])
            return
        self.position_index += amount

    def current_position(self) -> (float, float):
        return self.current_x, self.current_y

    def update_position(self, x, y):
        self.current_x = x
        self.current_y = y


