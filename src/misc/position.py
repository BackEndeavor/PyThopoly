from enum import Enum


class Placement(Enum):
    LEFT_BOTTOM = [(0, 0), (0, 0)]
    LEFT_TOP = [(0, 1), (0, -1)]
    CENTER = [(0.5, 0.5), (-0.5, -0.5)]
    RIGHT_BOTTOM = [(1, 0), (-1, 0)]
    RIGHT_TOP = [(1, 1), (-1, -1)]


class RectanglePosition:
    def __init__(self, x: float, y: float, width: int, height: int, placement: Placement):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.placement = placement

    def _calculate_position(self, new_placement: Placement):
        current_offset_x, current_offset_y = self.placement.value[1]
        normalized_x = self.x + (self.width * current_offset_x)
        normalized_y = self.y + (self.height * current_offset_y)

        new_offset_x, new_offset_y = new_placement.value[0]
        new_x = normalized_x + (self.width * new_offset_x)
        new_y = normalized_y + (self.height * new_offset_y)

        return new_x, new_y

    def move(self, placement: Placement):
        if placement == self.placement:
            return  # No change in placement, no need to move
        new_x, new_y = self._calculate_position(placement)
        self.x = new_x
        self.y = new_y
        self.placement = placement

    def resize(self, width, height):
        self.width = width
        self.height = height
        new_x, new_y = self._calculate_position(self.placement)
        self.x = new_x
        self.y = new_y

    def with_placement(self, placement: Placement):
        copied_position = self.copy()
        copied_position.move(placement)
        return copied_position

    def with_size(self, width, height):
        copied_position = self.copy()
        copied_position.resize(width, height)
        return copied_position

    def copy(self):
        return RectanglePosition(self.x, self.y, self.width, self.height, self.placement)

    def __mul__(self, other):
        return self.multiply(other)

    def __rmul__(self, other):
        return self.multiply(other)

    def multiply(self, other):
        match other:
            case int():
                return RectanglePosition(self.x * other, self.y * other, self.width, self.height, self.placement)
            case RectanglePosition():
                return RectanglePosition(self.x * other.x, self.y * other.y, self.width, self.height, self.placement)
            case tuple():
                return RectanglePosition(self.x * other[0], self.y * other[1], self.width, self.height, self.placement)
            case _:
                raise ValueError(f"Cannot multiply {type(other)} with {type(self)}")
